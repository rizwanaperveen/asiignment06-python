#14. Aggregation
#Assignment:
#Create a class Department and a class Employee. Use aggregation by having a Department object store a reference to an Employee object that exists independently of it

        # Define the Employee class
class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def get_details(self):
        return f"Employee Name: {self.name},  Position: {self.position}"

# Define the Department class using aggregation
class Department:
    def __init__(self, name):
        self.name = name
        self.employees = []  # List to store Employee objects

    def add_employee(self, employee):
        self.employees.append(employee)  # Adding existing Employee object

    def show_employees(self):
        print(f"Department: {self.name}")
        for emp in self.employees:
            print(emp.get_details())

# Example usage
emp1 = Employee("Ali","Manager")
emp2 = Employee("Ibrahim", "Clerk")

dept = Department("Human Resources")
dept.add_employee(emp1)
dept.add_employee(emp2)

dept.show_employees()


#02
class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def display_employee(self):
        print(f"Employee: {self.name}, Position: {self.position}")

class Department:
    def __init__(self, department_name):
        self.department_name = department_name
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def display_department(self):
        print(f"Department: {self.department_name}")
        for employee in self.employees:
            employee.display_employee()

emp1 = Employee("Saira", "Manager")
emp2 = Employee("NAsir", "Developer")

department = Department("IT")
department.add_employee(emp1)
department.add_employee(emp2)

department.display_department()