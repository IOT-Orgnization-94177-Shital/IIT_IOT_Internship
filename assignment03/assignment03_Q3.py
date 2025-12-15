def count_vowels(s):
    vowels = "aeiouAEIOU"
    v_count = 0
    for ch in s:
        if ch in vowels:
            v_count += 1
    return v_count
def count_consonants(s):
    c_count = 0
    for ch in s:
        if ch.isalpha() and ch.lower() not in "aeiou":
            c_count += 1
    return c_count
def vowel_consonant_ratio(vowels, consonants):
    if consonants == 0:
        return "Cannot calculate ratio (consonants = 0)"
    return vowels / consonants
string = input("Enter a string: ")
v = count_vowels(string)
c = count_consonants(string)
ratio = vowel_consonant_ratio(v, c)
print("Number of vowels     :", v)
print("Number of consonants :", c)
print("Vowel to consonant ratio :", ratio)