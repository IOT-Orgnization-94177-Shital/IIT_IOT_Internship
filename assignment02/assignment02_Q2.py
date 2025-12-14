num = int(input("enter a 5 digit number:"))
rev = 0
temp = num
while temp > 0:
    digit = temp % 10
    rev = rev * 10 + digit
    temp = temp //10
# if num == rev:
# print("the number is a palindrome.")
# else:
# print("the number is not palindrom.") 