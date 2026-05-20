# Reverse Triangle
row=int(input("enter row: "))

for i in range(row,0,-1):
    num=1
    for j in range(i):
        print(num,end="")
        num=num+1
    print()