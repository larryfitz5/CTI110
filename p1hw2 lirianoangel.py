# Your Name: Angel Liriano
# Date: 09/28/2024
# Assignment Name: P1HW2_LirianoAngel
# A brief description of the project:
# This program collects the user's budget and the amount they will spend on gas, accommodation, and food.
# It calculates the total expenses, subtracts them from the budget, and displays the remaining amount.

# Step 1: Ask user for their budget
budget = float(input("Enter your budget: $"))

# Step 2: Ask user for their travel destination
destination = input("Enter your travel destination: ")

# Step 3: Ask user for the amount they will spend on gas
gas_expense = float(input("How much will you spend on gas? $"))

# Step 4: Ask user for the amount they will spend on accommodation
accommodation_expense = float(input("How much will you spend on accommodation? $"))

# Step 5: Ask user for the amount they will spend on food
food_expense = float(input("How much will you spend on food? $"))

# Step 6: Calculate total expenses
total_expenses = gas_expense + accommodation_expense + food_expense

# Step 7: Calculate the remaining amount after expenses
remaining_budget = budget - total_expenses

# Step 8: Display the results
print("\n---------- Travel Expenses ----------")
print(f"Location: {destination}")
print(f"Initial Budget: ${budget:.2f}")
print(f"Fuel: ${gas_expense:.2f}")
print(f"Accommodation: ${accommodation_expense:.2f}")
print(f"Food: ${food_expense:.2f}")
print(f"Total Expenses: ${total_expenses:.2f}")
print(f"Remaining Balance: ${remaining_budget:.2f}")
