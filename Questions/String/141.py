text = "helloWorldHowAreYou"
res =""
for ch in text:
    if ch.isupper():
        res+="_"+ch.lower()
    else:
        res+=ch
print(res)