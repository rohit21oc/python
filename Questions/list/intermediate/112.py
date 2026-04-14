my_list = []

result = []

for i in range(5):
    value = int(input("Enter number: "))
    my_list.append(value)
print(my_list)
for i in range(len(my_list)-1,-1,-1):
    result.append(my_list[i])
print(result)