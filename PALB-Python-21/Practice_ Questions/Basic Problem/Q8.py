# Check Triangle Validity

side1=int(input("enter side1 of triangle: "))
side2=int(input("enter side2 of triangle: "))
side3=int(input("enter side3 of triangle: "))

# triangle validity rule: sum of any two sides of triangle > third side
if((side1+side2)>side3 and (side1+side3)> side2 and (side2+side3)>side1):
    print("traingle is valid")
else:
    print("triange is Invalid")

