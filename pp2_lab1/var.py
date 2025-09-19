x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

x = 4       # x is of type int
x = "Sally" # x is now of type str
print(x)

a = 4
A = "Sally"
#A will not overwrite a

# Legal variable names:

myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

# Illegal variable names:

# 2myvar = "John"
# my-var = "John"
# my var = "John"

x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

x = y = z = "Orange"
print(x)
print(y)
print(z)

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

# x = "Python"
# y = "is"
# z = "awesome"
# print(x, y, z)  output is "Python is awesome"