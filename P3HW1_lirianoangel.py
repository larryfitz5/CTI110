# P3HW1_LirianoAngel
# Angel Liriano
# Date: 10-19-24
# This program takes the grades for six modules, calculates the average, and displays the corresponding letter grade for the average.

# Getting input for six grades (ensure they are floats)
mod_1 = float(input('Enter grade for Module 1: '))
mod_2 = float(input('Enter grade for Module 2: '))
mod_3 = float(input('Enter grade for Module 3: '))
mod_4 = float(input('Enter grade for Module 4: '))
mod_5 = float(input('Enter grade for Module 5: '))
mod_6 = float(input('Enter grade for Module 6: '))

# Add the grades to a list
grades = [mod_1, mod_2, mod_3, mod_4, mod_5, mod_6]

# Calculate the lowest, highest, sum, and average of the grades
lowest_grade = min(grades)
highest_grade = max(grades)
total = sum(grades)
average = total / len(grades)

# Determine the letter grade based on the average
if average >= 90:
    letter_grade = 'A'
elif average >= 80:
    letter_grade = 'B'
elif average >= 70:
    letter_grade = 'C'
elif average >= 60:
    letter_grade = 'D'
else:
    letter_grade = 'F'

# Displaying results
print("\n------------Results------------")
print(f"Lowest Grade:      {lowest_grade:.1f}")
print(f"Highest Grade:     {highest_grade:.1f}")
print(f"Sum of Grades:     {total:.1f}")
print(f"Average Grade:     {average:.2f}")
print(f"Letter Grade:      {letter_grade}")
print("--------------------------------")
