class Student:
    school = "ABC School"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("School:", Student.school)


s1 = Student("Rahul", 20)
s1.display()