def evenNumber():
    for i in range(1,11):
        if i%2==0:
            print(i,end=" ")

evenNumber()

def add():
    num1 = int(input("Enter Num1: "))
    num2 = int(input("Enter Num2: "))
    print(f"{num1}+{num2} = {num1+num2}")
add()

def sub():
     num1 = int(input("Enter Num1: "))
     num2 = int(input("Enter Num2: "))
     print(f"{num1}-{num2} = {num1-num2}")
sub()

def add1(a,b):
    print(a+b)

x = int(input("Enter first num: "))
y = int(input("Enter second num: "))
add1(x,y)

