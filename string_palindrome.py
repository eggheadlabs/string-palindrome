# How do you check if a given string is a palindrome?
# Example: "racecar"

def is_palindrome(s):
    return s == s[::-1]

s = "racecar"
if is_palindrome(s):
    print(s + ' is palindrome')
else:
    print(s + ' is not palindrome')