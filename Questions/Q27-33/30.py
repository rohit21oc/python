number = int(input("ENter a number: "))

last_digit = number%10
print(last_digit);
print(f"The last digit of {number} is {last_digit}");

if(last_digit/5):
    print(f"last digit of {number} is divisible by 5")
else:
    print("Not divisible")