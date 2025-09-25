#Set
# Sets are written with curly brackets.
# Create a Set:

thisset = {"apple", "banana", "cherry"}
print(thisset)

# Sets cannot have two items with the same value.
thisset = {"apple", "banana", "cherry", "apple"}

print(thisset)

# True and 1 is considered the same value:

thisset = {"apple", "banana", "cherry", True, 1, 2}

print(thisset)

# False and 0 is considered the same value:

thisset = {"apple", "banana", "cherry", False, True, 0}

print(thisset)

# To determine how many items a set has, use the len() function.
thisset = {"apple", "banana", "cherry"}

print(len(thisset))

# Set items can be of any data type:
set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}

# A set with strings, integers and boolean values:

set1 = {"abc", 34, True, 40, "male"}

# Sets are defined as objects with the data type 'set':
myset = {"apple", "banana", "cherry"}
print(type(myset)) #<class 'set'>

# Using the set() constructor to make a set:

thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)

# List is a collection which is ordered and changeable. Allows duplicate members.
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
# Dictionary is a collection which is ordered** and changeable. No duplicate members.

# Access Items
thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)

# Check if "banana" is present in the set:

thisset = {"apple", "banana", "cherry"}

print("banana" in thisset) # True

# Check if "banana" is NOT present in the set:

thisset = {"apple", "banana", "cherry"}

print("banana" not in thisset) # False

# Add Items
thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset) # {'orange', 'banana', 'apple', 'cherry'}

# Add elements from tropical into thisset:

thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

print(thisset) #{'apple', 'mango', 'cherry', 'pineapple', 'banana', 'papaya'}

# Add Any Iterable
# Add elements of a list to a set:
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

thisset.update(mylist)

print(thisset) # {'banana', 'cherry', 'apple', 'orange', 'kiwi'}

# Remove "banana" by using the remove() method:

thisset = {"apple", "banana", "cherry"}

thisset.remove("banana")

print(thisset) # {'cherry', 'apple'}
# Note: If the item to remove does not exist, remove() will raise an error.

# Remove "banana" by using the discard() method:

thisset = {"apple", "banana", "cherry"}

thisset.discard("banana")

print(thisset) # {'cherry', 'apple'}
# Note: If the item to remove does not exist, discard() will NOT raise an error.

# Remove a random item by using the pop() method:

thisset = {"apple", "banana", "cherry"}

x = thisset.pop()

print(x)

print(thisset)
# Note: Sets are unordered, so when using the pop() method, you do not know which item that gets removed.

# The clear() method empties the set:

thisset = {"apple", "banana", "cherry"}

thisset.clear()

print(thisset)

# The del keyword will delete the set completely:

thisset = {"apple", "banana", "cherry"}

del thisset

print(thisset)

# Loop through the set, and print the values:

thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)

# The union() and update() methods joins all items from both sets.

# The intersection() method keeps ONLY the duplicates.

# The difference() method keeps the items from the first set that are not in the other set(s).

# The symmetric_difference() method keeps all items EXCEPT the duplicates.  

# The union() method returns a new set with all items from both sets.
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3) # {3, 'a', 'b', 1, 'c', 2}

# You can use the | operator instead of the union() method, and you will get the same result.
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1 | set2
print(set3) # {'c', 3, 'a', 1, 'b', 2}

# Join Multiple Sets
# Join multiple sets with the union() method:

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

myset = set1.union(set2, set3, set4)
print(myset) # {'c', banana, 3, Elena, 'a', apple, John, 2, 'b', cherry, 1}

# Use | to join two sets:

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

myset = set1 | set2 | set3 |set4
print(myset) # {John, 2, 'a', 3, cherry, 1, banana, 'b', 'c', Elena, apple}

# Join a set with a tuple:

x = {"a", "b", "c"}
y = (1, 2, 3)

z = x.union(y)
print(z) # {1, 2, 'a', 'c', 3, 'b'}
# Note: The  | operator only allows you to join sets with sets, and not with other data types like you can with the  union() method.

#The update() method inserts all items from one set into another.
# The update() changes the original set, and does not return a new set. 
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1) #{1, 'b', 'a', 3, 'c', 2}
# Note: Both union() and update() will exclude any duplicate items.


# The intersection() method will return a new set, that only contains the items that are present in both sets.
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.intersection(set2)
print(set3) # {'apple'}

# You can use the & operator instead of the intersection() method, and you will get the same result.
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 & set2
print(set3)
# Note: The & operator only allows you to join sets with sets, and not with other data types like you can with the intersection() method.

#The intersection_update() method will also keep ONLY the duplicates, but it will change the original set instead of returning a new set.
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.intersection_update(set2)

print(set1)

# The values True and 1 are considered the same value. The same goes for False and 0.
set1 = {"apple", 1,  "banana", 0, "cherry"}
set2 = {False, "google", 1, "apple", 2, True}

set3 = set1.intersection(set2)

print(set3) #{False, True, 'apple'}

# The difference() method will return a new set that will contain only the items from the first set that are not present in the other set.
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.difference(set2)

print(set3) #{'banana', 'cherry'}

# You can use the - operator instead of the difference() method, and you will get the same result.
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 - set2
print(set3) # {'banana', 'cherry'}
# Note: The - operator only allows you to join sets with sets, and not with other data types like you can with the difference() method.

# The difference_update() method will also keep the items from the first set that are not in the other set, but it will change the original set instead of returning a new set.
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.difference_update(set2)

print(set1) # {'banana', 'cherry'}

# The symmetric_difference() method will keep only the elements that are NOT present in both sets.
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.symmetric_difference(set2)

print(set3) #{'google', 'banana', 'microsoft', 'cherry'}
# You can use the ^ operator instead of the symmetric_difference() method, and you will get the same result.

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 ^ set2
print(set3) # {'google', 'banana', 'microsoft', 'cherry'}
# Note: The ^ operator only allows you to join sets with sets, and not with other data types like you can with the symmetric_difference() method.


# The symmetric_difference_update() method will also keep all but the duplicates, but it will change the original set instead of returning a new set.
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.symmetric_difference_update(set2)

print(set1)

# Use the frozenset() constructor to create a frozenset from any iterable.
x = frozenset({"apple", "banana", "cherry"})
print(x)
print(type(x)) # frozenset({'apple', 'cherry', 'banana'})
                # <class 'frozenset'>


# # Frozenset methods
# copy()	 	Returns a shallow copy	
# difference()	-	Returns a new frozenset with the difference	
# intersection()	&	Returns a new frozenset with the intersection	
# isdisjoint()	 	Returns whether two frozensets have an intersection	
# issubset()	<= / <	Returns True if this frozenset is a (proper) subset of another	
# issuperset()	>= / >	Returns True if this frozenset is a (proper) superset of another	
# symmetric_difference()	^	Returns a new frozenset with the symmetric differences	
# union()	|	Returns a new frozenset containing the union

# # Set methods
# add()	 	Adds an element to the set
# clear()	 	Removes all the elements from the set
# copy()	 	Returns a copy of the set
# difference()	-	Returns a set containing the difference between two or more sets
# difference_update()	-=	Removes the items in this set that are also included in another, specified set
# discard()	 	Remove the specified item
# intersection()	&	Returns a set, that is the intersection of two other sets
# intersection_update()	&=	Removes the items in this set that are not present in other, specified set(s)
# isdisjoint()	 	Returns whether two sets have a intersection or not
# issubset()	<=	Returns True if all items of this set is present in another set
#  	<	Returns True if all items of this set is present in another, larger set
# issuperset()	>=	Returns True if all items of another set is present in this set
#  	>	Returns True if all items of another, smaller set is present in this set
# pop()	 	Removes an element from the set
# remove()	 	Removes the specified element
# symmetric_difference()	^	Returns a set with the symmetric differences of two sets
# symmetric_difference_update()	^=	Inserts the symmetric differences from this set and another
# union()	|	Return a set containing the union of sets
# update()	|=	Update the set with the union of this set and others

