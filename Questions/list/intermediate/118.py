lists = [2,36,5,6,9,1,245,68,17,37,59,71,86,31]

for num in lists:
    factor = 0
    for i in range(1,num+1):
        if num % i ==0:
            factor +=1
    if factor == 2:
            print(num)