class Person:
    def __init__(self, name, city):
        self.name = name
        self.city = city

    def display(self):
        print(self.name, "Lives in", self.city)

p1 = Person("Rahul", "Indore")
p2 = Person("Aman", "Bhopal")

p1.display()
p2.display()