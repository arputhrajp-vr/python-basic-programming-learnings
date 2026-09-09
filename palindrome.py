# Input string
text = "madam"

# Initialize reverse as an empty string
reverse = ""

# Reverse the string manually
for char in text:
    reverse = char + reverse  # Prepend each character

# Check if the string is a palindrome
if text == reverse:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
