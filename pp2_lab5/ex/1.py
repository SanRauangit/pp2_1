import re
def match_pattern(text):
    pattern= r'ab*'
    return bool(re.search(pattern,text))
r=open("b.txt","r")
file=r.read()
content=file.strip()
string=content.split()
for s in string:
    if s:
        result=match_pattern(s)
        print(s,result)