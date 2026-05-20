# Find Largest Element in List
lst=[1,2,30,4,8,9]
largest_elem=lst[0]     # or largest_elem=float('-inf')
for i in range(len(lst)):
    if lst[i]>largest_elem:
        largest_elem=lst[i]
    
print(largest_elem)