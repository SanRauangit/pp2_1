def square_generator(n):
    for i in range(1,n+1):
        if i*i<=n:    
            yield i**2

n=int(input())
squares=square_generator(n)
for square in squares:
    print(square)