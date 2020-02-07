# Justice Smith
# 02.05.2020
# COP2930-Arup Guha
# Individual Prog Ass't 2

import math

totalFencing = int(input("How much fencing, in feet?"))
print("Your available dimensions are:")
for x in range(1, totalFencing):
    y = (totalFencing/2)-x
    area = x * y
    if y < x:
        break
    print("{} by {} with area {}" .format(x, y, area))




# planning:

# output needs: Write out a single line of the form
# (X by Y with area Z)
# where X is lowdim, in ft, Y is highdim in ft, and Z is area for every possible rectangle
# Order the rectangles by increasing order of X.
# Also, the last line may have X = Y.

# need X factors with % = 0
