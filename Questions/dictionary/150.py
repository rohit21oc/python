d1 = {'a':400,'b':200,'c':300}
d2 = {'a':150,'b':200,'d':300}

result ={}

for k,v in d1.items():
    result[k] = v

for k,v in d2.items():
    if k in result:
        result[k] = result[k]+v
    else:
        result[k] = v
print(result)