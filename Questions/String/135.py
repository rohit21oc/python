str = "RohitKumar"
res = ""
for ch in str:
    ascii = ord(ch)
    if ascii>=97 and ascii<=122:
        new_ascii = ascii-32
        char = chr(new_ascii)
        res +=char
    elif ascii>=65 and ascii<=90:
        new_ascii = ascii+32
        char = chr(new_ascii)
        res += char
    else:
        res +=ch
print(res)
