import math
def areaCircle():
    radius=int(input("Enter the radius "))
    pi=3.14
    area=pi*(radius**2)
    print("area of circle is {}".format(area))
def areaTraingle():
    height=int(input("Height of traigle "))
    base=int(input("Base of traingle "))
    print("area of Triangle ".format(0.5*base*height))
def areatraigle():
    side1=int(input("Side 1 "))
    side2=int(input("Side 2 "))
    side3=int(input("Side 3 "))
    s=side1+side2+side3
    print("area of Triangle {} ".format(((s-side1)*(s-side2)*(s-side3))**(1/2)))
    
areatraigle()