# 02_number_guessing_game.py
# A simple number guessing game for beginners.
# Goal:
# 1. Run the game and play once.
# 2. Read the code and understand the loop and conditions.
# 3. Make small changes, such as a bigger number range.

import random

# These two numbers decide the difficulty.
# Easy first: the secret number will be between 1 and 20.
LOW = 1
HIGH = 20

# random.randint(a, b) gives a random whole number from a to b.
secret_number = random.randint(LOW, HIGH)

# We count how many guesses the player makes.
attempts = 0

print("Welcome to the number guessing game!")
print(f"I am thinking of a number between {LOW} and {HIGH}.")
print("Can you guess it?\n")

# Keep asking until the player gets it right.
while True:
    guess = int(input("Enter your guess: "))
    attempts = attempts + 1

    if guess < secret_number:
        print("Too low. Try a bigger number.\n")
    elif guess > secret_number:
        print("Too high. Try a smaller number.\n")
    else:
        print(f"Correct! The secret number was {secret_number}.")
        print(f"You guessed it in {attempts} attempts.")
        break

# Try this:
# 1. Change HIGH from 20 to 50 or 100.
# 2. Print a special message if attempts <= 3.
# 3. Add a line that shows 'You are very close!' when the guess is off by only 1.
# 4. Give the player only 5 attempts and print 'Game over' if they run out.
