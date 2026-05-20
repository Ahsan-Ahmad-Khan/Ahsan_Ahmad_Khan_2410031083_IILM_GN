# Grade System
mark=int(input("enter mark: "))
if mark>=90 and mark<=100:
    print("Grade A")
elif(mark>=75 and mark<90):
    print("Grade B")
elif(mark>=50 and mark<75):
    print("Grade C")
else:
    print("Fail")