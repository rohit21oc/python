a = [12,56,30,60,90,85]
b = a
c = a.copy()

print(a)
print(id(a))
print(b)
print(id(b))
print(c)
print(id(c))

a[2] = 0
print("a: ",a)
print("b: ",b)
print("c: ",c)