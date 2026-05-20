# Number Pyramid
row=int(input("enter row: "))
for i in range(1,row+1):
    print(" "*(row-i),end="")
    num=1
    for j in range((2*i)-1):
        print(num,end="")
        num+=1
    print()