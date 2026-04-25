import shutil
import os

if os.path.exists("folder 2"):
    shutil.rmtree("folder 2")
    print("Folder removed successfully.")
else:
    print("The folder does not exist.")