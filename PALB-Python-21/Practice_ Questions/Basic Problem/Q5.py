# Swap Two Numbers using multiple assignment- without using third variable
num1=int(input("Enter First Number: "))
num2=int(input("Enter Second Number: "))
print("Before swapping: ",num1,num2)
# num1,num2=num2,num1
    # or
# num1=num1+num2
# num2=num1-num2
# num1=num1-num2

# or using xor swapping
num1=num1^num2
num2=num1^num2
num1=num1^num2

# using third variable:
# temp=num1
# num1=num2
# num2=temp
print("After swapping: ",num1,num2)



