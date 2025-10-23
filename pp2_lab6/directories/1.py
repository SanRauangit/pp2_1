import os
def directories_files(path):
    if os.path.exists(path):
        print("Directories: ")
        for b in os.listdir(path):
            if os.path.isdir(os.path.join(path,b)):
                print(b)
        
        print("\n Files and directories: ")
        print(os.listdir(path))

        print("\n Files:")
        for a in os.listdir(path):
            if os.path.isfile(os.path.join(path,a)):
                print(a)
p=input("Enter path: ").strip()
if not p:
    p="."
directories_files(p)