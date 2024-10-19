# Angel Liriano
# 10-11-24
# P2HW2_LirianoAngel
# This program accepts grades for six modules, stores them in a list, and displays the lowest, highest, sum, and average of the grades.

# Pseudocode:
# 1. Start
# 2. Display a prompt asking the user to enter six grades, one for each module.
# 3. Accept the six grades as input from the user, one at a time.
# 4. Convert each grade to a floating-point number and store them in a list.
# 5. Calculate the lowest grade by finding the minimum value in the list.
# 6. Calculate the highest grade by finding the maximum value in the list.
# 7. Calculate the sum of all the grades by adding up the values in the list.
# 8. Calculate the average grade by dividing the sum of the grades by the number of grades (6).
# 9. Display the following results:
#     - The lowest grade
#     - The highest grade
#     - The sum of the grades
#     - The average of the grades (formatted to two decimal places)
# 10. End

# Getting grades from the user
grades = [
    float(input("Enter grade for Module 1: ")),
    float(input("Enter grade for Module 2: ")),
    float(input("Enter grade for Module 3: ")),
    float(input("Enter grade for Module 4: ")),
    float(input("Enter grade for Module 5: ")),
    float(input("Enter grade for Module 6: "))
]

# Calculations
lowest_grade = min(grades)
highest_grade = max(grades)
sum_of_grades = sum(grades)
average_grade = sum_of_grades / len(grades)

# Displaying the results
print("\n------------Results------------")
print(f"Lowest Grade:      {lowest_grade:.1f}")
print(f"Highest Grade:     {highest_grade:.1f}")
print(f"Sum of Grades:     {sum_of_grades:.1f}")
print(f"Average:           {average_grade:.2f}")
print("--------------------------------")
