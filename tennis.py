# Justice Smith
# 02.07.20
# COP2930

# planning
# match is first to 2 sets.
# set is first to 6 with 2 game lead(e.g. first to 6-4 or 7-6 tiebreaker

sGames = 0
rGames = 0
sSets = 0
rSets = 0
totalSets = 0


gameWinner = raw_input("Please enter the game winners, in sequence.\n")

while True:
    if gameWinner == "SERENA":
        sGames += 1
        if sGames == 6 and rGames < 5:
            sSets += 1
            totalSets += 1
        elif sGames == 7:
            sSets += 1
    if gameWinner == "ROGER":
        rGames += 1
        if rGames == 6 and sGames < 5:
            rSets += 1
            totalSets += 1
        elif rGames == 7:
            rSets += 1
    if totalSets >= 2 and sSets == 2 or rSets == 2:
        break
if sSets == 2:
    player = "SERENA"
    print("{} won the match 2 sets to {}".format(player, rSets))
if rSets == 2:
    player = "ROGER"
    print("{} won the match 2 sets to {}".format(player, sSets))


