def div3_4(n):
    for i in range(1,n+1):
        if i%3==0 and i%4==0:
            yield i
n=int(input()) 
for n in div3_4(n):
    print(n)