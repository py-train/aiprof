# 03_cows_and_bulls.py
# A beginner-friendly Cows and Bulls game.
# It is similar in spirit to Wordle, but uses numbers.
#
# Rules:
# - The computer chooses a secret number with unique digits.
# - You try to guess it.
# - A BULL means: correct digit, correct position.
# - A COW means: correct digit, wrong position.
#
# Beginner goal:
# 1. Run the file and play once.
# 2. Read the code and understand the functions.
# 3. Change DIGITS from 3 to 4 or 5 and run again.

import random

# You can change this number to make the game easier or harder.
# Try 3 first, then 4 later.
DIGITS = 3

# ANSI color codes for the terminal.
# Note: orange is not standard in many terminals, so bright yellow is used.
RESET = "\033[0m"
GREEN = "\033[92m"         # for bulls
ORANGE = "\033[93m"        # bright yellow / orange-like, for cows
CYAN = "\033[96m"
MAGENTA = "\033[95m"

# Function 1: generate a secret number with unique digits.
def generate_secret(length):
    digits = "0123456789"
    secret = ""

    while len(secret) < length:
        chosen_digit = random.choice(digits)

        # Avoid repeated digits.
        if chosen_digit not in secret:
            secret = secret + chosen_digit

    return secret

# Function 2: count cows and bulls.
def get_cows_and_bulls(secret, guess):
    bulls = 0
    cows = 0

    for index in range(len(secret)):
        if guess[index] == secret[index]:
            bulls = bulls + 1
        elif guess[index] in secret:
            cows = cows + 1

    return cows, bulls

secret_number = generate_secret(DIGITS)
attempts = 0

print(CYAN + "Welcome to Cows and Bulls!" + RESET)
print(f"I have picked a secret number with {DIGITS} unique digits.")
print("Bull = right digit in the right place.")
print("Cow  = right digit in the wrong place.")
print()

while True:
    guess = input(f"Enter a {DIGITS}-digit guess: ")

    # Basic checks to keep the game beginner-friendly.
    if len(guess) != DIGITS:
        print("Please enter the correct number of digits.\n")
        continue

    if not guess.isdigit():
        print("Please enter numbers only.\n")
        continue

    if len(set(guess)) != DIGITS:
        print("Please do not repeat digits in your guess.\n")
        continue

    attempts = attempts + 1
    cows, bulls = get_cows_and_bulls(secret_number, guess)

    print(
        f"Result: "
        + ORANGE + f"{cows} cow(s)" + RESET
        + " | "
        + GREEN + f"{bulls} bull(s)" + RESET
    )

    if bulls == DIGITS:
        print()
        print(MAGENTA + "You cracked the number!" + RESET)
        print(f"Secret number: {secret_number}")
        print(f"Attempts used: {attempts}")
        break

    print()

# Try this:
# 1. Change DIGITS from 3 to 4.
# 2. Add a maximum number of attempts.
# 3. Print 'Very close!' if bulls == DIGITS - 1.
# 4. Show previous guesses in a list.
# 5. Change colors or remove colors if your terminal does not support them.
