row=int(input("enter row: "))
for i in range(1,row+1):
    print(" "*(row-i)+"*"*(2*i-1))

                # or

for i in range(1,row+1):
    print(" "*(row-i),end="")
    for j in range(2*i-1):
        print("*",end="")
    print()