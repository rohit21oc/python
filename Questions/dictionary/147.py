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

for name,marks in student_marks.items():
    # total = sum(marks)
    total = 0
    for mark in marks:
        total+=mark
    percentage = total/500*100
    print(f"{name} has scored {total} marks, Percentage = {percentage}")
