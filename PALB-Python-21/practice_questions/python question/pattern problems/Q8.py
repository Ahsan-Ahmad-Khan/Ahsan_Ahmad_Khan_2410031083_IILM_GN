# Diamond pattern
row=int(input("enter row: "))

# upper
for i in range(1,row):
    print(" "*(row-i)+"*"*((2*i)-1)+" "*(row-i))
# lower
for i in range(row,0,-1):
    print(" "*(row-i)+"*"*((2*i)-1)+" "*(row-i))

