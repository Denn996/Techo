import random

#Title of the game and welcome message
print("*" * 50)
print("        THE NUMBER GUESSING GAME         ")
print("*" * 50)

name = input("Enter your name: ")
print(f"Helloo {name}, welcome to the Guess Game!")

#Game instructions
print("I am thinking of a secret number between 1 and 100.")
print("You have exactly 5 attempts to guess the number. Good luck!")
print("You start with a score of 100, and each wrong guess will cost you 20 points. Try to guess the number in as few attempts as possile to maximize your score!")


#Generate a random secret number between 1 and 100
secret_number = random.randint(1, 100)
attempts = 0
max_attempts = 5
score = 100

#Game loop
while True:
    attempts_left = max_attempts - attempts
    print(f"\nYou have {attempts_left} attempts left. Your current score is {score}.")

    guess_number = input("Enter your guess (or type 'quit' to exit): ")

    #Check if user wants to quit the game
    if guess_number.lower() == 'quit':
        print(f"\nThanks for playing! The secret number was {secret_number}.")
        break

    #Validate user input
    guess = int(guess_number)
    attempts += 1

    #Check the user's guess against the secret number
    if guess == secret_number:
        print("\n" + "=" * 50)
        print(" CONGRATULATIONS! ")
        print(f"You guessed the secret number {secret_number} in {attempts} attempts!")
        print(f"Your final score is {score}.")
        print("=" * 50 + "\n")
        break

    elif guess < secret_number:
        print("Too low! Try a higher number.")
        score -= 20

    elif guess > secret_number:
        print("Too high! Try a lower number.")
        score -= 20

    #Check if the user has used all the attempts
    if attempts == max_attempts:
        print("\n" + "=" * 50)
        print(" GAME OVER! ")
        print(f"You are out of attempts! The secret number was {secret_number}.")
        print(f"Your final score is: {score}/100")
        print("=" * 50 + "\n")
        break