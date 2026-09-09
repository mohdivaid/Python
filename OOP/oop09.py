class Employee:
    company = "ABC Pvt Ltd"

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display(self):
        print("Name:", self.name)
        print("Salary:", self.salary)
        print("Company:", Employee.company)

e1 = Employee("Rahul", 30000)

e1.display()