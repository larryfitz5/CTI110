# Anngel Liriano
# Date 11-17-2024
# P5LAB1_lirianoangel
# This program simulates a self-checkout machine that calculates the total amount owed and disperses the correct change in dollars, quarters, dimes, nickels, and pennies.

import random

# Function to calculate and display the change
def disperse_change(change):
    # Convert change to cents for easier calculation
    change_in_cents = round(change * 100)

    # Calculate number of dollars, quarters, dimes, nickels, and pennies
    dollars = change_in_cents // 100
    change_in_cents %= 100

    quarters = change_in_cents // 25
    change_in_cents %= 25

    dimes = change_in_cents // 10
    change_in_cents %= 10

    nickels = change_in_cents // 5
    change_in_cents %= 5

    pennies = change_in_cents

    # Display the change breakdown
    print("Change breakdown:")
    print(f"Dollars: {dollars}")
    print(f"Quarters: {quarters}")
    print(f"Dimes: {dimes}")
    print(f"Nickels: {nickels}")
    print(f"Pennies: {pennies}")

# Main function
def main():
    # Generate a random total amount owed (0.01 to 100.00)
    total_owed = round(random.uniform(0.01, 100.00), 2)
    print(f"Total owed: ${total_owed}")

    # Prompt user to enter the amount of cash given
    cash_given = float(input("Enter the amount of cash you are paying: $"))

    # Calculate the change owed
    change_owed = round(cash_given - total_owed, 2)

    # Check if the cash given is less than the total owed
    if change_owed < 0:
        print("Insufficient funds. Please provide enough money to cover the total.")
    elif change_owed == 0:
        print("Exact amount provided. No change owed.")
    else:
        # Display the amount of change owed
        print(f"Change owed: ${change_owed}")
        # Call the disperse_change function
        disperse_change(change_owed)

# Call the main function
if __name__ == "__main__":
    main()
