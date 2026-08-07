student = {
    "Rahul": 75,
    "Aman": 45,
    "Priya": 82,
    "Sneha": 58,
    "Vikas": 60
}
for student_name, marks in student.items():
    if marks >= 60:
        print(student_name)