# Justice Smith
# 02.07.20
# COP2930

# planning
# match is first to 2 sets.
# set is first to 6 with 2 game lead(e.g. first to 6-4 or 7-6 tiebreaker

serenaWins = 0
rogerWins = 0
serenaSets = 0
rogerSets = 0

print("Please enter the game winners, in sequence.\n")

while True:
    if serenaSets == 2 or rogerSets == 2:
        if rogerSets > serenaSets:
            print("ROGER won the game 2 sets to {} sets.".format(serenaSets))
            break
        else:
            print("SERENA won the game 2 sets to {}.".format(rogerSets))
        break

    gameWinner = input()

    if gameWinner == "SERENA":
        serenaWins += 1

        if serenaWins == 6 and serenaWins >= (rogerWins + 2):
            serenaWins = 0
            rogerWins = 0
            serenaSets += 1

        if serenaWins == 7 and rogerWins == 6:
            serenaWins = 0
            rogerWins = 0
            serenaSets += 1

    if gameWinner == "ROGER":
        rogerWins += 1

        if rogerWins == 6 and rogerWins >= (serenaWins + 2):
            rogerWins = 0
            serenaWins = 0
            rogerSets += 1

        if rogerWins == 7 and serenaWins == 6:
            rogerWins = 0
            serenaWins = 0
            rogerSets += 1

    else:
        print("Error: Unrecognized Input. Please enter either ROGER or SERENA.")
        continue
