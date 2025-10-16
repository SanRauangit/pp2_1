import re
def a_to_b(text):
    pattern=r'a.*b$'
    return bool(re.match(pattern,text))
r=open("b.txt","r")
file=r.read()
content=file.strip()
string=content.split()
for s in string:
    if s:
        result=a_to_b(s)
        print(s,result)