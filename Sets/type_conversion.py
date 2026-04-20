list1 = [1,2,5,6,3,8,9,85]

print(list1)

b = set(list1)
print(type(b))

c = list(b)
print(c)

my_Set1 = {45,25,69,3,56,85,21}
my_Set2 = {45,52,69,56,12,53,28}

print(my_Set1.union(my_Set2))
print(my_Set1.intersection(my_Set2))

my_list = [1,5,6,2,8,9]
my_list3 = [1,45,6,22,18,9]

a1 = set(my_list)
b1= set(my_list3)

res = list(a1.intersection(b1))
print(res)