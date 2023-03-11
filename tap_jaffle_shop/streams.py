"""Stream type classes for tap-jaffle-shop."""

from __future__ import annotations

from tap_jaffle_shop.client import JaffleShopStream


class StoresStream(JaffleShopStream):
    """List of Jaffle Shop stores."""

    name = "stores"
    primary_keys = ["id"]


class CustomersStream(JaffleShopStream):
    """List of Jaffle Shop customers."""

    name = "customers"
    primary_keys = ["id"]


class OrdersStream(JaffleShopStream):
    """List of Jaffle Shop orders."""

    name = "orders"
    primary_keys = ["id"]


class ProductsStream(JaffleShopStream):
    """List of Jaffle Shop products."""

    name = "products"
    primary_keys = ["sku"]


class ItemsStream(JaffleShopStream):
    """List of Jaffle Shop items."""

    name = "items"
    primary_keys = ["id"]


class SuppliesStream(JaffleShopStream):
    """List of Jaffle Shop supplies."""

    name = "supplies"
    primary_keys = ["id"]
