# Author: Justice Smith
# Course No.: COP2930
# Date: 1/12/2020
# Assignment Title: Individual Programming Ass't 1
# Brief Description: Simple interest calculator

print("Hello! Today we're going to calculate for compound interest earned.") # Manners matter
# First loop is to ensure that the principal is a positive, real number.
while True:
    try:
        principal = int(input("How much was your principal?"))
        if principal < 0:
            raise ValueError
        break
    except ValueError:
        print("Invalid input. Principal must be 0 or more.") # Here is that clarification.
# This loop is to ensure that we get a valid percentage value.
while True:
    try:
        interest = float(input("What was your average interest rate percentage?"))
        if interest < 0 or interest > 100:
            raise ValueError
        break
    except ValueError:
        print("Invalid input. Interest Rate percentage must be between 0% and 100%.")
# This loop is to ensure that the number of years is an integer greater than 0.
while True:
    try:
        years = int(input("Over the course of how many years did you accrue interest?"))
        if years <= 0:
            raise ValueError
        break
    except ValueError:
        print("Invalid input. Years of compounding must be greater than 0.")        
        
# Simple compound interest formula(the only differentiating aspect is lack of periods)
Final = principal*(interest/100)*years

print("The total amount saved after", years, "years of saving is", int(Final), end = ".")
