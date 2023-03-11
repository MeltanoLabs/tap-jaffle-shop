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
    ) -> None:
        self._dataframe: pd.DataFrame | None = None
        super().__init__(tap=tap, name=None, schema=None)

    @abc.abstractmethod
    def create_dataframe(self) -> pd.DataFrame:
        """Create a new dataframe object.

        Note: the results of this method will be automatically cached by the base class.
        """

    @property
    def dataframe(self) -> pd.DataFrame:
        """The pandas dataframe."""
        if self._dataframe is None:
            self._dataframe = self.create_dataframe()

        return self._dataframe

    def get_records(self, context: dict | None) -> t.Iterable[dict]:
        """Return a generator of record-type dictionary objects.

        Args:
            context: Stream partition or context dictionary. (Not used.)
        """
        for record_dict in self.dataframe.to_dict("records"):
            yield record_dict

    @property
    def schema(self) -> dict:
        """A JSON Schema dict that represents the stream's dataframe."""
        return th.PropertiesList(
            *[
                th.Property(
                    col,
                    PandasStream.pandas_dtype_to_jsonschema_type(
                        self.dataframe.dtypes[col]
                    )(),
                )
                for col in self.dataframe.columns
            ]
        ).to_dict()

    @classmethod
    def pandas_dtype_to_jsonschema_type(cls, dtype: str) -> Type[th.JSONTypeHelper]:
        """Returns a JSON Schema type definition for the Pandas dtype.json

        Uses ref table at: https://note.nkmk.me/en/python-pandas-dtype-astype/

        Returns:
            A JSONTypeHelper class representing the json schema type.
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
