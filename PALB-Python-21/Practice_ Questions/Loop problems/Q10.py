# Strong Number
num=int(input("enter number: "))
temp=num
if num<=0:
    print(f"{num} is not strong number")
else:
    
    sum=0
    while num>0:
        digit=num%10
        fact=1
        for i in range(1,digit+1):
            fact=fact*i
        sum+=fact
        num=num//10
    
    if sum==temp:
        print(f"{temp} is strong number")
    else:
        print(f"{temp} is not strong number")
