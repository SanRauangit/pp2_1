import os
def delete_file(file_path):
    if not os.path.exists(file_path):
        print("Path does not exists")
        return False
    if not os.access(file_path,os.W_OK):
        print("No write access")
        return False
    os.remove(file_path)
    print("Done")
p=input("Enter file to delete: ").strip()
delete_file(p)