#This is a list comprehension that creates a new list containing only the fruits that have the letter "a" in their names.

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)

#This is the same example above, but using a for loop instead of list comprehension.

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)

#This is a list comprehension that creates a new list containing only the fruits that are not "apple".

newlist = [x for x in fruits if x != "apple"]

#This is the same example above, but using a for loop instead of list comprehension.

newlist = [x for x in fruits]

#This is a list comprehension that creates a new list containing the numbers from 0 to 9.

newlist = [x for x in range(10)]

#This is the same example above, but using a for loop instead of list comprehension accepting less than 5.

newlist = [x for x in range(10) if x < 5]

#This is a list comprehension that creates a new list containing the uppercase versions of the fruits.

newlist = [x.upper() for x in fruits]
