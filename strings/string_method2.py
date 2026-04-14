word = "hello/this/is/a/python"
a = word.split("/")
print(a)

my_list = ["hello", "world","where","are","you",58]
str = " | ".join(str(i) for i in my_list)
print(str)
print(type(str))

text = "I am Rohit"

result = " ".join(text.split()[::-1])
print(text)

text1 = "wr efv    sfv f     fv"

clean = " ".join(text1.split())
print(clean)