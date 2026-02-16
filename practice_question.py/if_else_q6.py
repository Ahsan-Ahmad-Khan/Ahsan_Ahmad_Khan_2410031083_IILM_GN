Ram_age=int(input("Enter age of Ram: "))
Shyam_age=int(input("Enter age of shyam: "))
Ajay_age=int(input("Enter age of ajay: "))

if(Ram_age>Shyam_age and Ram_age>Ajay_age):
    print(f"Ram is Younger and age is {Ram_age}")
elif(Shyam_age>Ram_age and Shyam_age>Ajay_age):
    print(f"Shyam is Younger and age is {Shyam_age}")
else:
    print(f"Ajay is Younger and age is {Ajay_age}")