# Angel Liriano
# 2023-10-27
# P3HW2_Salary_LirianoAngel
# This program calculates an employee's weekly gross pay, including any overtime pay if applicable.

"""
Pseudocode:
1. Prompt the user to enter the employee's name.
2. Prompt the user to enter the number of hours worked by the employee.
3. Prompt the user to enter the employee's hourly pay rate.
4. If the hours worked are more than 40, calculate overtime hours and overtime pay.
   - Calculate overtime pay as 1.5 times the regular pay rate for hours over 40.
5. Calculate regular pay as the pay rate multiplied by hours worked (up to 40 hours).
6. Add regular pay and overtime pay to get the gross pay.
7. Display the employee's name, pay rate, hours worked, overtime hours, overtime pay, regular pay, and gross pay.
"""

# Gather input from the user
employee_name = input("Enter employee's name: ")
hours_worked = float(input("Enter number of hours worked this week: "))
pay_rate = float(input("Enter employee's pay rate: "))

# Determine if employee worked overtime
overtime_hours = 0
overtime_pay = 0

if hours_worked > 40:
    overtime_hours = hours_worked - 40
    overtime_pay = overtime_hours * (pay_rate * 1.5)

# Calculate regular pay and gross pay
regular_hours = min(hours_worked, 40)
regular_pay = regular_hours * pay_rate
gross_pay = regular_pay + overtime_pay

# Display the results
print("\n--- Employee Pay Summary ---")
print(f"Employee Name: {employee_name}")
print(f"Pay Rate: ${pay_rate:.2f}")
print(f"Hours Worked: {hours_worked}")
print(f"Overtime Hours: {overtime_hours}")
print(f"Overtime Pay: ${overtime_pay:.2f}")
print(f"Regular Pay: ${regular_pay:.2f}")
print(f"Gross Pay: ${gross_pay:.2f}")
