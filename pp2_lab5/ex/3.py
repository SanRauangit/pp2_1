import re
def low_und(text):
    pattern = r'[a-z]*+_[a-z]*$'
    return bool(re.match(pattern,text))
r=open("c.txt","r")
file=r.read()
content=file.strip()
string=content.split()
for s in string:
    if s:
        result=low_und(s)
        print(s,result)