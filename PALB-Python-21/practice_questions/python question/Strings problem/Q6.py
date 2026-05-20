str=input("enter string: ")
word=str.split()
largest=word[0]
for i in word:
    if len(i)>len(largest):
        largest=i
print(largest)

