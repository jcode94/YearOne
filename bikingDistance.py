# Justice Smith
# COP2930
# Pair Programming Problem A

# User Input
totalTimeBiking = float(input("How long, in minutes, did you want to spend biking?\n"))
# Establishing threshold
if totalTimeBiking > 0 and totalTimeBiking <= 30:
    dist = (totalTimeBiking/60)*28
elif totalTimeBiking > 30 and totalTimeBiking <= 60:
# Auto-inserted the cumulative values rather than include the recalculation since the values past are static.
    dist = 14 + ((totalTimeBiking-30)/60)*20
elif totalTimeBiking > 60 and totalTimeBiking <= 90:
    dist = 24 + ((totalTimeBiking-60)/60)*14
elif totalTimeBiking > 90:
    dist = 31 + ((totalTimeBiking-90)/60)*10
# User Output
print("You will bike a distance of", dist, "miles.")