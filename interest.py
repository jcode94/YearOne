# Author: Justice Smith
# Course No.: COP2930
# Date: 1/12/2020
# Assignment Title: Individual Programming Ass't 1
# Brief Description: Simple interest calculator

print("Hello! Today we're going to calculate for compound interest earned.")  # Manners matter

#This checks to skip question on principle if they didn't have one.
answer1 = input("Did you make regular deposits over the course of the investment?")
if answer1.lower() == "yes":
        # First loop is to ensure that the principal is a positive, real number.
        while True:
            try:
                Principal = int(input("How much was your principal?"))
            if Principal < 0:
                raise ValueError
            break
        except ValueError:
        print("Invalid input. Principal must be 0 or more.")  # Here is that clarification.
    else:
    if answer1 == "no":
        Principal = 0
    else:
    print("Please enter yes or no.")

# This loop is to ensure that we get a valid percentage value.
while True:
    try:
        interestRate = float(input("What was your average interest rate percentage over the accrual period?"))
    if interestRate < 0 or interestRate > 100:
        raise ValueError
    break
except ValueError:
print("Invalid input. Interest Rate percentage must be between 0% and 100%.")

# This loop is to ensure that the number of years is an integer greater than 0.
while True:
    try:
        Years = int(input("Over the course of how many years did you accrue interest?"))
        if Years <= 0:
            raise ValueError
        break
    except ValueError:
        print("Invalid input. Years of compounding must be greater than 0.")

#This checks to skip 2 questions if they're not necessary
        answer2= input("Did you make regular deposits over the course of the investment?")
        if answer2 == "yes":
while True:
    try:
        pmt = int(input("How much did you deposit monthly?"))
        if pmt <= 0:
            raise ValueError
        break
    except ValueError:
        print("Invalid input. Amount of deposit must be greater than 0.")

            # This loop is to ensure that the number of deposits is an integer greater than 0.
            while True:
                try:
                    n = int(input("How many times did you deposit annually?"))
                    if n <= 0:
                        raise ValueError
                    break
                except ValueError:
                    print("Invalid input. Number of annual deposit must be greater than 0.")
        elif answer2 == "no":
            pmt = 0
            n = 0
        else:
            print("Please enter yes or no.")


# Variable Declaration/Assignment
P = Principal
r = interestRate/100
t = Years

# Equations
investmentTotal = (P * ((1+(r/n)) ** (n * t))) + (pmt * (((1 + (r / n) ** (nt) - 1) / (r / n)) ** (1 + (r / n))))


print("The total amount saved after ", t, " years of saving is $", int(investmentTotal), end=".", sep="")
