# Count frequency of each character using dictionary.
str=input("enter string: ")
d={}

for i in str:
    # d[i]=str.count(i)
            # or
    if i in d:
        d[i]+=1
    else:
        d[i]=1

print(d)