import math
func=int(input("Choose function to work with \n 1.Grams to ounces \n 2.Farenheit to celsium \n 3.Volume of sphere \n"))
if(func==1):
    def grams_to_ounces(grams):
        ounces=grams*28.3495231
        return ounces
    n=int(input())
    print(grams_to_ounces(n))        
elif(func==2):
    def farenheit_to_celsius(farenheit):
        celsuis=(5/9)*(farenheit-32)
        return celsuis
    f=int(input())
    c=farenheit_to_celsius(f)
    print(f"{f}F={c:.2f}C" )
elif(func==3):
    def volume_sphere(radius):
        return (4/3)*math.pi*radius**3
    radius=int(input())
    print(volume_sphere(radius))