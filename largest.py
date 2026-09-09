"""This program finds the largest number in a list of numbers. without using the built-in max() function."""

numbers = [3, 7, 2, 9, 1]
Largest = numbers[0]

for number in numbers:
    if number > Largest:
        Largest = number

print("The largest number is:", Largest)