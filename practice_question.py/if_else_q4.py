marks=float(input("Enter marks out of 100: "))
if(marks>=60 and marks <=100):
    print("Your marks is: ",marks)
    print("You got 1st division")

elif(marks>=50 and marks<=59):
    print("Your marks is: ",marks)
    print("You got 2nd division")

elif(marks>=40 and marks<=49):
    print("Your marks is: ",marks)
    print("You got 3rd division")

elif(marks>=35 and marks<=39):
    print("Your marks is: ",marks)
    print("You are passed")

else:
    print("Your marks is: ",marks)
    print("You failed")

