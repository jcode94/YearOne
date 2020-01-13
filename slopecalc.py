# Author: Justice Smith
# Date: 1/12/2020
# Brief Description: Calculate slope from two points

# User coordinate inputs
X1 = int(input("What is the x-coordinate of the first point?"))
Y1 = int(input("What is the y-coordinate of the first point?"))
X2 = int(input("What is the x-coordinate of the second point?"))
Y2 = int(input("What is the y-coordinate of the second point?"))

#formula input for calculation
slope = (Y2 - Y1)/(X2 - X1)

# User output
print("The slope of your line is", slope)

