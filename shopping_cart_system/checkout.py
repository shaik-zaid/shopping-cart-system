# checkout.py
from .data_model import cart

def checkout():
    if not cart:
        print("\nCart is empty. Nothing to checkout.\n")
        return

    print("\n===== Checkout =====")
    total = 0
    for c in cart:
        subtotal = c["price"] * c["quantity"]
        total += subtotal
        print(f"{c['name']} - ₹{c['price']} x {c['quantity']} = ₹{subtotal}")

    print(f"\nFinal Total: ₹{total}")
    print("Thank you for shopping with us!\n")
    cart.clear()
