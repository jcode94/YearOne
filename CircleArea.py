# Author: Justice Smith
# Date: 1/12/2020
# Brief Description: User form to calculate area of circle based on radius

# Variable input 
radius = int(input("What is the radius of your circle?\n"))
name = input("What is your name?\n")

# Variable declaration
PI = 3.14159
area = PI*radius*radius

# Calculated result
print("Congratulations,",name, ", the area of your circle is",area)
