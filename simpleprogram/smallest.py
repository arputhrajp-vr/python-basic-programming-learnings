"""This program finds the smallest number in a list of numbers without using the built-in min() function."""

numbers=[3, 7, 2, 9, 1]
smallest = numbers[0]

for number in numbers:
    if number < smallest:
        smallest = number

print("The smallest number is:", smallest)