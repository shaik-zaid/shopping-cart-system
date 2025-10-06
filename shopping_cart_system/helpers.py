# helpers.py
from .data_model import products, cart

def find_product(product_id):
    for p in products:
        if p["id"] == product_id:
            return p
    return None

def find_in_cart(product_id):
    for c in cart:
        if c["id"] == product_id:
            return c
    return None
