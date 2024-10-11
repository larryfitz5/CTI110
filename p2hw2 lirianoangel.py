# Title block
# Angel Liriano
# 10-11-24
# P2HW2_LirianoAngel
# This program accepts grades for six modules, stores them in a list, and displays the lowest, highest, sum, and average of the grades.

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
