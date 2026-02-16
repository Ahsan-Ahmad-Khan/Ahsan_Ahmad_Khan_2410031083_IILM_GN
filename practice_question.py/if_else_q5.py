import math
centre_point_x=int(input("enter x"))
centre_point_y=int(input("enter y"))
point_x1=int(input("enter x1"))
point_y1=int(input("enter y1"))

radius=int(input("enter radius: "))
distance=math.sqrt((point_x1-centre_point_x)*2 + (point_y1-centre_point_y)*2)
if(distance>radius):
    print("point is outside the circle")
elif(distance==radius):
    print("point is on circle")
else:
    print("point is inside circle")