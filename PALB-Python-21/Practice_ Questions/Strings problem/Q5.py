# Remove All Spaces from String
import string
s=""
str=input("enter string: ")
for i in str:
    if i not in string.whitespace:  # or  if i != " "
        s+=i
print(s)