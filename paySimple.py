# Author: Justice Smith
# Course No.: COP2930
# Assignment Title: Individual Programming Ass't 1
# Date: 1/12/2020
# Brief Description: Take Home Pay

# User Input
print("Hello! Let's find out your net salary.")

# Variable Declaration/Assignment
Gross = float(input("First, what is your gross income?"))
ETP = float(input("What is the effective tax percentage you pay?"))  

# Equations/calculations
Net = ((100-ETP)/100)*Gross # net pay formula

# Output
print("Sadly, you actually get to take home $", Net) # User output with total

