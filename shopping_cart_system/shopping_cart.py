# shopping_cart.py
# Main menu and entry point

from .view_products import view_products
from .add_to_cart import add_to_cart
from .view_cart import view_cart
from .update_cart import update_cart
from .remove_from_cart import remove_from_cart
from .checkout import checkout

def menu():
    while True:
        print("""\n===== Shopping Cart =====
1. View Products
2. Add to Cart
3. View Cart
4. Update Cart
5. Remove from Cart
6. Checkout
7. Exit
============================""")

        choice = input("Enter your choice (1-7): ").strip()

        if choice == '1':
            view_products()
        elif choice == '2':
            add_to_cart()
        elif choice == '3':
            view_cart()
        elif choice == '4':
            update_cart()
        elif choice == '5':
            remove_from_cart()
        elif choice == '6':
            checkout()
        elif choice == '7':
            print("\nExiting program. Goodbye!\n")
            break
        else:
            print("\nInvalid choice! Please enter a number between 1 and 7.\n")


if __name__ == "__main__":
    menu()
