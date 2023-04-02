"""Stream type classes for tap-jaffle-shop."""

from __future__ import annotations

from tap_jaffle_shop.client import JaffleShopStream


class StoresStream(JaffleShopStream):
    """List of Jaffle Shop stores."""

    base_name = "stores"
    primary_keys = ["id"]


class CustomersStream(JaffleShopStream):
    """List of Jaffle Shop customers."""

    base_name = "customers"
    primary_keys = ["id"]


class OrdersStream(JaffleShopStream):
    """List of Jaffle Shop orders."""

    base_name = "orders"
    primary_keys = ["id"]


class ProductsStream(JaffleShopStream):
    """List of Jaffle Shop products."""

    base_name = "products"
    primary_keys = ["sku"]


class ItemsStream(JaffleShopStream):
    """List of Jaffle Shop items."""

    base_name = "items"
    primary_keys = ["id"]


class SuppliesStream(JaffleShopStream):
    """List of Jaffle Shop supplies."""

    base_name = "supplies"
    primary_keys = ["id", "sku"]
