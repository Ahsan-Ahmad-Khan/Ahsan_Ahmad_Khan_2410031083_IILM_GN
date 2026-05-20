"""Calculate Simple Interest using formula:
SI = (P × R × T) / 100"""

P=int(input("Enter Principal amount: "))
R=int(input("enter annual interest rate: "))
T=int(input("Enter Time period in Years: "))

SI=(P*R*T)/100
print("The simple interest is: ",SI)
