
# Your Name: Angel Liriano
# Date: 10-6-2024
# Assignment Name: P1HW1_LirianoAngel
# A brief description: This program collects input from the user for base and exponent to calculate and display the result.
#                      It also takes three numbers, adds the first two, and subtracts the third from the sum.

# Collect input from the user for base and exponent
base = int(input("Enter an integer for the base: "))  # Collect base
exponent = int(input("Enter an integer for the exponent: "))  # Collect exponent

# Calculate the result of base raised to the power of exponent
result = base ** exponent

# Display the base, exponent, and result using .format() method
print("{} raised to the power of {} is {}!".format(base, exponent, result))

# Collect input for three separate integers
num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))
num3 = int(input("Enter the third integer: "))

# Perform the addition and subtraction
sum_result = num1 + num2
final_result = sum_result - num3

# Display the result of the operations using .format()
print("{} plus {} is {}".format(num1, num2, sum_result))
print("{} minus {} is {}".format(sum_result, num3, final_result))
