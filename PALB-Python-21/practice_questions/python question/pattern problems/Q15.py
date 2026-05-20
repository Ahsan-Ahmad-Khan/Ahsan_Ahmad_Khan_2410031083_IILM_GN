# Increasing Same Number

row=int(input("enter row: "))

for i in range(1,row+1):
    print(str(i)*i)

            # or

for i in range(1,row+1):
    for j in range(i):
        print(i,end="")
    print()