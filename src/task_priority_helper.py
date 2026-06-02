# 04_task_priority_helper.py
# A realistic beginner script.
# Goal: rank 3 tasks using simple scores.

print("Task Priority Helper")
print("Give each task a score from 1 to 5.")
print("Higher urgency and impact should increase priority.\n")

# A function calculates a simple score.
# We give slightly more weight to impact than urgency.
def task_score(urgency, impact):
    return urgency + (impact * 2)

# This function prints a result nicely.
def show_task_result(task_name, urgency, impact):
    score = task_score(urgency, impact)
    print(f"Task: {task_name} | Urgency: {urgency} | Impact: {impact} | Score: {score}")
    return score

# Collect data for task 1.
task1_name = input("Enter task 1 name: ")
task1_urgency = int(input("Urgency for task 1 (1-5): "))
task1_impact = int(input("Impact for task 1 (1-5): "))
print()

# Collect data for task 2.
task2_name = input("Enter task 2 name: ")
task2_urgency = int(input("Urgency for task 2 (1-5): "))
task2_impact = int(input("Impact for task 2 (1-5): "))
print()

# Collect data for task 3.
task3_name = input("Enter task 3 name: ")
task3_urgency = int(input("Urgency for task 3 (1-5): "))
task3_impact = int(input("Impact for task 3 (1-5): "))
print()

# Calculate and show scores.
score1 = show_task_result(task1_name, task1_urgency, task1_impact)
score2 = show_task_result(task2_name, task2_urgency, task2_impact)
score3 = show_task_result(task3_name, task3_urgency, task3_impact)

print("\n--- Suggested first priority ---")

# Decide which task should come first.
if score1 >= score2 and score1 >= score3:
    print("Start with:", task1_name)
elif score2 >= score1 and score2 >= score3:
    print("Start with:", task2_name)
else:
    print("Start with:", task3_name)

# Try this:
# 1. Change the formula in task_score().
# 2. Give urgency more weight than impact.
# 3. Add a 4th task.
# 4. Add another factor such as 'effort' or 'customer importance'.
