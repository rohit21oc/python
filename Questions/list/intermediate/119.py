my_list = [116,65,652,84,681,"Rohit"]

first = my_list[0]
last = my_list[-1]

for i in range(len(my_list)):
    if i == 0:
        my_list[i] = last
    elif i == len(my_list)-1:
        my_list[i] = first
print(my_list)