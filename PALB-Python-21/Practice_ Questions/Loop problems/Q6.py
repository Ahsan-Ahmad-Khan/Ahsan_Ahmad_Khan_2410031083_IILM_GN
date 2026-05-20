# Count Digits in a Number
num=int(input("enter number: "))
count=0
if num==0:
    print("count: ",1)
else:
    while num>0:
        digit=num%10
        count+=1
        num=num//10
    
    print("count: ",count)