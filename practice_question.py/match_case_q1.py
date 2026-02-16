# day=input("Enter day: ")
# season=input("enter seson(rainy,snowy,windy,sunny,overcast): ")
# if day=="sunday":
#     if(season=="sunny"):
#         print(season)
# elif day=="Monday":
#     if(season=="rainy"):
#         print(season)
# elif day=="Tuesday":
#     if(season=="snowy"):
#         print(season)

# elif day=="wednesday":
#     if(season=="windy"):
#         print(season)

# elif day=="Thurssday":
#     if(season=="Overcast"):
#         print(season)

# elif day=="Friday":
#     if(season=="again rainyt"):
#         print(season)

# elif day=="saturday":
#     if(season=="again windy"):
#         print(season)



# match season:
#     case "sunny" if day=='sunday':
#         print(f"Today is {day}")
#     case "snowy" if day=="monday":
#         print(f"today is {day}")
#     case "windy" if day=="Tuesday":
#         print(f"today is {day}")
#     case "overcast" if day=="wednesday":
#         print(f"today is {day}")
#     case "rainy" if day=="Thursday":
#         print(f"Today is {day}")

# marks=int(input("Enter marks out of 100: "))

# match marks:
#     case marks if 90<marks<=100:
#         print("grade is A")
#     case marks if 80<marks<=90:
#         print("grade is B")
#     case marks if 70<marks<=80:
#         print("grade is c")
#     case marks if 60<marks<=70:
#         print("grade is D")


P=int(input("enter principal amount: "))
R=int(input("enter rate: "))
T=int(input("enter Years: "))

SI=(P*R*T)/100
print(SI)
Amount=(P*((1/R)*100))**T
print(Amount)
CI=Amount-P
print(CI)
difference=SI-CI
print(difference)
match difference:
    case difference if 0<=difference<50:
          print(difference**2)

    case difference if 50<=difference<200:
          print(difference**3)

    case difference if 200<=difference<1000:
          print(difference**0.5)

    case difference if difference>=2000:
          print(difference**0.33)
    
    









