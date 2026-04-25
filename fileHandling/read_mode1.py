with open("text.txt", "r") as f:
    # print(f.read())
    x = f.read()

# print(f.read()) #error because the file is already read and the cursor is at the end of the file
count = 0
for ch in x:
    count += 1
    print(ch)

print("Total characters in the file: ", count)