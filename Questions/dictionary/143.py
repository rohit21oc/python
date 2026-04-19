list1 = ["Good","India","Bihar","Math"]
list2 = ["Bad","Delhi","Patna","95"]
result = {}

for i in range(0,len(list1)):
    result.update(zip(list1,list2))
print(result)