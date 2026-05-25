# Author: dennoh
# Golden Tulip Restaurant POS System

# ==========================================
# PART 1: Welcome & Menu
# ==========================================
print("*" * 45)
print("     Welcome to Golden Tulip Restaurant!     ")
print("*" * 45)

menu = {
    "1": {"name": "Pilau", "price": 250.00},
    "2": {"name": "Nyama Choma", "price": 400.00},
    "3": {"name": "Chapati", "price": 30.00},
    "4": {"name": "Ugali", "price": 50.00},
    "5": {"name": "Samosa", "price": 60.00}
}

print("\n--- Today's Menu ---")
for key, item in menu.items():
    print(f"[{key}] {item['name']:<15} : KES {item['price']:.2f}")

# ==========================================
# PART 2: Taking the Order
# ==========================================
order_items = []
grand_total = 0.0

print("\n--- Place Your Order ---")
print("(Type the item number to order, or type '0' when you are full)")

while True:
    choice = input("\nEnter item number (or 0 to finish): ")
    
    if choice == '0':
        break 
        
    elif choice in menu:
        quantity = int(input(f"How many portions of {menu[choice]['name']}? "))
        
        line_total = quantity * menu[choice]['price']
        grand_total += line_total
        
        order_items.append({
            "name": menu[choice]['name'],
            "quantity": quantity,
            "price": menu[choice]['price'],
            "total": line_total
        })
        print(f"--> Added {quantity}x {menu[choice]['name']} to your order.")
        
    else:
        print("Invalid choice, please look at the menu numbers and try again.")

# ==========================================
# PART 3: The Dining Experience & Receipt
# ==========================================
if len(order_items) > 0:
    print("\n" + "~" * 45)
    print("... Preparing your food ...")
    print("... Serving at your table ...")
    print("... Please enjoy your meal! ...")
    print("~" * 45 + "\n")

    print("=" * 45)
    print("         GOLDEN TULIP RECEIPT         ")
    print("=" * 45)
    
    for item in order_items:
        print(f"{item['name']:<15} x{item['quantity']:<2} @ KES {item['price']:<6.2f} = KES {item['total']:.2f}")
        
    print("-" * 45)
    print(f"{'TOTAL DUE':<31} = KES {grand_total:.2f}")
    print("=" * 45)
    
    # ==========================================
    # PART 4: Payment Processing (NEW)
    # ==========================================
    print("\n--- Checkout ---")
    
    # Keep asking for payment until they provide enough cash
    while True:
        cash_provided = float(input(f"Please enter payment amount (KES): "))
        
        if cash_provided >= grand_total:
            # They paid enough! Calculate change.
            change = cash_provided - grand_total
            print("\nPayment Successful!")
            print(f"Cash given: KES {cash_provided:.2f}")
            print(f"Change due: KES {change:.2f}")
            break # Exit the payment loop
            
        else:
            # They did not pay enough.
            shortfall = grand_total - cash_provided
            print(f"Insufficient funds! You are short by KES {shortfall:.2f}. Please provide the full amount.")

    print("\nThank you for choosing Golden Tulip Restaurant!")
    print("We hope to see you again soon.\n")
    
else:
    print("\nYou didn't order anything today.")
    print("Thank you for visiting Golden Tulip Restaurant, have a great day!")