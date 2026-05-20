"""If salary > 50000 → 10% bonus
Else → 5% bonus"""

salary=int(input("enter salary: "))

if salary>50000:
    bonus=salary * 0.10
else:
    bonus=salary*0.05

print(bonus)

