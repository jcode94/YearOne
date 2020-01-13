# Author: Justice Smith
# Date: 1/12/2020
# Brief Description: Gas cost calculator

print("Hello! I have just a few questions:")
GasPrice = float(input("What is the current cost of gasoline?"))
GasInTank = float(input("How many gallons of gas are in the car right now?"))
GasMileage = float(input("How many miles per gallon of gas can your vehicle travel?"))
TripLength = float(input("How many miles long is your intended trip?"))

Cost = ((TripLength/GasMileage)-GasInTank)*GasPrice

print("Oh no! The cost of gas for your trip is", Cost)
