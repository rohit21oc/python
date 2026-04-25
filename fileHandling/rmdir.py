import os
if os.path.exists("folder 1"):
    os.rmdir("folder 1")
    print("Folder removed successfully.")
else:
    print("The folder does not exist.")