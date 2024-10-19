# P3LAB_LirianoAngel
# This program calculates the most efficient breakdown of a monetary value into dollars, quarters, dimes, nickels, and pennies.

# Get input from the user
amount = float(input("Enter a monetary value: "))

# Convert the amount into cents (to avoid float precision issues)
cents = int(round(amount * 100))

# Calculate the number of dollars
dollars = cents // 100
cents = cents % 100

# Calculate the number of quarters
quarters = cents // 25
cents = cents % 25

# Calculate the number of dimes
dimes = cents // 10
cents = cents % 10

# Calculate the number of nickels
nickels = cents // 5
cents = cents % 5

# Remaining cents are pennies
pennies = cents

# Display the result, considering singular and plural forms
if dollars > 0:
    if dollars == 1:
        print(f"{dollars} dollar")
    else:
        print(f"{dollars} dollars")

if quarters > 0:
    if quarters == 1:
        print(f"{quarters} quarter")
    else:
        print(f"{quarters} quarters")

if dimes > 0:
    if dimes == 1:
        print(f"{dimes} dime")
    else:
        print(f"{dimes} dimes")

if nickels > 0:
    if nickels == 1:
        print(f"{nickels} nickel")
    else:
        print(f"{nickels} nickels")

if pennies > 0:
    if pennies == 1:
        print(f"{pennies} penny")
    else:
        print(f"{pennies} pennies")
