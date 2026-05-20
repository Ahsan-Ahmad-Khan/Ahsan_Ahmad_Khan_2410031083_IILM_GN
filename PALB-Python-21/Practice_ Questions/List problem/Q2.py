# Find third Largest Element
lst=[1,2,9,10,3,6,5,9.3]
largest_elem=second_elem=third_element=float('-inf')
for i in lst:
    if i > largest_elem:
        third_element=second_elem
        second_elem=largest_elem
        largest_elem=i
    elif i>second_elem and i != largest_elem:
        third_element=second_elem
        second_elem=i
    elif (i>third_element and i!= largest_elem and i!=second_elem):
        third_element=i
    
print(largest_elem,second_elem,third_element)

    




