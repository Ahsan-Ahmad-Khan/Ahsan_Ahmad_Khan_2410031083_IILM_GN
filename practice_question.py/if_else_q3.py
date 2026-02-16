Qty=int(input("enter Quantity of items: "))
Qtyprice=float(input("enter original price: "))

if Qty>1000:
    discount=10
    total_expenses=Qtyprice*Qty-(Qtyprice*Qty*discount)/100
    print(total_expenses)
else:
    total_expenses=Qtyprice*Qty
    print(total_expenses)
