"""Stream type classes for tap-jaffle-shop."""

from __future__ import annotations

from singer_sdk import typing as th  # JSON Schema typing helpers

from tap_jaffle_shop.client import JaffleShopStream


class StoresStream(JaffleShopStream):
    """List of Jaffle Shop stores."""

    name = "stores"
    # TODO: Identify primary keys, if any
    # primary_keys = ["id"]

    # TODO: Define or detect the real schema
    schema = th.PropertiesList(th.Property("tuple_data", th.StringType)).to_dict()


class MarketsStream(JaffleShopStream):
    """List of Jaffle Shop stores."""

    name = "markets"
    # TODO: Identify primary keys, if any
    # primary_keys = ["id"]

    # TODO: Define or detect the real schema
    schema = th.PropertiesList(th.Property("tuple_data", th.StringType)).to_dict()


class CustomersStream(JaffleShopStream):
    """List of Jaffle Shop stores."""

    name = "customers"
    # TODO: Identify primary keys, if any
    # primary_keys = ["id"]

    # TODO: Define or detect the real schema
    schema = th.PropertiesList(th.Property("tuple_data", th.StringType)).to_dict()


class OrdersStream(JaffleShopStream):
    """List of Jaffle Shop stores."""

    name = "orders"
    # TODO: Identify primary keys, if any
    # primary_keys = ["id"]

    # TODO: Define or detect the real schema
    schema = th.PropertiesList(th.Property("tuple_data", th.StringType)).to_dict()


class ProductsStream(JaffleShopStream):
    """List of Jaffle Shop stores."""

    name = "products"
    # TODO: Identify primary keys, if any
    # primary_keys = ["id"]

    # TODO: Define or detect the real schema
    schema = th.PropertiesList(th.Property("tuple_data", th.StringType)).to_dict()


class ItemsStream(JaffleShopStream):
    """List of Jaffle Shop stores."""

    name = "items"
    # TODO: Identify primary keys, if any
    # primary_keys = ["id"]

    # TODO: Define or detect the real schema
    schema = th.PropertiesList(th.Property("tuple_data", th.StringType)).to_dict()


class SuppliesStream(JaffleShopStream):
    """List of Jaffle Shop stores."""

    name = "supplies"
    # TODO: Identify primary keys, if any
    # primary_keys = ["id"]

    # TODO: Define or detect the real schema
    schema = th.PropertiesList(th.Property("tuple_data", th.StringType)).to_dict()
