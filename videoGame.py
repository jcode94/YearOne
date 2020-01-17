# Justice Smith
# 1.17.2020
# videoGameCost Formula

# User Input
payPerHour = int(input("What is your hourly pay?\n"))
workHours = int(input("How many hours do you work weekly?\n"))
weeksWorked = int(input("How many weeks are you planning to work this summer?\n"))
costVideoGame = int(input("What is the cost of a single video game?\n"))

# Equations for information integration
numberOfVideoGames = (payPerHour*workHours*weeksWorked)//costVideoGame
leftover = (payPerHour*workHours*weeksWorked)%costVideoGame

#User output
print("With your income earned, you will be able to purchase ", numberOfVideoGames," video games and will have $", leftover," dollars left over.", sep="")

