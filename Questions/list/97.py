""" how many elements are divisible by 2 and 5"""

a = [16151,8565,10,56520,6650,660,6556,2596,65,50,65,650,25,23,20,65,60]
count = 0;

for i in range(0,len(a)):
    if a[i]%2==0 and a[i]%5 ==0:
        count+=1
        print(a[i])
print(f"{count} numbers are divisible by 2 and 5")        
