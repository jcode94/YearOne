# Author: Justice Smith
# Course No.: COP2930
# Assignment Title: Individual Programming Ass't 1
# Date: 1/12/2020
# Brief Description: Take Home Pay

print("Hello! Let's find out your net salary.")

while True: # Loop that triggers when the failure event occurs
    try:
        Gross = float(input("First, what is your gross income?"))   
        if Gross <= 0 or Gross > 1000000: # Conditional statement
            raise ValueError
        break # Breaks program to print error and allow reinput
    except ValueError:
        print("Invalid Error. The income must be between 0 and 1000000 dollars.")

while True:
    try:
        ETP = float(input("What is the effective tax percentage you pay?"))  
        if ETP < 0 or ETP > 100:
            raise ValueError
        break
    except ValueError:
        print("Invalid Error. The effective tax percentage must be between 0 and 100%.")
Net = ((100-ETP)/100)*Gross # net pay formula

print("Sadly, you actually get to take home $", Net) # User output with total
