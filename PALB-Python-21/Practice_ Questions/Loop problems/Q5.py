# Factorial of a Number
num=int(input("enter number: "))
fact=1
if num==0 or num==1:
    print(f"factorial of {num} is: ",1)
elif num<0:
    print("factorial of negative number are not defined")
else:
    for i in range(num,0,-1):
        fact=fact*i
    print(f"factorial of given {num} is {fact}")
