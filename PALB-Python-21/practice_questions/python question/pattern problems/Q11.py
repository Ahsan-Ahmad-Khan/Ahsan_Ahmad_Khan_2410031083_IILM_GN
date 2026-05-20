# Hollow Pyramid
#     *
#    * *
#   *   *
#  *     *
# *********

row=int(input("enter row: "))
for i in range(1,row+1):
    print(" "*(row-i),end="")
    for j in range(1,2*i):
        if j==1 or j==2*i-1 or i==row:
            print("*",end="")
        else:
            print(" ",end="")
    print()