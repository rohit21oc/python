# my_list = [215,658,5,32,1,58,895,2,3559,62]
my_list = [-10,-5156,-1,-53]
largest = my_list[0]

# for i in range(0,len(my_list)):
#     if my_list[i]>largest:
#         largest = my_list[i];
# print(largest)

for i in my_list:
    if i>largest:
        largest = i;
print(largest)