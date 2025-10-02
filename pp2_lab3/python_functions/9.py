import math
def volume_sphere(radius):
    return (4/3)*math.pi*radius**3
radius=int(input())
print(volume_sphere(radius))