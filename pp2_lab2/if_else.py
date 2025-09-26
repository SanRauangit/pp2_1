# Python Conditions and If statements
# Equals: a == b
# Not Equals: a != b
# Less than: a < b
# Less than or equal to: a <= b
# Greater than: a > b
# Greater than or equal to: a >= b

# If statement:
a = 33
b = 200
if b > a:
  print("b is greater than a") # b is greater than a

#   If statement, without indentation (will raise an error):
# a = 33
# b = 200
# if b > a:
# print("b is greater than a") # you will get an error

# The elif keyword is Python's way of saying "if the previous conditions were not true, then try this condition".
a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")  # a and b are equal


# The else keyword catches anything which isn't caught by the preceding conditions.
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")  # a is greater than b


# You can also have an else without the elif:
a = 200
b = 33
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a") # b is not greater than a


# Short hand if
# One line if statement:
if a > b: print("a is greater than b")

# One line if else statement:
a = 2
b = 330
print("A") if a > b else print("B") # B


# One line if else statement, with 3 conditions:
a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")


# Test if a is greater than b, AND if c is greater than a:
a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True") # Both conditions are True


#  Test if a is greater than b, OR if a is greater than c:
a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True") # At least one of the conditions is True


# Test if a is NOT greater than b:
a = 33
b = 200
if not a > b:
  print("a is NOT greater than b") #  a is NOT greater than b


# You can have if statements inside if statements, this is called nested if statements.
x = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")  # Above ten,
                                # and also above 20!


# if statements cannot be empty, but if you for some reason have an if statement with no content, put in the pass statement to avoid getting an error. 
a = 33
b = 200

if b > a:
  pass

