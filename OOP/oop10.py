class Employee:
    company = "ABC Pvt Ltd"

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display(self):
        print("Name:", self.name)
        print("Salary:", self.salary)
        print("Company:", Employee.company)

    @classmethod
    def change_company(cls, new_company):
        cls.company = new_company


e1 = Employee("Rahul", 30000)
e2 = Employee("Aman", 40000)

print("Before changing company:")

e1.display()
e2.display()

Employee.change_company("XYZ Pvt Ltd")

print("\nAfter changing company:")

e1.display()
e2.display()