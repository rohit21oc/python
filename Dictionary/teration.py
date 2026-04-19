my_dict = {
    "name":"Rohit",
    "age":22,
    "city":"Delhi"
}

print(my_dict.keys())

for key in my_dict.keys():
    print(my_dict[key])

marks ={
    "math":89,
    "physics":90,
    "bio":75,
    "hindi":88,
    "ENG":99
}
print(marks)
total_marks=0
for k in marks.values():
    total_marks+=k
print(total_marks)

for k,v in my_dict.items():
    print(f"{k} -> {v}")