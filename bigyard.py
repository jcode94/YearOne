# Justice Smith
# 02.05.2020
# COP2930-Arup Guha
# Individual Prog Ass't 2

# planning:

# output needs: Write out a single line of the form
# (X by Y with area Z)
# where X is lowdim, in ft, Y is highdim in ft, and Z is area for every possible rectangle
# Order the rectangles by increasing order of X.
# Also, the last line may have X = Y.


# The unfactorables under 100(the predetermined input set)...
primes = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97]

# User input
print("How much fencing, in feet?")

# Check for unfactorable primes.
while True:
    # Get totalFencing
    totalFencing = int(input(""))
    # Check to see if input is in prime list
    if totalFencing in primes:
        print("Your number cannot be a prime number. Please enter a composite integer.")
        # Cont. allows for new input
        continue
    else:
        print("Your available dimensions are:")
        for x in range(1, totalFencing, 1):
            y = (totalFencing/2)-x
            area = x * y
            if y < x:
                break
            print("{} by {} with area {}" .format(x, int(y), int(area)))







