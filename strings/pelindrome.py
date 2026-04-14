my_string = input("Enter the string: ")

if my_string == my_string[::-1]:
    print("It's a pelindrome string")
else:
    print("It's not a pelindrome string")

check = my_string.endswith("g")
print(check)
