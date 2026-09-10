#This is a list sort method that sorts the list alphabetically, and a case-insensitive sort method that sorts the list alphabetically without considering the case of the letters.
thislist = ["banana", "Orange", "Kiwi", "Cherry"]
thislist.sort()
print(thislist)

#This is a list sort method that sorts the list alphabetically, and a case-insensitive sort method that sorts the list alphabetically without considering the lowercase of the letters. 
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist) 

#This is a list reverse method that reverses the order of the list.

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)