# Justice Smith
# 02.05.2020
# COP2930-Arup Guha
# Individual Prog Ass't 2

# planning
# match is first to 2 sets.
# set is first to 6 with 2 game lead(e.g. first to 6-4 or 7-6 tiebreaker

# Create variables
serenaWins = 0
rogerWins = 0
serenaSets = 0
rogerSets = 0

# Single iteration instructions, outside looping
print("Please enter the game winners, in sequence.\n")


while True:
    # First check to break out of topmost level, checks after every input
    if serenaSets == 2 or rogerSets == 2:
        if rogerSets > serenaSets:
            # Juicy new-style str formatting
            print("ROGER won the game 2 sets to {} sets.".format(serenaSets))
            break
        else:
            print("SERENA won the game 2 sets to {}.".format(rogerSets))
        break

    # Open, repeating input
    gameWinner = input()

    # 1 of 2 topmost logic forks
    if gameWinner == "SERENA":
        serenaWins += 1

        # Set incrementer for set win condition one
        if serenaWins == 6 and serenaWins >= (rogerWins + 2):
            # Have to reset win counter
            serenaWins = 0
            rogerWins = 0
            serenaSets += 1

        # Set incrementer for set win condition two
        if serenaWins == 7 and rogerWins == 6:
            serenaWins = 0
            rogerWins = 0
            serenaSets += 1

    # 2 of 2 topmost level forks
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

    #Basic input response for anything not two acceptable inputs.
    else:
        print("Error: Unrecognized Input. Please enter either ROGER or SERENA.")
        continue
