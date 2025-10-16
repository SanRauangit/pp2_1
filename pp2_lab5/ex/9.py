import re
def insert_space(text):
    pattern=r'(?<!^)(?=[A-Z])'
    return re.sub(pattern,' ',text)
r=open("c.txt","r")
file=r.read()
content=file.strip()
string=content.split()
for s in string:
    if s:
        result=insert_space(s)
        print(s,result)