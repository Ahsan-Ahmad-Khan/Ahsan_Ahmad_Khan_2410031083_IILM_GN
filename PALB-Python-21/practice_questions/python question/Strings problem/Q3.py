str=input("enter string: ")
temp=str
rev=""
for i in str:
    rev=i+rev

if rev==temp:
    print(f"{temp} is palindrome")
else:
    print(f"{temp} is not palindrome")

            # or

if str==str[::-1]:
    print(f"{str} is palindrome")
else:
    print(f"{str} is not palindrome")