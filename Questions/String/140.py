text = "python is good"

words = text.split()
print(words)

rev = " ".join(i[::-1] for i in words)
print(rev)