list1 = [1,2,3,4,5]
list2 = [6,7,8,9]

result = []

for num in list1:
    result.append(num)
for num in list2:
    result.append(num)

print(result)
result = list1+list2;
print(result)