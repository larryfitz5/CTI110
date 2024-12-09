# Angel Liriano
# 10-24-2024
# P5HW_LirianoAngel
# Brief description of program: A menu-driven math quiz program that provides addition and subtraction challenges to the user.
# The program generates random numbers, allows the user to guess the result, and provides feedback.

import random

def addition_quiz():
    """Generate two random numbers for addition and handle user guesses."""
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    correct_answer = num1 + num2

    print(f"\n  {num1}")
    print(f"+ {num2}")

    guesses = 0
    while True:
        try:
            user_guess = int(input("Enter your answer: "))
            guesses += 1
            if user_guess < correct_answer:
                print("Sorry, guess is too low.")
            elif user_guess > correct_answer:
                print("Sorry, guess is too high.")
            else:
                print(f"Congratulations!!!! Your answer is correct.")
                print(f"Number of guesses: {guesses}")
                break
        except ValueError:
            print("Invalid input. Please enter a number.")

def subtraction_quiz():
    """Generate two random numbers for subtraction and handle user guesses."""
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    # Ensure the subtraction result is non-negative
    if num1 < num2:
        num1, num2 = num2, num1
    correct_answer = num1 - num2

    print(f"\n  {num1}")
    print(f"- {num2}")

    guesses = 0
    while True:
        try:
            user_guess = int(input("Enter your answer: "))
            guesses += 1
            if user_guess < correct_answer:
                print("Sorry, guess is too low.")
            elif user_guess > correct_answer:
                print("Sorry, guess is too high.")
            else:
                print(f"Congratulations!!!! Your answer is correct.")
                print(f"Number of guesses: {guesses}")
                break
        except ValueError:
            print("Invalid input. Please enter a number.")

def display_menu():
    """Display the main menu."""
    print("\nMAIN MENU")
    print("-----------------")
    print("1. Adding Random Numbers")
    print("2. Subtracting Random Numbers")
    print("3. Exit")

def main():
    """Main function to drive the program."""
    while True:
        display_menu()
        try:
            choice = int(input("Please choose one of the menu options: "))
            if choice == 1:
                addition_quiz()
            elif choice == 2:
                subtraction_quiz()
            elif choice == 3:
                print("Thank you for playing...\nBye!!")
                break
            else:
                print("Invalid choice. Please choose 1, 2, or 3.")
        except ValueError:
            print("Invalid input. Please enter a number.")

# Run the main program
if __name__ == "__main__":
    main()
