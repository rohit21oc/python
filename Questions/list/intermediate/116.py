my_list = [15,256,899,25,885,2,2,55885254,10256,65,6,1251,565,5,15,654,856654]

largest = float("inf")
second_largest = float("inf")

for num in my_list:
    if num>largest:
        second_largest = largest
        largest = num
    elif num> second_largest or num<largest:
        second_largest = num
print(f"Second largest number is: {second_largest}")
print(f"largest number is: {largest}")
