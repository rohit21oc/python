import os
if os.path.exists("hello.txt"):
    os.rename("hello.txt", "greet.txt")
    print("File renamed successfully.")
else:
    print("The file does not exist.")
