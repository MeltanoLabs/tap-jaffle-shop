"""Custom client handling, including JaffleShopStream base class."""

from __future__ import annotations

import abc
import typing as t

from jafgen.simulation import Simulation
from singer_sdk import Tap
from singer_sdk.streams import Stream


class JaffleShopStream(Stream, metaclass=abc.ABCMeta):
    """Stream class for JaffleShop streams."""

    def __init__(
        self,
        tap: Tap,
        simulation: Simulation,
    ) -> None:
        self._simulation = simulation
        super().__init__(tap=tap, schema=None, name=self.name)

    def get_records(self, context: dict | None) -> t.Iterable[dict]:
        """Return a generator of record-type dictionary objects.

        Args:
            context: Stream partition or context dictionary. (Not used.)
        """
        list_of_record_tuples: list = self._simulation.__dict__[self.name]
        for record_tuple in list_of_record_tuples:
            # TODO: Return a real records dict with actual field names
            yield {"tuple_data": record_tuple}
