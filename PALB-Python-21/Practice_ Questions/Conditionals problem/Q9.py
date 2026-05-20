"""Check whether input character is:
Digit
Uppercase
Lowercase"""

char=input("enter character: ")
if char.isdigit():
    print("char is a digit ",char)
elif char.isupper():
    print("char is in uppercase ",char)
elif char.islower():
    print("char is in lower case ",char)
else:
    print("use other method")

