# 03_bill_splitter.py
# A realistic mini-program.
# Goal: help a group split a restaurant bill.

# We convert input text into numbers with float() and int().
bill_amount = float(input("Enter the total bill amount: "))
tip_percent = float(input("Enter tip percentage (for example 10 or 12.5): "))
people = int(input("How many people are sharing the bill? "))

# A function makes the calculation easy to reuse.
def calculate_share(bill, tip_pct, group_size):
    tip_amount = bill * tip_pct / 100
    final_total = bill + tip_amount
    share_per_person = final_total / group_size
    return tip_amount, final_total, share_per_person

# We call the function and store all 3 returned values.
tip_amount, final_total, share_per_person = calculate_share(bill_amount, tip_percent, people)

print("\n--- Bill Summary ---")
print(f"Original bill: {bill_amount:.2f}")
print(f"Tip amount: {tip_amount:.2f}")
print(f"Final total: {final_total:.2f}")
print(f"Each person pays: {share_per_person:.2f}")

# A tiny extra message based on the bill size.
if share_per_person > 1000:
    print("This was a premium meal!")
else:
    print("That looks manageable.")

# Try this:
# 1. Change the number of people.
# 2. Try a different tip percentage.
# 3. Add a discount before the tip.
# 4. Change the final message thresholds.
