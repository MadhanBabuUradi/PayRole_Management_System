import csv
from Employee_Management01 import EMPLOYEE_FILE


def calculate_salary():
    try:
        with open(EMPLOYEE_FILE, mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                emp_id = row[0]
                name = row[1]
                salary = float(row[3])
                days_worked = int(input(f"Enter days worked for {name} (ID: {emp_id}): "))
                tax = 0.1 * salary  # 10% tax deduction
                net_salary = (salary / 30) * days_worked - tax
                print(f"Net Salary for {name} (ID: {emp_id}): ${net_salary:.2f}")
    except FileNotFoundError:
        print("No employee records found.")
