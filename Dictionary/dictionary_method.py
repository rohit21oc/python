student = {
    "name":"Rohit",
    "age":22,
    "roll no":5043,
    "course":"B.tech",
    1:3,
    321:[12,35,6],
    "address":{"HN":278,"Gali no":27,"city":"New Ashok Nagar"}
}
# del student
student["city"] = "Delhi"
student.update({"subject":"AI","sub_code":"AI5658"})
print(student)
res = student.get("nameee")
print(res)
print(student["name"])

# k = input("Enter key: ")
# result = student.get(k)
# if result is not None:
#     print(result)
# else:
#     print("Key does not exists")
student.pop("age")

del student["city"]
print(student)

