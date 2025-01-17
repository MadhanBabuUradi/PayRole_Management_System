from Employee_Management01 import add_employee, delete_employee, view_employees
from Salary_Calculation02 import calculate_salary


def main_menu():
    while True:
        print("\nPayroll Management System")
        print("1. Add Employee")
        print("2. View Employees")
        print("3. Delete Employee")
        print("4. Calculate Salary")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        if choice == '1':
            add_employee()
        elif choice == '2':
            view_employees()
        elif choice == '3':
            delete_employee()
        elif choice == '4':
            calculate_salary()
        elif choice == '5':
            print("Exiting Payroll Management System.")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main_menu()
