class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
      
    def display(self):

      print("Name:",self.name, "\nSalary:",self.salary)

e1 = Employee("Siddharth", 50000)
e1.display()