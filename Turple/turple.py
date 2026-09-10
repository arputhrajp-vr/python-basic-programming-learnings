#printing a tuple

thistuple = ("apple", "banana", "cherry")
print(thistuple)

#Tuples can also be created without the parentheses

thistuple = "apple", "banana", "cherry"
print(thistuple)

# Tuples can have different data types

thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)

# Print the number of items in the tuple:

thistuple = ("apple", "banana", "cherry")
print(len(thistuple))

"""To create a tuple with only one item, you have to add a comma after the item, otherwise Python will not recognize it as a tuple.

Example
One item tuple, remember the comma"""

thistuple = ("apple",)
print(thistuple)

# To create an empty tuple, use round brackets with no content.
thistuple = ()
print(type(thistuple))

