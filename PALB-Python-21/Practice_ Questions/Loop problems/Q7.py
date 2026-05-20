# Reverse a Number
num=int(input("enter number: "))
rev=0
if num<0:
    sign=-1
else:
    sign=1

num=abs(num)
while num>0:
    digit=num%10
    rev=rev*10+digit
    num=num//10

print("reverse number is : ",sign*rev)
