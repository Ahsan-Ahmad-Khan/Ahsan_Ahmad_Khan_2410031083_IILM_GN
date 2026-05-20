num=int(input("Enter number: "))
total=0
temp=num
while num>0:
    digit=num%10
    total=total+digit
    num=num//10
    
print(f"sum of digits of {temp} is: {total}")