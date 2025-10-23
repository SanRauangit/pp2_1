def is_palindrome(text):
    str=text.lower()
    reverse=str[::-1]
    if str==reverse:
        return True
    else:
        return False
s="abba"
r=is_palindrome(s)
print(r)