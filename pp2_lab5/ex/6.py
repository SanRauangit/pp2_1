import re
def replace(text):
    pattern=r'[ ,.]'
    return re.sub(pattern,':',text)
r=open("d.txt","r")
file=r.read()
result = replace(file)
print(result)