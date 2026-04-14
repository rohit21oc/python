old_list = [12, 32, 25, 33, 85, 96, 84, 561, 361]
new_list = []

# for i in range(0,len(old_list)):
#     if old_list[i]%2==0:
#         new_list.append(old_list[i])
# print(new_list)

# for i in old_list[:]:
#     if i%2 ==0:
#         old_list.remove(i)
# print(old_list)

for i in range(len(old_list) - 1, -1, -1):
    if old_list[i] % 2 == 0:
        old_list.pop(i)
print(old_list)
# for i in range(len(old_list) - 1, -1, -1):
#     print(old_list[i],end=" ")
