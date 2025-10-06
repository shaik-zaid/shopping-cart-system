# add_to_cart.py
from .data_model import products, cart, MAX_CART_ITEMS
from .helpers import find_product, find_in_cart

def add_to_cart():
    if len(cart) >= MAX_CART_ITEMS:
        print("\nCart is full! Remove an item before adding more.\n")
        return

    try:
        product_id = int(input("Enter Product ID to add: "))
        quantity = int(input("Enter quantity: "))
    except ValueError:
        print("\nInvalid input. Please enter numbers only.\n")
        return

    product = find_product(product_id)
    if not product:
        print("\nProduct not found.\n")
        return

    existing_item = find_in_cart(product_id)
    if existing_item:
        existing_item["quantity"] += quantity
        print(f"\nUpdated quantity of {product['name']} to {existing_item['quantity']}.\n")
    else:
        cart.append({
            "id": product["id"],
            "name": product["name"],
            "price": product["price"],
            "quantity": quantity
        })
        print(f"\nAdded {product['name']} (x{quantity}) to cart.\n")
