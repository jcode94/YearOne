# Justice Smith
# 1.17.2020
# Number of pictures storeable

# User Input
size = int(input("How much storage space does your thumb drive have, gigabytes?\n"))
length = int(input("What is the length of each picture, in pixels?\n"))
width = int(input("What is the width of each picture, in pixels?\n"))

# calculation
expandedSize = size*1000000000
pictureTotal = (expandedSize/(3*(length*width)))

# User Output
print("The total number of pictures that you can store on your thumb drive is", int(pictureTotal))
