# Author: Justice Smith
# Course No.: COP2930
# Assignment Title: Individual Programming Ass't 1
# Date: 1/12/2020
# Brief Description: Speed Limit Conversion

while True: # Loop to give clear feedback on invalid input
    try:
        MPH = float(input("What is your speed in miles per hour?"))
        if MPH <0 or MPH > 100: # input parameters
            raise ValueError
        break
    except ValueError:
        print("Invalid Input. The speed must be between 0 and 100.")
KPH = MPH*1.60934 # Conversion formula

print("Your converted speed in kilometers per hour is", KPH, end = ".\n")
print("Wow!! That's fast!")
            
        
