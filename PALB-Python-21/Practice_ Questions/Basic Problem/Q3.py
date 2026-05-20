# Calculate Power Without Using **
num=int(input("Enter number: "))
power=int(input("Enter power: "))

result=1
for i in range(power):
    result*=num

print(result)


# Calculate Power Using **
print(num**power)