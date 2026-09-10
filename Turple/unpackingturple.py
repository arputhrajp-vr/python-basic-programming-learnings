# Unpacking a tuple

fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)

# You can also use an asterisk * to collect the remaining values as a list.

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)

## If the asterisk is added to another variable name than the last, Python will assign values to the variable until the number of values left matches the number of variables left.

fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits

print(green)
print(tropic)
print(red)