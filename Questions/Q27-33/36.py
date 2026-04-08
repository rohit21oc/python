"Q36. Take three numbers as input from User and print which one is greater or are they equal"

num1 = int(input("Enter num1: "))
num2 = int(input("Enter num2: "))
num3 = int(input("Enter num3: "))

if(num1>num2 and num1>num3):
    print(f"{num1} is greatest number")
elif(num2>num1 and num2>num3):
    print(f"{num2} is greatest number")
else:
    print(f"{num3} is greatest number")