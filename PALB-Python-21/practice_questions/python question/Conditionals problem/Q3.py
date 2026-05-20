# Simple Calculator (if-elif)
num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))
operator=input("Enter operator (+,-,/,*): ")

if operator=='+':
    print(f"the sum of {num1} and {num2} is: {num1+num2} ")
elif(operator=='-'):
    print(f"The subtraction of {num1} and {num2} is {num1-num2}")
elif operator=='*':
    print(f"The multiplication of {num1} and {num2} is : {num1*num2}")
elif(operator=='/'):
    print(f"The division of {num1} and {num2} is: {num1/num2}")
else:
    print("Invalid operator")
