import re
def snake_camel(text):
    pattern=r'_([a-z])'
    return re.sub(pattern,lambda match : match.group(1).upper(),text)
r=open("c.txt","r")
file=r.read()
content=file.strip()
string=content.split()
for s in string:
    if s:
        result=snake_camel(s)
        print(s,result)