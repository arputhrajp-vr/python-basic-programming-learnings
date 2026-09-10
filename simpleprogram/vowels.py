"""This program counts the number of vowels in a string."""

text = "python Programming"
count = 0

for char in text:
    if char.lower() in "aeiou":
        count += 1

print("The number of vowels in the string is:", count)