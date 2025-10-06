# __init__.py
# This file marks the directory as a Python package.
# It also helps with cleaner imports when using the module.

from .data_model import products, cart, MAX_CART_ITEMS
from .helpers import find_product, find_in_cart
from .view_products import view_products
from .add_to_cart import add_to_cart
from .view_cart import view_cart
from .update_cart import update_cart
from .remove_from_cart import remove_from_cart
from .checkout import checkout

__all__ = [
    "products",
    "cart",
    "MAX_CART_ITEMS",
    "find_product",
    "find_in_cart",
    "view_products",
    "add_to_cart",
    "view_cart",
    "update_cart",
    "remove_from_cart",
    "checkout"
]
