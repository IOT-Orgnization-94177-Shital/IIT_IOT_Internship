def reverse_string(text):
    """Returns the reversed version of the given string"""
    return text[::-1]
def count_vowels(text):
    """Returns the number of vowels in the given string"""
    vowels = "aeiouAEIOU"
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count
from string_ops import reverse_string, count_vowels
s = input("Enter a string: ")
print("Reversed string:", reverse_string(s))
print("Number of vowels:", count_vowels(s))