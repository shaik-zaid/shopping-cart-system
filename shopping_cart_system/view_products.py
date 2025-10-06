# view_products.py
from .data_model import products

def view_products():
    print("\n===== Available Products =====")
    for p in products:
        print(f"ID: {p['id']} | {p['name']} - ₹{p['price']}")
    print()
