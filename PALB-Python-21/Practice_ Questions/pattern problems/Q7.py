# inverted Pyramid Pattern
row=int(input("enter row: "))
for i in range(row,0,-1):
    print(" "*(row-i)+"*"*((2*i)-1)+" "*(row-i))
