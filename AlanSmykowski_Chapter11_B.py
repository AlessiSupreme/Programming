#Program to determine the length of the hypotenuse of a right triangle based on user input

import math


#Calculation
def calculateHypotenuse(angleDegrees, adjacentSide):
    
    #Convert angle
    angleRadians = math.radians(angleDegrees)
    
    #Calculate hypotenuse
    hypotenuse = adjacentSide / math.cos(angleRadians)
    
    return hypotenuse


#Main
def main():
    
    #Prompt for angle
    angleDegrees = float(input("\nEnter the nearest angle in degrees: "))
    
    #Prompt for side length
    adjacentSide = float(input("Enter the length of the adjacent side: "))

    #Call for calculation
    hypotenuse = calculateHypotenuse(angleDegrees, adjacentSide)

    #Print hypotenuse
    print(f"The length of the hypotenuse is {hypotenuse:.2f}")


#Main call
if __name__ == "__main__":
    main()