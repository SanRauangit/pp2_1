import re
def split_upper(text):
    pattern=r'(?<!^)(?=[A-Z])'
    return re.split(pattern,text)
r=open("c.txt","r")
file=r.read()
content=file.strip()
string=content.split()
for s in string:
    if s:
        result=split_upper(s)
        print(s,result)