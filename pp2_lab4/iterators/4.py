def square_gen(a,b):
    for i in range(a,b+1):
        yield i**2
a=int(input())
b=int(input())
for n in square_gen(a,b):
    print(n)