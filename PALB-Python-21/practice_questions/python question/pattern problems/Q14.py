# Hollow Diamond
#    *
#   * *
#  *   *
#   * *
#    *

# row=int(input("enter row: "))

# for i in range(1,row+1):
#     print(" "*(row-i),end="")
#     for j in range(1,2*i):
#         if j==1 or j==2*i-1:
#             print("*",end="")
#         else:
#             print(" ",end="")
#     print()
# for i in range(row-1,0,-1):
#     print(" "*(row-i),end="")
#     for j in range(1,2*i):
#         if j==1 or j==2*i-1:
#             print("*",end="")
#         else:
#             print(" ",end="")
#     print()
row=int(input("enter row: "))
for i in range(1,row+1):
    print(" "*(row-i),end="")
    for j in range(1,2*i):
        if j==1 or j==2*i-1:
            print("*",end="")
        else:
            print(" ",end="")
    print()

for i in range(row-1,0,-1):
    print(" "*(row-i),end="")
    for j in range(1,2*i):
        if j==1 or j==2*i-1:
            print("*",end="")
        else:
            print(" ",end="")
    print()
