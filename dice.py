import random

print("*" * 40)
print("        DICE ROLLING SIMULATOR        ")
print("*" * 40)

name = input("What is your name? ")
print(" ")
print(f"Hello, {name}! Let's roll some dice!")
print(" ")
print("You can roll a die with any number of sides. Let's get started!")
print(" ")

while True:
    print(" ")
    try:
        sides = int(input("Enter the number of sides on the die (or '0' to quit): "))
        if sides == 0:
            print(" ")
            print("Thanks for playing! Goodbye!")
            break
            
        elif sides < 1:
            print(" ")
            print("Please enter a positive integer for the number of sides.")
            continue
        
        else:
            result = random.randint(1, sides)
            print(" ")
            print(f"You rolled a {result} on a {sides}-sided die!")
    except ValueError:
        print(" ")
        print("Invalid input. Please enter a valid number of sides.")
