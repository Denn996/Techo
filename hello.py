
#!usr/bin/env python3

print("--- Customer Information ---")
name = input("Enter customer name: ")
age = int(input("Enter customer age: ")) 


print(f"\nWelcome to Duka Smart, {name}! (Age: {age})")


receipt_items = []
subtotal = 0.0

print("\n--- Enter 3 Items ---")
for i in range(1, 4):
    item_name = input(f"Item {i} name: ")
    quantity = int(input(f"Quantity for {item_name}: "))
    price = float(input(f"Price per unit for {item_name} (KES): "))
    

    line_total = quantity * price
    subtotal += line_total
    
    
    receipt_items.append({
        "Name": item_name,
        "Quantity": quantity,
        "Total": line_total
    })

vat = float(subtotal * 0.16)
grand_total = subtotal + vat

print("\n" + "="*40)
print(f"Welcome to Duka Smart, {name}! (Age: {age})\n")
print("--- RECEIPT ---")


for index, item in enumerate(receipt_items, start=1):
    print(f"{index}. {item['Name']:<15} x{item['Quantity']:<2} =  KES {item['Total']:.2f}")

print("\n")
print(f"{'Subtotal':<10} :  KES {subtotal:.2f}")
print(f"{'VAT (16%)':<10} :  KES {vat:.2f}")
print(f"{'TOTAL':<10} :  KES {grand_total:.2f}")
print("="*40)


print("\n--- Payment ---")
print(f"Amount Due: KES {grand_total:.2f}")
cash_paid = float(input("Enter cash paid by customer (KES): "))


if cash_paid >= grand_total:

    change = cash_paid - grand_total
    print("\nPayment Successful!")
    print(f"{'Cash paid':<10} :  KES {cash_paid:.2f}")
    print(f"{'Change':<10} :  KES {change:.2f}")
else:
    
    shortfall = grand_total - cash_paid
    print("\nPayment Failed!")
    print(f"You have a shortfall of KES {shortfall:.2f}. Please provide more cash.")



    print("Thank you for shopping at Duka smart.")



    
