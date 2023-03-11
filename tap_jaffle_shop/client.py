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

    def __init__(
        self,
        tap: Tap,
        simulation: Simulation,
    ) -> None:
        """Store the simulation object, then call the base class constructor."""
        self._simulation = simulation
        super().__init__(tap=tap)

    def create_dataframe(self) -> pd.DataFrame:
        """Create a new dataframe object.

        Note: the results of this method will be automatically cached by the
        PandasStream base class.
        """
        return self._simulation.__dict__[f"df_{self.name}"]
