"""JaffleShop tap class."""

from __future__ import annotations

from jafgen.simulation import Simulation
from singer_sdk import Tap
from singer_sdk import typing as th  # JSON schema typing helpers

# TODO: Import your custom stream types here:
from tap_jaffle_shop import streams


class TapJaffleShop(Tap):
    """JaffleShop tap class."""

    name = "tap-jaffle-shop"

    # TODO: Update this section with the actual config values you expect:
    config_jsonschema = th.PropertiesList(
        th.Property(
            "years",
            th.NumberType,
            required=True,
            default=2,
            description="The number of years to simulate data for.",
        ),
        th.Property(
            "stream_name_prefix",
            th.StringType,
            required=True,
            default="jaffle_shop_raw-",
            description=(
                "A name prefix to apply to all streams. Note that the dash ('-') "
                "character will be interpreted by many targets as a delimiter "
                "between schema and table name."
            ),
        ),
    ).to_dict()

    def create_simulation(self):
        """Generate a simulation object from the tap's config.

        Returns:
            A Simulation object.
        """
        return Simulation(years=self.config["years"])

    def discover_streams(self) -> list[streams.JaffleShopStream]:
        """Return a list of discovered streams.

        Returns:
            A list of discovered streams.
        """
        sim = self.create_simulation()
        return [
            streams.StoresStream(self, sim),
            streams.CustomersStream(self, sim),
            streams.MarketsStream(self, sim),
            # streams.ProductsStream(self, sim),  # TODO: DEBUG 'products' stream
            streams.OrdersStream(self, sim),
            # streams.ItemsStream(self, sim),  # TODO: DEBUG 'items' stream
            # streams.SuppliesStream(self, sim),  # TODO: DEBUG 'supplies' stream
        ]


if __name__ == "__main__":
    TapJaffleShop.cli()
