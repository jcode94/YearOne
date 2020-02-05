# Justice Smith
# 02.05.2020
# COP2930-Arup Guha
# Individual Prog Ass't 2

import math

totalFencing = 0

# Greet
print("Welcome! We're going to calculate the fencing dimensions available to you.\n")
# User initial input; what we have to work with
totalFencing = int(input("How much fencing do you have, in feet?")

while True:
    for lowdim in range(4, math.sqrt(totalFencing)):
        if totalFencing%lowdim == 0:
            highdim = totalFencing/lowdim
            print("%d by %d", lowdim highdim)

print("The dimensions available to you are:\n %d by %")

# planning:

# output needs: Write out a single line of the form
# (X by Y with area Z)
# where X is lowdim, in ft, Y is highdim in ft, and Z is area for every possible rectangle
# Order the rectangles by increasing order of X.
# Also, the last line may have X = Y.

# need X factors with % = 0

