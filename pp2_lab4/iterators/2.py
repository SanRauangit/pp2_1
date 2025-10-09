def even_generator(n):
    for i in range(0,n+1,2):
        yield i
n=int(input())
even=even_generator(n)
result=",".join(str(n) for n in even)
print(result)