#!/usr/bin/env python3

print("*" * 20)
print("    PUZZLE GAME    ")
print("*" * 20)

name = input("Enter your name: ")
print(f"Hellooo {name}, welcome to the puzzle game!")

import random
number = random.randint(1, 100)
print(f"Random number generated: {number}")


even = number % 2 == 0
odd = number % 2 != 0


while number != 1:
    if number % 2 == 0:
        print(f"{number} is an even number, Half of {number} is: {number // 2}.")
        number = number // 2
        
    else:
        print(f"{number} is an odd number, Three times {number} plus one is: {number * 3 + 1}.")
        number = number * 3 + 1



print("Congratulations! You have reached the end of the puzzle game.")
        


