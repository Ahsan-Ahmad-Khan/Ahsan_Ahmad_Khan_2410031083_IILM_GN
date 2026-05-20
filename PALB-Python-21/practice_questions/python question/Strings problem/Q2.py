# Reverse a String (Without Slicing)
str=input("enter string: ")
# for i in range(len(str),0,-1):
#     print(str[i-1],end="")

        # or
    
rev=""
for ch in str:
    rev=ch+rev
print(rev)