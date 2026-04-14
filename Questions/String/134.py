# str = input("ENter a string: ")
# result = ""
# print(id(result))
# result = result+"ABC"
# print(result)
# print(id(result))
# res = str.upper()
# print(res)

chars = "abc35165AGVY"
result1 =""
for ch in chars:
    ascii = ord(ch)
    if ascii>=97 and ascii <= 122:
        new_ascii = ascii-32
        char = chr(new_ascii)
        result1 += char
    else:
        result1 +=ch
print(result1)