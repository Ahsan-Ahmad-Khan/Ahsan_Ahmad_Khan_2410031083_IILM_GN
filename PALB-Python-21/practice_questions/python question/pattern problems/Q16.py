# Increasing Continuous Numbers
row=int(input("enter number: "))
num=1
for i in range(1,row+1):
    for j in range(i):
        print(num,end="")
        num=num+1
    print()