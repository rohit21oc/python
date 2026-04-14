a = [12,5,689,5,24,56,12];
pos = a.index(24)
print(pos)
a.sort()
print(a)
a.reverse()
print(a)

# a.append([1,256,85,69])
# print(a)
a.extend([1,256,85,69])
print(a)

count = a.count(5)
print(count)