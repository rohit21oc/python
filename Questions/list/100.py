a = [16151,8565,10,56520,6650,660,6556,2596,65,50,65,650,25,23,20,65,60]
sum =0
for i in range(0,len(a)):
    if a[i]%3 ==0 and a[i]%4==0:
        # print(a[i])
        sum+=a[i]
        print(a[i])
print(sum)         