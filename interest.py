# Justice Smith
# COP2930
# 1/18/2020
# Individual Programming Ass't 1...but hardmode
# compound interest calculator w regular deposits

print("Hello! Today we're going to calculate for compound interest earned with regular deposits.")  # Manners matter


# We need to find out if there was an initial deposit
while True:
    try:
# This while loop accounts for the 3 options: Y, N, and otherChar
        answer1 = input("Did you make a principal deposit at the start of your investment period?")
# The .lower() here puts all entries in lowercase for comparison to sought value, so Yes isn't read as otherChar
        if answer1.lower() == "yes":
            while True:
                try:
# This while loop ensures that the input is a positive integer > 0.
                    Principal = float(input("How much was your principal?"))
                    if Principal < 0:
                        raise ValueError
                    break
                except ValueError:
                    print("Oh no! It seems you've entered a value less than 0. The principal MUST be a value greater than or equal to 0.")
        elif answer1.lower() == "no":
# We made a two-pronged 0 declaration in case user answered yes to principal q. and then entered 0. Smooths process for user.
             Principal = 0
# Accounting for otherChar
        elif answer1.lower() != "yes" or "no":
            raise ValueError
        break
    except ValueError:
        print("Unfortunately, this question only takes yes or no answers. Please enter yes or no.")


# Finding out the investment period interest rate
# While loop to account for values of interestRate that are not between 0 and 100.
while True:
    try:
        interestRate = float(input("What was your average interest rate percentage over the accrual period?"))
# Inclusivity is important, though uncommon!
        if interestRate < 0 or interestRate > 100:
            raise ValueError
        break
    except ValueError:
        print("Agh. The interest Rate percentage must be a number between 0% and 100%, but don't worry, we'll do all the converting for you.")

# This loop is to ensure that the number of years is an integer greater than 0.
while True:
    try:
        Years = int(input("Over the course of how many years did you accrue interest?"))
# Despite it seeming unnecessary, we include values such as 0 for number of years saved
##  because we want to give the user as much freedom with the program as possible.
        if Years <= 0:
            raise ValueError
        break
    except ValueError:
        print("No no no. Your investment has to last SOME amount of time. Give us a number greater than zero.")

# While loop to account for Y, N, and otherChar for declaration of deposit variables.
# Nested whiles because I want to avoid having user answer questions with null values if the're Not Applicable(skip)
while True:
    try:
        answer2 = input("Did you make regular deposits over the course of the investment?")
        if answer2.lower() == "yes":
            while True:
                try:
                    pmt = float(input("How much was each deposit?"))
                    if pmt <= 0:
                         raise ValueError
                    break
                except ValueError:
                    print("Invalid input. Amount of deposit must be a number greater than 0.")

                    # This loop is to ensure that the number of deposits is an integer greater than 0.
            while True:
                try:
                    n = int(input("How many times did you deposit annually?"))
                    if n <= 0:
                        raise ValueError
                    break
                except ValueError:
                    print("Invalid input. Number of annual deposit must be a whole number greater than 0.")
            P = Principal
            r = interestRate / 100
            t = Years
            investmentTotal = (P * ((1 + (r / n)) ** (n * t))) + (pmt * (((1 + (r / n)) ** (n * t) - 1) / (r / n)))

            print("The total value of your investment after ", t, " years of saving is approximately $", int(investmentTotal),
                  end=".", sep="")
# we set these variables if there were no deposits made so we can do the simple compound formula without deposits.
        elif answer2.lower() == "no":
            P = Principal
            r = interestRate / 100
            t = Years
            simpleTotal = P * (1 + r * t)
            print("The total value of your investment after ", Years, " years of saving is approximately $", int(simpleTotal),
                              end=".", sep="")
        elif answer2.lower() != "yes" or "no":
            raise ValueError
        break
    except ValueError:
        print("Please enter yes or no.")