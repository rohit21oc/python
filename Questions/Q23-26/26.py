class_held = int(input("Enter how many classes are held: "))
class_attended = int(input("Enter how many classes are attended: "))

class_per = (class_attended/class_held)*100;

print(f"class attended percentage is {class_per}")

if(class_per>=75):
    print("You can sit in the exam")
else:
    print("No,you are not allowed to attend the exam")