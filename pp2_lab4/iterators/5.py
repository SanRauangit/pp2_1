def reverse(n):
    for i in range(n,-1,-1):
        yield i
n=int(input())
for n in reverse(n):
    print(n)