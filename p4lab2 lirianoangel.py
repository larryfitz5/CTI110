# Angel Liriano
# P4LAB2_LirianoAngel.py
# 2024-11-14
# Description: This program prompts the user to enter an integer, then displays its multiplication
#              table from 1 to 12. It will handle invalid inputs and offer the user a choice
#              to run the program again or exit.

def display_multiplication_table(number):
    # Using a for loop to display multiplication table from 1 to 12
    for i in range(1, 13):
        print(f"{number} x {i} = {number * i}")

def main():
    while True:  # This is the while loop that allows the program to run multiple times
        try:
            # Asking user to enter an integer
            user_input = int(input("Please enter an integer: "))
            
            if user_input >= 0:
                # Display multiplication table if input is zero or higher
                print(f"Multiplication table for {user_input}:")
                display_multiplication_table(user_input)
            elif user_input < 0:
                # Handling negative integer input case
                print("Error: Cannot accept negative values.")
            
            # Ask if the user wants to run the program again
            run_again = input("Would you like to run the program again? (yes/no): ").strip().lower()
            if run_again != "yes":
                print("Exiting program.")
                break  # Exit the loop if user doesn't want to run again
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

# Call the main function to start the program
main()
