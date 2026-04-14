str = input("Enter a string: ")
alphabets = 0;
digits = 0
spaces = 0
symbole = 0

for i in str:
    ascii = ord(i)
    if ascii>=65 and ascii <=90 or ascii >=97 and ascii<=122:
        alphabets+=1
    elif ascii == 40:
        spaces +=1
    elif ascii>=48 and ascii<=57:
        digits +=1
    elif ascii>=33 and ascii<=47:
        symbole+=1
print(alphabets)
print(digits)
print(spaces)
print(symbole)


# print(symbole)ev55256 efv  R #sdfv