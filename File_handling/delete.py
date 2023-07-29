import os
if os.path.exists("myfile.txt"):
    os.remove("myfile.txt")
    print("File deleted successfully")
else:
     print("The file does not exist")
