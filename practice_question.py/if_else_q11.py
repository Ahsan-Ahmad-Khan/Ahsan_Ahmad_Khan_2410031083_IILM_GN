# to calculate eliectricity bill calculaton
units=int(input("enter used units: "))
if(units<=100):
    print("3 rupees per unit")
    bill= units*3

elif (units<=200):
    print("5 rupees per unit")
    bill=(100*3)+(units-100)*5
else:
    print("7 rupees per unit")
    bill=(100*3)+(100*5)+(units-200)*7
print(bill)