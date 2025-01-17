import csv

EMPLOYEE_FILE = "employees.csv"

def add_employee():
    with open(EMPLOYEE_FILE, mode='a', newline='') as file:
        writer = csv.writer(file)
        emp_id = input("Enter Employee ID: ")
        name = input("Enter Employee Name: ")
        position = input("Enter Position: ")
        salary = float(input("Enter Monthly Salary: "))
        writer.writerow([emp_id, name, position, salary])
        print("Employee added successfully!")

def view_employees():
    try:
        with open(EMPLOYEE_FILE, mode='r') as file:
            reader = csv.reader(file)
            print("\nEmployee Records:")
            for row in reader:
                print(f"ID: {row[0]}, Name: {row[1]}, Position: {row[2]}, Salary: {row[3]}")
    except FileNotFoundError:
        print("No employee records found.")

def delete_employee():
    emp_id = input("Enter Employee ID to delete: ")
    updated_data = []
    found = False
    try:
        with open(EMPLOYEE_FILE, mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] != emp_id:
                    updated_data.append(row)
                else:
                    found = True
        with open(EMPLOYEE_FILE, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(updated_data)
        if found:
            print("Employee deleted successfully!")
        else:
            print("Employee not found.")
    except FileNotFoundError:
        print("No employee records found.")
