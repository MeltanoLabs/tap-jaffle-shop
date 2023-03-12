"""JaffleShop tap class."""

from __future__ import annotations

from jafgen.simulation import Inventory, Simulation, Stock, pd
from singer_sdk import Tap
from singer_sdk import typing as th  # JSON schema typing helpers

from tap_jaffle_shop import streams
from tap_jaffle_shop.client import JaffleShopStream


class TapJaffleShop(Tap):
    """JaffleShop tap class."""

    name = "tap-jaffle-shop"

    config_jsonschema = th.PropertiesList(
        th.Property(
            "years",
            th.NumberType,
            required=True,
            default=1,
            description="The number of years to simulate data for.",
        ),
        th.Property(
            "stream_name_prefix",
            th.StringType,
            required=True,
            default="tap_jaffle_shop-raw_",
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
            A Simulation object with dataframes appended.
        """
        sim = Simulation(years=self.config["years"])

        sim.run_simulation()

        # Note: The following logic is copied from `Simulation.save_results()` and may
        # not be stable across versions.
        #
        # Source:
        # https://github.com/dbt-labs/jaffle-shop-generator/blob/0806cb627139238225503f019af042e4aa39f92e/jafgen/simulation.py#L106
        sim.df_customers = pd.DataFrame.from_dict(
            customer.to_dict() for customer in sim.customers.values()
        )
        sim.df_orders = pd.DataFrame.from_dict(order.to_dict() for order in sim.orders)
        sim.df_items = pd.DataFrame.from_dict(
            item.to_dict() for order in sim.orders for item in order.items
        )
        sim.df_stores = pd.DataFrame.from_dict(
            market.store.to_dict() for market in sim.markets
        )
        sim.df_products = pd.DataFrame.from_dict(Inventory.to_dict())
        sim.df_supplies = pd.DataFrame.from_dict(Stock.to_dict())

        return sim

    def discover_streams(self) -> list[streams.JaffleShopStream]:
        """Return a list of discovered streams.

        Returns:
            A list of discovered streams.
        """
        sim = self.create_simulation()
        name_prefix = self.config.get("stream_name_prefix", "")
        stream_types: list[type[JaffleShopStream]] = [
            streams.StoresStream,
            streams.CustomersStream,
            streams.ProductsStream,
            streams.OrdersStream,
            streams.ItemsStream,
            streams.SuppliesStream,
        ]
        return [
            stream_type(self, sim, name=name_prefix + stream_type.base_name)
            for stream_type in stream_types
        ]


if __name__ == "__main__":
    TapJaffleShop.cli()
