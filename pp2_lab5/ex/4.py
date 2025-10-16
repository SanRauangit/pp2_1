import re
def upper_lower(text):
    pattern = r'[A-Z][a-z]+'
    return bool(re.findall(pattern,text))
r=open("c.txt","r")
file=r.read()
content=file.strip()
string=content.split()
for s in string:
    if s:
        result=upper_lower(s)
        print(s,result)