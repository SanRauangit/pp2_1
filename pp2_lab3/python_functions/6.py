def reversed_words(sentence):
    words=sentence.split()
    reversed_words=words[::-1]
    return ' '.join(reversed_words)
user=input()
result=reversed_words(user)
print(result)