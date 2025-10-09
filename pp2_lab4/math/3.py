import math
def polygon(n,length):
    return (n*length**2)/(4*math.tan(math.pi/n))
n=int(input("Number of sides: "))
s=int(input("Length: "))
area=polygon(n,s)
print(f"{area:.2f}")