# Fibonacci Series
# 0 1 1 2 3 5 8 13
num=int(input("enter number: "))
first_num=0
second_num=1

for i in range(num):
    print(first_num,end=" ")
    first_num,second_num=second_num,first_num+second_num
