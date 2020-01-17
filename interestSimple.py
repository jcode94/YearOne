# Author: Justice Smith
# Course No.: COP2930
# Date: 1/12/2020
# Assignment Title: Individual Programming Ass't 1
# Brief Description: Simple interest calculator assuming a constant interest rate and no further deposits.

# Welcome message
print("Hello! Today we're going to calculate for compound interest earned.") # Manners matter

# User Input
principal = int(input("How much was your principal?"))
interest = float(input("What was your average interest rate percentage?"))
years = int(input("Over the course of how many years did you accrue interest?"))


# Simple compound interest formula(the only differentiating aspect is lack of periods)
Final = principal*(interest/100)*years

# User Output
print("The total amount saved after", years, "years of saving is", int(Final), end = ".")

