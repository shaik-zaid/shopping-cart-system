# remove_from_cart.py
from .data_model import cart
from .helpers import find_in_cart

def remove_from_cart():
    if not cart:
        print("\nCart is empty! Nothing to remove.\n")
        return

    try:
        product_id = int(input("Enter Product ID to remove: "))
    except ValueError:
        print("\nInvalid input. Please enter a number.\n")
        return

    item = find_in_cart(product_id)
    if not item:
        print("\nItem not found in cart.\n")
        return

    cart.remove(item)
    print(f"\nRemoved {item['name']} from cart.\n")
