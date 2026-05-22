#!usr/bin/env python3

#Assigning the restaurant name
print("\n--- GOLDEN TULIP RESTAURANT ---")

client_name = input("Enter your name: ")
print(f"Welcome to Golden Tulip Restaurant, {client_name}!")

print("\n--- MENU ---")


menu_items = [
    {"name": "Chapati", "quantity": 1, "price": 20.00},
    {"name": "Pilau", "quantity": 1, "price": 250.00},
    {"name": "Samosa", "quantity": 1, "price": 50.00},
    {"name": "Pizza", "quantity": 1, "price": 800.00},
    {"name": "beef", "quantity": 1 , "price":150.00},
    {"name": "Black tea", "quantity": 1 ,"price":40.00}
]


for item in menu_items:
    
    line_total = item["quantity"] * item["price"]
    
    
    print(f"{item['name']:<10} x{item['quantity']:<2} @ KES {item['price']:<6.2f} = KES {line_total:.2f}")