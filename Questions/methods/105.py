my_list = [15,20,36,51,15,24,15,85,15]
old = int(input("Enter old: "))
new = int(input("Enter new: "))

for i in range(0,len(my_list)):
    if my_list[i]==old:
        my_list[i]=new;
print(my_list)

