a = [10,25,36,28,90]
b = []
num = int(input("Enter a number: "))
# for i in range(0,len(a)):
#     if a[i]%num !=0:
#         b.append(a[i])
# print(b)

for i in a[:]:
    if i%num==0:
        a.remove(i)
print(a)