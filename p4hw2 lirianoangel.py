# Angel Liriano
# 2024-11-10
# P4HW2_LirianoAngel
# This program calculates weekly gross pay for multiple employees, including overtime pay if applicable,
# and displays a summary of all employees entered.

# Initialize totals
total_overtime_pay = 0
total_regular_pay = 0
total_gross_pay = 0
employee_count = 0

# Loop to process multiple employees
while True:
    # Get employee name
    employee_name = input("Enter employee's name or 'Done' to terminate: ")

    # Check for sentinel value to terminate
    if employee_name.lower() == "done":
        break

    # Get hours worked and pay rate
    hours_worked = float(input(f"How many hours did {employee_name} work? "))
    pay_rate = float(input(f"What is {employee_name}'s pay rate? "))

    # Calculate overtime hours and pay
    overtime_hours = 0
    overtime_pay = 0

    if hours_worked > 40:
        overtime_hours = hours_worked - 40
        overtime_pay = overtime_hours * (pay_rate * 1.5)

    # Calculate regular pay and gross pay
    regular_hours = min(hours_worked, 40)
    regular_pay = regular_hours * pay_rate
    gross_pay = regular_pay + overtime_pay

    # Update totals
    total_overtime_pay += overtime_pay
    total_regular_pay += regular_pay
    total_gross_pay += gross_pay
    employee_count += 1

    # Display the individual employee's pay summary with formatted output
    print("\nEmployee name:   ", employee_name)
    print("Hours Worked    Pay Rate    OverTime    OverTime Pay    RegHour Pay    Gross Pay")
    print("--------------------------------------------------------------------------------")
    print(f"{hours_worked:<15.1f}{pay_rate:<12.2f}{overtime_hours:<12.1f}"
          f"{overtime_pay:<15.2f}${regular_pay:<13.2f}${gross_pay:.2f}\n")

# Display totals for all employees
print("\nTotal number of employees entered:", employee_count)
print(f"Total amount paid for overtime: ${total_overtime_pay:.2f}")
print(f"Total amount paid for regular hours: ${total_regular_pay:.2f}")
print(f"Total amount paid in gross: ${total_gross_pay:.2f}")
