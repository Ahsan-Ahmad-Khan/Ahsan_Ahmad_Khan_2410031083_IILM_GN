# BUTTERFLY PATTERN
#  for n=4
# *      *
# **    **
# ***  ***
# ********
# ********
# ***  ***
# **    **
# *      *

row = int(input("enter row: "))
for i in range(1,row+1):
    print("*"*i+" "*(2*(row-i))+"*"*i)
for i in range(row,0,-1):
    print("*"*i+" "*(2*(row-i))+"*"*i)