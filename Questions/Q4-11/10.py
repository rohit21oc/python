hindi = int(input("enter hindi subject's marks: "))
english = int(input("enter english subject's marks: "))
math = int(input("enter Math subject's marks: "))
science = int(input("enter Science subject's marks: "))
social_Science = int(input("enter Social Science subject's marks: "))

total_marks = hindi+english+math+science+social_Science
percentage = total_marks/5;
print(f"Total marks of your all subject is {total_marks}")
print(f"Total percentage of your marks is {percentage}")