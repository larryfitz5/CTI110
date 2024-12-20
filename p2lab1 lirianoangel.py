# Your Name: Angel Liriano
# Date: 10-6-2024
# Assignment Name: P2LAB1_LirianoAngel
# A brief description: This program calculates and displays the diameter, circumference, and area of a circle 
#                      based on a user-provided radius. It formats the results as specified in the instructions.

import math  # Import math module to use the constant pi

# Collect the radius input from the user (as a float)
radius = float(input("Enter the radius of the circle: "))

# Perform calculations
diameter = 2 * radius  # Formula for diameter
circumference = 2 * math.pi * radius  # Formula for circumference
area = math.pi * radius ** 2  # Formula for area

# Display the results, formatted as specified
print("Diameter: {:.1f}".format(diameter))  # Diameter formatted to 1 decimal place
print("Circumference: {:.2f}".format(circumference))  # Circumference formatted to 2 decimal places
print("Area: {:.3f}".format(area))  # Area formatted to 3 decimal places
