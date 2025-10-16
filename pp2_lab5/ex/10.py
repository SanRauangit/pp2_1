import re
def camel_snake(text):
    pattern=r'(?<!^)(?=[A-Z])'
    return re.sub(pattern,'_',text).lower()
r=open("c.txt","r")
file=r.read()
content=file.strip()
string=content.split()
for s in string:
    result=camel_snake(s)
    print(s,result)