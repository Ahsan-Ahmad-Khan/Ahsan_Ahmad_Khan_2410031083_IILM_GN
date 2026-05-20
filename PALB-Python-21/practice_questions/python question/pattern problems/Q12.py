# Diamond Number Pattern
#    1
#   121
#  12321
#   121
#    1

row=int(input("enter row: "))
for i in range(1,row+1):
    print(" "*(row-i),end="")
    for j in range(1,i+1):
        print(j,end="")
    for j in range(i-1,0,-1):
        print(j,end="")
    print()
for i in range(row-1,0,-1):
    print(" "*(row-i),end="")
    for j in range(1,i+1):
        print(j,end="")
    for j in range(i-1,0,-1):
        print(j,end="")
    print()
