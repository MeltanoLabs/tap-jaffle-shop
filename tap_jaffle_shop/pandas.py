"""Custom client handling, including JaffleShopStream base class."""

from __future__ import annotations

import abc
import typing as t
from typing import Type

from jafgen.simulation import pd
from singer_sdk import Tap
from singer_sdk import typing as th  # Typing Helper classes
from singer_sdk.streams import Stream


class PandasStream(Stream, metaclass=abc.ABCMeta):
    """Stream class for Pandas dataframe streams."""

    def __init__(
        self,
        tap: Tap,
        name: str | None = None,
    ) -> None:
        """Set up an empty dataframe cache object, then call the base class constructor.

        Args:
            tap: The tap object.
            name: The name of the stream, to use during discovery and when sending
                data to the target. (Optional.)
        """
        self._dataframe: pd.DataFrame | None = None
        self._schema: dict | None = None
        super().__init__(tap=tap, name=name, schema=None)

    @abc.abstractmethod
    def create_dataframe(self) -> pd.DataFrame:
        """Create a new dataframe object.

        Note: the results of this method will be automatically cached by the base class.
        """

    @property
    def dataframe(self) -> pd.DataFrame:
        """The pandas dataframe.

        Note: The property is automatically cached to preserve compute cycles and ensure
        the dataset itself is stable.

        Returns:
            A dataframe object.
        """
        if self._dataframe is None:
            self._dataframe = self.create_dataframe()

        return self._dataframe

    def get_records(self, context: dict | None) -> t.Iterable[dict]:
        """Return a generator of record-type dictionary objects.

        Args:
            context: Stream partition or context dictionary. (Not used.)

        Yields:
            A stream of dictionary objects, one per record.
        """
        for record_dict in self.dataframe.to_dict("records"):
            yield record_dict

    @property
    def schema(self) -> dict:
        """A JSON Schema dict that represents the stream's dataframe.

        Returns:
            A dictionary object describing the stream's JSON Schema.
        """
        if self._schema is not None:
            return self._schema

        def _get_type(col: str) -> th.JSONTypeHelper:
            if str(col).endswith("_at"):
                # Pandas base class cannot detect datetime values
                # https://github.com/MeltanoLabs/tap-jaffle-shop/issues/2
                return th.DateTimeType()

            return PandasStream.pandas_dtype_to_jsonschema_type(
                self.dataframe.dtypes[col]
            )()

        self._schema = th.PropertiesList(
            *[th.Property(col, _get_type(col)) for col in self.dataframe.columns]
        ).to_dict()
        return self._schema

    @classmethod
    def pandas_dtype_to_jsonschema_type(cls, dtype: str) -> Type[th.JSONTypeHelper]:
        """Returns a JSON Schema type definition for the Pandas dtype.json

        Uses ref table at: https://note.nkmk.me/en/python-pandas-dtype-astype/

        Args:
            dtype: The dtype as described from Pandas or Numpy.

        Returns:
            A JSONTypeHelper class representing the json schema type.

        Raises:
            ValueError: If the dtype cannot be converted to a JSON Schema type.
        """
        dtype = str(dtype)
        if "int" in dtype:
            return th.IntegerType

        if "float" in dtype:
            return th.NumberType

        if "complex" in dtype:
            return th.NumberType

        if dtype == "bool":
            return th.BooleanType

        if dtype == "unicode":
            return th.StringType

        if dtype == "object":
            return th.StringType

        raise ValueError(
            f"Could not detect JSON schema type for Pandas dtype '{dtype}'"
        )
