# Justice Smith
# 1.24.2020
# COP2930
# Pair Programming Problem A

# dummy value
distance = 0

# User Input
totalTimeBiking = float(input("How long, in minutes, did you want to spend biking?\n"))
# Establishing threshold
if 0 < totalTimeBiking <= 30:
    distance = (totalTimeBiking / 60) * 28
elif 30 < totalTimeBiking <= 60:
    # Auto-inserted the cumulative values rather than include the recalculation since the values past are static.
    distance = 14 + ((totalTimeBiking - 30) / 60) * 20
elif 60 < totalTimeBiking <= 90:
    distance = 24 + ((totalTimeBiking - 60) / 60) * 14
elif totalTimeBiking > 90:
    distance = 31 + ((totalTimeBiking - 90) / 60) * 10
# User Output
print("You will bike a distance of", distance, "miles.")
