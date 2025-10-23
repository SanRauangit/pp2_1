import os
def check(p):
    if os.path.exists(p):
        print("Exists")
    else:
        return
    readable=os.access(p,os.R_OK)
    print(f"Readable: {readable}")
    writeable=os.access(p,os.W_OK)
    print(f"Writeable: {writeable}")
    executable=os.access(p,os.X_OK)
    print(f"Executable: {executable}")
p=input("Enter path: ").strip()
if not p:
    p="."
check(p)