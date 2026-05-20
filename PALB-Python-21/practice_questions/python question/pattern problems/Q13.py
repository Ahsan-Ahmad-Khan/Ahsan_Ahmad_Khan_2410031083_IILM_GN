# Alternating 0-1 Triangle
# 1
# 01
# 101
# 0101

row=int(input("enter row: "))
for i in range(1,row+1):
    toggle=i%2
    for j in range(i):
        print(toggle,end="")
        toggle=1-toggle
    print()
