# Tuple
# A tuple is a collection which is ordered and unchangeable.
# Tuples are written with round brackets.
# Create a Tuple:
thistuple = ("apple", "banana", "cherry")
print(thistuple)

# Tuples allow duplicate values:
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)

# Tuple Length
thistuple = ("apple", "banana", "cherry")
print(len(thistuple))

# # Create Tuple With One Item
# To create a tuple with only one item, you have to add a comma after the item, otherwise Python will not recognize it as a tuple.
# One item tuple, remember the comma:
thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))

# Tuple items can be of any data type:
tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)

# A tuple with strings, integers and boolean values:
tuple1 = ("abc", 34, True, 40, "male")

# What is the data type of a tuple?
mytuple = ("apple", "banana", "cherry")
print(type(mytuple)) #<class 'tuple'>

# The tuple() Constructor
thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)

# List is a collection which is ordered and changeable. Allows duplicate members.
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
# Dictionary is a collection which is ordered** and changeable. No duplicate members.

# Access Tuple Items
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])

# Negative Indexing
thistuple = ("apple", "banana", "cherry")
print(thistuple[-1])

# Range of Indexes
# Return the third, fourth, and fifth item:
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])

# This example returns the items from the beginning to, but NOT included, "kiwi":
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[:4]) #('apple', 'banana', 'cherry', 'orange')

# This example returns the items from "cherry" and to the end:
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:]) #('cherry', 'orange', 'kiwi', 'melon', 'mango')

# Range of Negative Indexes
# This example returns the items from index -4 (included) to index -1 (excluded)
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1]) #('orange', 'kiwi', 'melon')

# Check if Item Exists
# Check if "apple" is present in the tuple:
thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple") # Yes, 'apple' is in the fruits tuple

# Change Tuple Values
# Convert the tuple into a list to be able to change it:
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x) #("apple", "kiwi", "cherry")

# Add Items
# Convert the tuple into a list, add "orange", and convert it back into a tuple:

thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y) # ('apple', 'banana', 'cherry', 'orange')

# Add tuple to a tuple. You are allowed to add tuples to tuples, so if you want to add one item, (or many), create a new tuple with the item(s), and add it to the existing tuple:
thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y

print(thistuple)

# Convert the tuple into a list, remove "apple", and convert it back into a tuple:

thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)

# The del keyword can delete the tuple completely:
thistuple = ("apple", "banana", "cherry")
del thistuple
print(thistuple) #this will raise an error because the tuple no longer exists

# Unpacking a tuple:

fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red) # apple
            # banana
            # cherry

# Using Asterisk*
# If the number of variables is less than the number of values, you can add an * to the variable name and the values will be assigned to the variable as a list:
# Assign the rest of the values as a list called "red":

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red) # apple
            # banana
            # ['cherry', 'strawberry', 'raspberry']

# If the asterisk is added to another variable name than the last, Python will assign values to the variable until the number of values left matches the number of variables left.
# Add a list of values the "tropic" variable:

fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits

print(green)
print(tropic)
print(red)      # apple
                # ['mango', 'papaya', 'pineapple']
                # cherry

# Loop Through a Tuple
# Iterate through the items and print the values:

thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)

# Loop Through the Index Numbers
# Print all items by referring to their index number:

thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
  print(thistuple[i])

# Print all items, using a while loop to go through all the index numbers:

thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
  print(thistuple[i])
  i = i + 1

# Join two tuples:

tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3) #('a', 'b', 'c', 1, 2, 3)
# Multiply the fruits tuple by 2:

fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple) # ('apple', 'banana', 'cherry', 'apple', 'banana', 'cherry')

# Tuple Methods
# count()	Returns the number of times a specified value occurs in a tuple
# index()	Searches the tuple for a specified value and returns the position of where it was found