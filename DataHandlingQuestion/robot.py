print("robot movement prgram detecting its intiall and final postion distance from origin")
#Let it intiall postion at orgin
#Up
import math
while(1>0):
    up=int(input("Enter up: "))
    down=int(input("Enter down: "))
    left=int(input("Enter left: "))
    right=int(input("Enter right: "))
    #Caluculate distance
    distance=(math.sqrt((up-down)**2+(left-right)**2))
    print("Distance {}".format(round(distance,2)))