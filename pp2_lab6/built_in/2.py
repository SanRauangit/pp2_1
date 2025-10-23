def upper_lower(text):
    upper=0
    lower=0
    for i in text:
        if i.isupper():
            upper+=1
        elif i.islower():
            lower+=1
    return upper,lower
t="Hello,World"
r=upper_lower(t)
print(r)