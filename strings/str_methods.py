str = "Rohit kumar is a %software engineer"

# x = str.title() #Rohit Kumar Is A %Software Engineer
# x = str.capitalize() #Rohit kumar is a %software engineer
x = str.lower()
# x = str.upper()
print(x)

"""isupper, islower, isalpha,isalnum,isspace"""
b = ""
# r = b.isupper()
# r = b.isalpha()
# r = b.isalnum()
r = b.isspace()
print(r)


word = "5454"
if word.isdigit():
    digit = int(word)
    print(digit,type(digit))
else:
    print("can't convert into digit")
