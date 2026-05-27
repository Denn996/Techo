#!usr/bin/env python3

print("*" * 50)
print("    NIMM(TIOUK TIOUK OR TSYNSHIDZI) GAME    ")
print("*" * 50)

name1 = input("Enter player 1 name: ")
name2 = input("Enter player 2 name: ")

print(f"Helloo {name1} and {name2}! Welcome to the NIMM game.")
print(" ")
print("The rules are simple: You can take 1 or 2 stones from the pile.")
print(" ")
print("The player who takes the last stone loses the game.")
print(" ")
print("The pile consist of 20 stones at the beginning of the game.")
print(" ")
print("Let's start the game!")

stones = 20

while True:
    print(" ")
    print(f"\nThere are {stones} stones left in the pile.")
    
    # Player 1's turn
    while True:
        print(" ")
        try:
            take = int(input(f"{name1}, how many stones do you want to take (1 or 2)? "))
            if take in [1, 2] and take <= stones:
                break
            else:
                print("Invalid input. Please enter 1 or 2, and it must not exceed the number of stones left.")
        except ValueError:
            print(" ")
            print("Invalid input. Please enter a number.")
    
    stones -= take
    if stones == 0:
        print(f"{name1} took the last stone. {name2} wins!")
        break
    
    # Player 2's turn
    while True:
        print(" ")
        try:
            take = int(input(f"{name2}, how many stones do you want to take (1 or 2)? "))
            if take in [1, 2] and take <= stones:
                break
            else:
                print("Invalid input. Please enter 1 or 2, and it must not exceed the number of stones left.")
        except ValueError:
            print(" ")
            print("Invalid input. Please enter a number.")
    
    stones -= take
    if stones == 0:
        print(" ")
        print(f"{name2} took the last stone. {name1} wins!")
        break