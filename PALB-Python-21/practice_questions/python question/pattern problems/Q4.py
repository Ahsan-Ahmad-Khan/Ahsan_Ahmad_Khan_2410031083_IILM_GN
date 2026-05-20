# Right Aligned Triangle
row=int(input("enter row: "))
for i in range(1,row+1):
    print(" "*(row-i)+"*"*i)