a = [15,1,256,58,4,5,"Code karo","Rohit",15,5,68,"Rohit",1]
result = []

for num in a:
    if num not in result:
        result.append(num)
print(result)