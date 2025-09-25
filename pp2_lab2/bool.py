# Comparison
print(10 > 9)
print(10 == 9)
print(10 < 9)

# Answer based on condition
a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

#  Evaluate Values and Variables
print(bool("Hello"))
print(bool(15))

# 2 variables
x = "Hello"
y = 15

print(bool(x))
print(bool(y))

# Most Values are True(nonempty,right ones)
bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])

# False ones
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})

# Object that evaluates in False
class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))

# Functions can Return a Boolean
def myFunction() :
  return True

print(myFunction())

# Example(YES!)
def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!")
#isinstance() returns boolean value (checks if variable is some certain data type)
x = 200
print(isinstance(x, int))