student_marks = {
    "Rohit":    [78, 85, 90, 88, 76],
    "Amit":     [65, 70, 72, 68, 74],
    "Priya":    [88, 92, 95, 91, 89],
    "Neha":     [75, 80, 78, 82, 77],
    "Rahul":    [60, 66, 70, 64, 68],
    "Sneha":    [90, 93, 89, 94, 91],
    "Vikas":    [55, 60, 58, 62, 59],
    "Anjali":   [82, 86, 84, 88, 85],
    "Karan":    [70, 75, 72, 78, 74],
    "Pooja":    [85, 88, 90, 87, 89]
}
highest_marks = 0
highest_marks_student_name = ""

for name,marks in student_marks.items():
    total_marks = sum(marks)
    if total_marks>highest_marks:
        highest_marks = total_marks
        highest_marks_student_name = name
print(f"highest_marks_student_name: {highest_marks_student_name}")
print(f"highest_marks: {highest_marks}")