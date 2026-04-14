a = [15,1,256,58,4,5,"Code karo","Rohit",15,5,68,"Rohit",1]

value = int(input("Enter a number: "))

if value in a:
    index = a.index(value)
    print(f"index: {index}")
else:
    print(-1)

