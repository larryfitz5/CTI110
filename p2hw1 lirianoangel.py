# Angel Liriano
# 10-11-24
# P2HW1_LirianoAngel
# This program calculates travel expenses and formats the output to align data properly and include currency format.

# User Inputs
budget = float(input("Enter Budget: "))
destination = input("Enter your travel destination: ")
gas = float(input("How much do you think you will spend on gas? "))
accommodation = float(input("Approximately, how much will you need for accommodation/hotel? "))
food = float(input("Last, how much do you need for food? "))

# Calculating remaining balance
total_expenses = gas + accommodation + food
remaining_balance = budget - total_expenses

# Displaying formatted output
print("\n------------Travel Expenses------------")
print(f"{'Location:':<20}{destination}")
print(f"{'Initial Budget:':<20}${budget:,.2f}")
print(f"{'Fuel:':<20}${gas:,.2f}")
print(f"{'Accommodation:':<20}${accommodation:,.2f}")
print(f"{'Food:':<20}${food:,.2f}")
print("----------------------------------------")
print(f"{'Remaining Balance:':<20}${remaining_balance:,.2f}")
