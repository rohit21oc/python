my_Sets = {1,2,5,6,8,3,45}

# print(my_Sets)
my_Sets.remove(45)
my_Sets.add(100)
my_Sets.add(200)

print(my_Sets)
found = False;
num = int(input("Enter a number: "))
for i in my_Sets:
    if i==num:
        found = True

if found:
    print("Yes")
else:
    print("No")