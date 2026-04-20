str = input("Enter a string: ")
new_str = ""
for i in str:
    if i not in new_str:
        new_str +=i
    else:
        continue;
print(new_str)

name = "stringgggsssjjaarr"

result = set(name)
print(result)

str_res = "".join(result)
print(str_res)
