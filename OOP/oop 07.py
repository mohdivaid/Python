class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def result(self):
        if self.marks >= 40:
            print(self.name, "Pass")
        else:
            print(self.name, "Fail")

s1 = Student("Rahul", 80)
s2 = Student("Aman", 35)

s1.result()
s2.result()