# 01_hello_points_game.py
# A very first Python program.
# Goal: run it, read the code, then change a few values and run again.

# Variables store information.
name = "Ashish"
favorite_snack = "samosa"
points = 10
bonus = 5

# print() shows text on the screen.
print("Welcome to the tiny points game!")
print("Player:", name)
print("Favorite snack:", favorite_snack)

# Python can also do math.
total_points = points + bonus
print("Starting points:", points)
print("Bonus points:", bonus)
print("Total points:", total_points)

# We can combine values inside a sentence with an f-string.
print(f"{name} wins {total_points} snack points for choosing {favorite_snack}!")

# Try this:
# 1. Change the name.
# 2. Change the snack.
# 3. Change points and bonus.
# 4. Add another variable, such as level = 2, and print it.
