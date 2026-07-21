marks = {
    "Math": 90,
    "English": 85,
    "Science": 95
}
sum_marks = sum(marks.values())
print("Total Marks:", sum_marks)

total_subjects = len(marks)
print("Total Subjects:", total_subjects)

average_marks = sum_marks / total_subjects
print("Average Marks:", average_marks)