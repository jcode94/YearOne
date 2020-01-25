# Justice Smith
# Arup Guha COP2930
# Problem B: Where Am I?

# import sys,time,random

# typing_speed = 110 #wpm
# def slow_type(t):
#    for l in t:
#        sys.stdout.write(l)
#        sys.stdout.flush()
#        time.sleep(random.random()*7.0/typing_speed)

# Setting initial user location
x = 0
y = 0

# Greeting
print("Welcome to the Grid, User.\n\n")
print("You are currently at (%d, %d) \n\n" % (x, y))

# User Input
while True:
    try:
        xCoord = int(input("What is the x-coordinate of the destination?\n"))
        if xCoord >= 100 or xCoord <= -100:
            raise ValueError
        break
    except ValueError:
        print("That value is far too high for our simple calculator. Try picking a number between -100 and +100.")
while True:
    try:
        yCoord = int(input("What is the y-coordinate of the destination?\n"))
        if yCoord >= 100 or yCoord <= -100:
            raise ValueError
        break
    except ValueError:
        print("That value is far too high for our simple calculator. Try picking a number between -100 and +100.")

# Check for shenanigans
if xCoord == 0 and yCoord == 0:

    print("Wow, you're fast. Even beat my average score of 0.5 * infinity.")
# Beginning of real block
else:
    while True:
        try:
            # Accounting for zero denominator in slope calculation.
            if xCoord == x:
                slope = "undefined"
            else:
                slope_float = (yCoord - y) / (xCoord - x)
                slope = "%.2f" % slope_float
            # Calculating Distance
            dist = ((xCoord - x) ** 2 + (yCoord - y) ** 2) ** (0.5)
            # User Output
            print("The current distance between you and your point (%d, %d) is %.2f and the slope created by that "
                  "line is %s." % (xCoord, yCoord, dist, slope))

            # teaser statement
            print("The shortest path to your destination takes 2 moves! Let's see how close you can get. :)\n")
            direction = input("What direction do you want to move(x/y)?\n")
            sign = input("In a positive or negative direction?\n")
            while True:
                try:
                    path = int(input("And how far do you want to move in that direction?\n"))
                    if path + x >= 100 or path + x <= -100:
                        raise ValueError
                    break
                except ValueError:
                    print("You would be moving outside of the working window. Try a smaller number.")
            # Ensuring correct sign of 'path' before calculation of 'x' and 'y'
            if sign.strip().lower() == "positive":
                path *= 1
            elif sign.strip().lower() == "negative":
                path *= -1
            else:
                print("Your answer must be either 'positive' or 'negative'.")
            # Increasing the coordinate values based on the amended 'path' values.
            if direction.strip().lower() == "x":
                x += path
                print("You are now at (%d, %d).\n\n" % (x, y))
            else:
                y += path
                print("You are now at (%d, %d).\n\n" % (x, y))
            if x == xCoord and y == yCoord:
                print("Congratulations! You've arrived at your destination.")
            elif x != xCoord or y != yCoord:
                raise ValueError
            break
        except ValueError:
            print("We're not quite there yet. We've still a bit to go.\n\n")
