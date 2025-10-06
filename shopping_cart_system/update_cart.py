# update_cart.py
from .data_model import cart
from .helpers import find_in_cart

def update_cart():
    if not cart:
        print("\nCart is empty! Nothing to update.\n")
        return

    try:
        product_id = int(input("Enter Product ID to update: "))
        quantity = int(input("Enter new quantity: "))
    except ValueError:
        print("\nInvalid input. Please enter numbers only.\n")
        return

    item = find_in_cart(product_id)
    if not item:
        print("\nItem not found in cart.\n")
        return

    if quantity <= 0:
        cart.remove(item)
        print(f"\nRemoved {item['name']} from cart.\n")
    else:
        item["quantity"] = quantity
        print(f"\nUpdated {item['name']} quantity to {quantity}.\n")
