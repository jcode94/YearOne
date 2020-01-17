# Justice Smith
# 01.17.2020
# Train Meeting

# User Inputs
distance = int(input("What is the current distance between the two trains, in miles?\n"))
speedTrain1MPH = int(input("What is the speed of Train 1 in miles per hour?\n"))
speedTrain2MPH = int(input("What is the speed of Train 2 in miles per hour?\n"))

#equations
z = distance
a = speedTrain1MPH
b = speedTrain2MPH
timeToMeetMinutes = (z/(a+b))*60
distanceTraveledByTrain1 = z*(a/(a+b))
distanceTraveledByTrain2 = z*(b/(a+b))

print("It will take the trains ", float(timeToMeetMinutes), " minutes to meet. Additionally, the distance, in miles, traveled by Train 1 is ", float(distanceTraveledByTrain1)," and the distance traveled by Train 2 is ", float(distanceTraveledByTrain2), ".", sep="")


