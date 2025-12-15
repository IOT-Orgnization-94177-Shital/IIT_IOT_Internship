s = input("Enter a string: ")
print("\nOriginal String:", s)
print("Length of string:", len(s))
print("-" * 50)
print("s[0:5]      :", s[0:5])
print("s[2:7]      :", s[2:7])
print("s[:5]       :", s[:5])        
print("s[3:]       :", s[3:])        
print("s[:]        :", s[:])         
print("-" * 50)
print("s[0:10:2]   :", s[0:10:2])
print("s[::2]      :", s[::2])
print("s[1::2]     :", s[1::2])
print("s[::-1]     :", s[::-1])      
print("-" * 50)
print("s[-5:]      :", s[-5:])
print("s[:-5]      :", s[:-5])
print("s[-8:-3]    :", s[-8:-3])
print("-" * 50)
print("Reversed string:", s[::-1])
if s == s[::-1]:
    print("The string is a Palindrome")
else:
    print("The string is NOT a Palindrome")

print("-" * 50)
if len(s) >= 4:
    print("First 4 characters:", s[:4])
    print("Last 4 characters :", s[-4:])
else:
    print("String length is less than 4")

print("-" * 50)
print("All string slicing demos executed successfully!")
