marks = {}
subject_count = int(input("How many Subjects: "))

for _ in range(0,subject_count):
    subject_name = input("Enter Subject name: ")
    subject_marks = int(input(f"ENter {subject_name} marks: "))
    marks[subject_name] = subject_marks
print(marks)