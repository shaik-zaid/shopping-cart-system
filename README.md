# 🛒 Shopping Cart System (Python Functions Only)

A simple, menu-driven **Shopping Cart System** built using **Python functions only** — no OOP, no database, and no file handling.  
This project is designed for beginners to understand how to structure modular Python applications using **lists, dictionaries, loops, and conditionals**.

---

## 📋 Features

✅ **View Products** – Display all available products with their IDs, names, and prices.  
✅ **Add to Cart** – Add a product to the cart with a specified quantity (max limit: 8 items).  
✅ **View Cart** – Display all items in the cart with subtotal and total price.  
✅ **Update Cart** – Modify the quantity of existing items in the cart.  
✅ **Remove from Cart** – Delete an item from the cart.  
✅ **Checkout** – Display final bill and clear the cart after purchase.  
✅ **Exit Program** – End the program safely.  

---

## 🗂️ Project Structure

```
shopping_cart_system/
│
├── data_model.py          # Stores predefined product list and empty cart
├── helpers.py             # Reusable utility functions (find_product, find_in_cart, etc.)
│
├── view_products.py       # Display all available products
├── add_to_cart.py         # Add product to cart (check max limit)
├── view_cart.py           # Show cart items with total
├── update_cart.py         # Edit existing cart quantities
├── remove_from_cart.py    # Remove an item from cart
├── checkout.py            # Display final bill and clear cart
│
└── shopping_cart.py       # Main menu (entry point)
```

---

## 💾 Data Model

Products and cart items are stored in **lists of dictionaries** (in-memory data, no external files).

### 🛍️ Products
```python
products = [
    {"id": 1, "name": "Laptop", "price": 45000},
    {"id": 2, "name": "Smartphone", "price": 15000},
    {"id": 3, "name": "Headphones", "price": 2000},
    {"id": 4, "name": "Keyboard", "price": 1200},
    {"id": 5, "name": "Mouse", "price": 800},
    {"id": 6, "name": "Charger", "price": 500},
    {"id": 7, "name": "USB Cable", "price": 300},
    {"id": 8, "name": "Backpack", "price": 2500}
]
```

### 🧺 Cart
```python
cart = [
    {"id": 1, "name": "Laptop", "price": 45000, "quantity": 1},
    {"id": 3, "name": "Headphones", "price": 2000, "quantity": 2}
]
```

Each cart item contains:
- `id` – Unique product ID  
- `name` – Product name  
- `price` – Product price  
- `quantity` – Number of items added  

---

## ⚙️ Functional Overview

| Function | Description |
|-----------|--------------|
| `view_products()` | Display all available products |
| `add_to_cart()` | Add a new product to the cart |
| `view_cart()` | Display all cart items and total cost |
| `update_cart()` | Update the quantity of items |
| `remove_from_cart()` | Remove a product from the cart |
| `checkout()` | Display final bill and clear cart |
| `menu()` | Show main menu and handle user input |

---

## 🧠 Requirements

- Python **3.8+**
- Basic understanding of:
  - Lists & Dictionaries  
  - Functions  
  - Loops & Conditionals  
  - Input/Output operations

---

## ▶️ How to Run

1. **Clone or Download** this repository  
   ```bash
   git clone https://github.com/shaik-zaid/shopping-cart-system.git
   cd shopping-cart-system
   ```

2. **Run the main file**
   ```bash
   python -m shopping_cart_system.shopping_cart
   ```
   ✅ This is the correct way to run modular Python projects.  
   *(Do not use `python shopping_cart.py` directly — it will cause import errors.)*

3. **Follow the menu prompts**

```
===== Shopping Cart =====
1. View Products
2. Add to Cart
3. View Cart
4. Update Cart
5. Remove from Cart
6. Checkout
7. Exit
============================
Enter your choice:
```

---

## 🧩 Example Usage

**Adding to Cart:**
```
Enter Product ID to add: 2
Enter quantity: 3

Added Smartphone (x3) to cart.
```

**Viewing Cart:**
```
===== Your Cart =====
Smartphone - ₹15000 x 3 = ₹45000

Total Amount: ₹45000
```

**Updating Quantity:**
```
Enter Product ID to update: 2
Enter new quantity: 1

Updated Smartphone quantity to 1.
```

**Checkout:**
```
===== Checkout =====
Smartphone - ₹15000 x 1 = ₹15000

Final Total: ₹15000
Thank you for shopping with us!
```

---

## 🧹 Exit Option
Choose **7** from the menu to exit the program:
```
Exiting Shopping Cart System. Goodbye!
```

---

## 🧩 Learning Goals

This project helps you learn:
- Function-based modular programming  
- Code organization and reusability  
- Data management with lists and dictionaries  
- Console-based user interaction  
- Input validation and error handling  

---

## 📁 Recommended Next Steps

After mastering this, you can improve the project by:
- Adding **file storage (JSON/CSV)** to save cart data  
- Using **OOP (classes)** for better scalability  
- Creating a **Tkinter GUI** or **Flask Web App**  
- Implementing **discounts or taxes**  
- Adding **unit tests** for each function  

---

## 👨‍💻 Author

**Shaik Zaid**  
📧 [shaikzaid9393@gmail.com]  
💼 [LinkedIn Profile](https://www.linkedin.com/in/shaik-zaid-832407331/)  
🐙 [GitHub](https://github.com/shaik-zaid)

---

⭐ **If you find this project helpful, please star the repository!**
