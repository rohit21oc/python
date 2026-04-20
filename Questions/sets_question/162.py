set1 = {15,25,689,58,63,"Python"}
set2 = {15,55,209,580,613,"Java"}

result = set1.intersection(set2)
print(result)
if len(result)==0:
    print("Both sets nothing have common")
else:
    print("Sets have something common Here the result: ")
    print(result)

    