# view_cart.py
from .data_model import cart

def view_cart():
    if not cart:
        print("\nYour cart is empty.\n")
        return

    print("\n===== Your Cart =====")
    total = 0
    for c in cart:
        subtotal = c["price"] * c["quantity"]
        total += subtotal
        print(f"{c['name']} - ₹{c['price']} x {c['quantity']} = ₹{subtotal}")
    print(f"\nTotal Amount: ₹{total}\n")
