# Check whether a number is a 3-digit number.
number=int(input("enter number: "))

if number>=100 and number<1000:
    print(f"{number} is three-digit number ")
else:
    print(f"{number} is not three-digit number")
