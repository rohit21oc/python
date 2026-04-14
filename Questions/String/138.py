text = "python is good programming language"

res = text.split(" ")
print(res)
reverse = " ".join(res[::-1])
print(reverse)

rev = " ".join(text.split(" ")[::-1])
print(rev)