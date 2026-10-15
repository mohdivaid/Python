# Problem 1: Student Grade Analytics & Deduplication System 

class Student:
    def __init__(self, roll_no, name, marks):
        self.roll_no = roll_no
        self.name = name
        self.marks = marks  

class ClassRoom:
    def __init__(self):
        self.students_list = []  

    def get_unique_subjects(self):
        all_subjects = []
        for student in self.students_list:
            for subject in student.marks.keys():

                if subject not in all_subjects:
                    all_subjects.append(subject)
        return all_subjects

    def get_top_performers(self):
        subjects = self.get_unique_subjects()
        top_list = []

        for subject in subjects:
            top_student_name = ""
            highest_marks = 0

            for student in self.students_list:

                if subject in student.marks:
                    if student.marks[subject] > highest_marks:
                        highest_marks = student.marks[subject]
                        top_student_name = student.name


            top_list.append((subject, top_student_name, highest_marks))

        return top_list


    def remove_duplicates(self):
        unique_students = []
        seen_rolls = []

        for student in self.students_list:
            if student.roll_no not in seen_rolls:
                seen_rolls.append(student.roll_no)
                unique_students.append(student)

        self.students_list = unique_students


# =================      TESTING      =================

classroom = ClassRoom()

s1 = Student(101, "Rahul", {"Math": 95, "Science": 80})
s2 = Student(102, "Priya", {"Math": 90, "Science": 98})
s3 = Student(101, "Rahul Duplicate", {"Math": 40}) 

classroom.students_list = [s1, s2, s3]

classroom.remove_duplicates()
print("Clean Student Names:")
for s in classroom.students_list:
    print(s.name)

print("\nUnique Subjects:", classroom.get_unique_subjects())

print("\nTop Performers:", classroom.get_top_performers())