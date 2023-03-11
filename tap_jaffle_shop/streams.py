"""Stream type classes for tap-jaffle-shop."""

from __future__ import annotations

from tap_jaffle_shop.client import JaffleShopStream


class StoresStream(JaffleShopStream):
    """List of Jaffle Shop stores."""

    name = "stores"
    # TODO: Identify primary keys, if any
    # primary_keys = ["id"]


class CustomersStream(JaffleShopStream):
    """List of Jaffle Shop stores."""

    name = "customers"
    # TODO: Identify primary keys, if any
    # primary_keys = ["id"]


class OrdersStream(JaffleShopStream):
    """List of Jaffle Shop stores."""

    name = "orders"
    # TODO: Identify primary keys, if any
    # primary_keys = ["id"]


class ProductsStream(JaffleShopStream):
    """List of Jaffle Shop stores."""

    name = "products"
    # TODO: Identify primary keys, if any
    # primary_keys = ["id"]


class ItemsStream(JaffleShopStream):
    """List of Jaffle Shop stores."""

    name = "items"
    # TODO: Identify primary keys, if any
    # primary_keys = ["id"]


class SuppliesStream(JaffleShopStream):
    """List of Jaffle Shop stores."""

    name = "supplies"
    # TODO: Identify primary keys, if any
    # primary_keys = ["id"]
