def is_palindrome(word):
    if word[:]==word[::-1]:
        return True
    else:
        return False
    
word=input()
print(is_palindrome(word))