length_list = int(input("Enter the length of list: "))
my_list = []
odd_list = []
even_list = []

for i in range(0,length_list):
    num = int(input(f"Enter element of at position {i}: "))
    my_list.append(num)
    if num%2==0:
        even_list.append(num)
    else:
        odd_list.append(num)

print("created_list = ",my_list)
print("odd_list = ",odd_list)
print("even_list = ",even_list)