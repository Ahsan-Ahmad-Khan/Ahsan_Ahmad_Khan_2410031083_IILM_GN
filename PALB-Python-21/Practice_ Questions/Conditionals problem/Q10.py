# Armstrong Number

num=int(input("enter number: "))
temp=num
total=0
power=len(str(num))
while num>0:
    digit=num%10
    total=total+digit**power
    num=num//10
    
if temp==total:
    print("numbsr is armstrong number")
else:
    print("number is not armstrong number")
    