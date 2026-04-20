def largestNum(num1,num2,num3):
    if num1>num2 & num1>num3:
        print("num1")
        print(f"{num1} is largest number")
    elif num2>num1 & num2>num3:
        print("num2")
        print(f"{num2} is largest number")
    else:
        print("num3")
        print(f"{num3} is largest number")
largestNum(35,35,35)