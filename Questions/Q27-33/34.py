"""Q34. A student will not be allowed to sit in exam if his/her attendance is less than 75%.

a. Take following input from user

1. Number of classes held

ii. Number of classes attended.

b. Print percentage of class attended

c. Print Is student is allowed to sit in exam or not."""

num_class = int(input("Enter number of class held: "));
num_class_attended = int(input("Number of classes attended: "))
clas_per = (num_class_attended/num_class)*100;

if clas_per>75:
    print("You can attend the exam")
else:
    print("You can not attend the exam")