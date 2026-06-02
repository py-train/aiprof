import random

# Function to get user input
def get_user_guess():
    while True:
        try:
            guess = int(input("Enter a number between 1 and 100: "))
            return guess
        except ValueError:
            print("That's not a valid number! Please try again.")

# Main function
def main():
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 5

    print("Welcome to the Number Guessing Game!")
    print(f"You have {max_attempts} attempts to guess the number.")

    # Loop for allowing user to guess the number
    while attempts < max_attempts:
        guess = get_user_guess()
        attempts += 1
        
        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You've guessed the number {secret_number} in {attempts} attempts.")
            break
    else:
        print(f"Sorry! You've used all your attempts. The number was {secret_number}.")

# Entry point of the program
if __name__ == "__main__":
    main()
