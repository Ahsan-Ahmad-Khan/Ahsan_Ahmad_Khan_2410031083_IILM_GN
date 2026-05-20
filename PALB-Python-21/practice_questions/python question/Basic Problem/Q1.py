# Largest of three number
num1=int(input("Enter First Number: "))
num2=int(input("Enter Second Number: "))
num3=int(input("Enter Third Number: "))

if num1>num2 and num1>num3:
    print(f"{num3} is largest")
elif num2>num3 and num2>num1:
    print(f"{num2} is largest")
else:
    print(f"{num3} is greater")