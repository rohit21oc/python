import os 
if os.path.exists("text.txt"):
    os.remove("text.txt")
    print("File removed successfully.") 
else:
    print("The file does not exist.")