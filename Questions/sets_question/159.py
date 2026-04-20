list1 = [1,25,63,89,56,55,85]
list2 = [12,25,613,79,86,55,85]
list3 = [1,25,63,89,56,55,45]

set1 = set(list1)
set2 = set(list2)
set3 = set(list3)
print(set1 & set2 & set3)
print(set1 | set2 | set3)
x = set1.intersection(set2)
result = x.intersection(set3)
print(result)


u = set1.union(set2)
uniunRes = u.union(set3)
print(uniunRes)