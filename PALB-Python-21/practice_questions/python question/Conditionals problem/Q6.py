# Palindrome Number
num=int(input("Enter number: "))
temp=num
rev=0
if num==0:
    print("number is  a palindrome")

elif num<0:
    print("number is not a palindrome")
else:
    while num>0:
        digit=num%10
        rev=rev*10+digit
        num=num//10
    
    if temp==rev:
        print("number is palindrome")
    else:
        print("number is not palindrome")
