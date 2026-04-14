"""Count how many even number in the given list"""

my_list = [15,165,4,565,2368,5,65,652,651,0];
count = 0;
for i in range(0,len(my_list)):
    if i%2==0:
        count = count+1
        
print("Total even number: ",count)