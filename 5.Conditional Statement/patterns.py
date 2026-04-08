"""
* * * * * 
* * * * *
* * * * *
* * * * *
* * * * *
 """
for i in range(1,6):
    for j in range(1,6):
        print("*",end=" ")
    print()


"""
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5 
"""
print()

for i in range(1,6):
    for j in range(1,6):
        print(j,end=" ")
    print()

"""
5 4 3 2 1
5 4 3 2 1
5 4 3 2 1
5 4 3 2 1
5 4 3 2 1 """
for i in range(5,0,-1):
    for j in range(5,0,-1):
        print(j,end=" ")
    print()

"""
1 1 1 1 1
2 2 2 2 2
3 3 3 3 3
4 4 4 4 4
5 5 5 5 5"""
for i in range(1,6):
    for j in range(1,6):
        print(i, end=" ")
    print()