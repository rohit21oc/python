num = int(input("Enter number: "))

count = 0
# for i in range(1,num):
#     if i%7==0:
#         count = count+1
#     print(i)
# print(count)

for i in range(20,num):
    if i%7==0 and i%6==0:
        count = count+1
    # print(i)
print(count)


