str = "grdhtdESRHT"
lowerAlpha = 0
upperAlpha = 0

for i in str:
    if i.isupper():
        upperAlpha +=1;
    elif i.islower():
        lowerAlpha +=1
print(upperAlpha)
print(lowerAlpha)