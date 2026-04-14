my_list = [1,2,5,6,6,78,78,96]
my_list2 = [1,25,86,78,6]
result = []

for num in my_list:
    if num in my_list2:
        if num not in result:
            result.append(num)
print(result)