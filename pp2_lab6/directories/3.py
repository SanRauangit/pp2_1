import os
def exists(p):
    if os.path.exists(p):
        print(f"Path exists")
        print(f"Directory: {os.path.dirname(p)}")
        print(f"Filename: {os.path.basename(p)}")
    else:
        print("Path does not exists")
p=input("Enter path: ")
exists(p)