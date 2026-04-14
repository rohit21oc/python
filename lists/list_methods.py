my_list = [21561,654,54,5.85,"Rohit",-651]
"""Append will add the elemment in the end of the list"""
my_list.append("prem")
my_list.append(152) 

print(my_list)

"""insert will add the elemment in the given index of the list if give 3rd index the element will add on 3rd index and old 3rd index will shift on 4th index"""

my_list.insert(3,"Python")
print(my_list)

"""Update the element"""

my_list[-2] = 520;
print(my_list)

"""Remove element from list"""

a= [1,1,20,55,1,56,10,1,5]
a.pop()
a.pop(2)
print(a)
a.remove(1)
print(a)
b = [1,2,3,4,5]
del b[3]
print(b)
b.clear()
print(b)