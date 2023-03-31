"""Custom client handling, including JaffleShopStream base class."""

from __future__ import annotations

import abc

from jafgen.simulation import Simulation
from singer_sdk import Tap

from tap_jaffle_shop.pandas import PandasStream, pd


class JaffleShopStream(PandasStream, metaclass=abc.ABCMeta):
    """Stream class for JaffleShop streams.

    This class builds upon the `PandasStream` class, which provides core capabilities
    for streams that are built on Pandas data frames.
    """

    batch_size = 100000

    def __init__(
        self,
        tap: Tap,
        simulation: Simulation,
        name: str,
    ) -> None:
        """Store the simulation object, then call the base class constructor.

        Args:
            tap: The tap object.
            simulation: A jaffle shop simulation object.
            name: The stream name to use during discovery and when sending data to the
                target.
        """
        self._simulation = simulation
        super().__init__(tap=tap, name=name)

    def create_dataframe(self) -> pd.DataFrame:
        """Create a new dataframe object.

        Note: the results of this method will be automatically cached by the
        PandasStream base class.

        Returns:
            A newly created DataFrame object.
        """
        return self._simulation.__dict__[f"df_{self.base_name}"]

    @property
    @abc.abstractmethod
    def base_name(self) -> str:
        """Get base name of the stream, before applying a prefix."""
