# 01_simple_calorie_counter.py
# A beginner-friendly calorie counter.
# It uses pre-stored food data in a small table-like dictionary.
# Goal:
# 1. Run the file and observe the output.
# 2. Read the code and understand how the food data is stored.
# 3. Change food quantities or add a new food item.

# This dictionary acts like a tiny table.
# Key = food name
# Value = calories per unit
food_calories = {
    "banana": 105,
    "apple": 95,
    "bread_slice": 80,
    "egg": 78,
    "coffee": 5,
    "rice_bowl": 220,
    "samosa": 260,
}

# This is a sample meal plan for one day.
# Key = food name
# Value = how many units were eaten
meal_plan = {
    "banana": 1,
    "egg": 2,
    "bread_slice": 2,
    "coffee": 1,
    "samosa": 1,
}

# Function 1: show the food table.
def show_food_table(food_table):
    print("Available food items and calories")
    print("-" * 38)
    print(f"{'Food':<15} {'Calories per unit':>18}")
    print("-" * 38)

    for food, calories in food_table.items():
        print(f"{food:<15} {calories:>18}")

    print("-" * 38)

# Function 2: calculate total calories for a meal plan.
def calculate_total(meal, food_table):
    total = 0

    print("\nYour meal summary")
    print("-" * 55)
    print(f"{'Food':<15} {'Qty':>5} {'Calories each':>15} {'Total':>12}")
    print("-" * 55)

    for food, quantity in meal.items():
        calories_each = food_table[food]
        calories_for_food = quantity * calories_each
        total = total + calories_for_food
        print(f"{food:<15} {quantity:>5} {calories_each:>15} {calories_for_food:>12}")

    print("-" * 55)
    print(f"{'Grand total':<15} {'':>5} {'':>15} {total:>12}")
    return total

# Step 1: show the stored food data.
show_food_table(food_calories)

# Step 2: calculate the total.
total_calories = calculate_total(meal_plan, food_calories)

# Step 3: print a simple message.
print()
if total_calories < 400:
    print("This looks like a light meal plan.")
elif total_calories < 800:
    print("This looks like a medium meal plan.")
else:
    print("This looks like a heavy meal plan.")

# Try this:
# 1. Change the quantities in meal_plan.
# 2. Add a new food item to food_calories, for example:
#    "orange": 62
# 3. Then add that food to meal_plan.
# 4. Change 'coffee' from 5 to 50 and see what happens.
