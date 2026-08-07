student = {
    "Rahul": 75,
    "Aman": 45,
    "Priya": 82,
    "Sneha": 58,
    "Vikas": 60
}
highest_marks = 0
name = ""
for student_name, marks in student.items():
    if marks > highest_marks:
        highest_marks = marks
        name = student_name
print(name)