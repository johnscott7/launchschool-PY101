# Process
# Ask the user for two inputs: a length and a width, in meters.
# Print the room's areas in both square meters and square feet
# Note 1 sq m = 10.7639 sq ft

# E
# l = 5, w = 10, area = 50 m
# l = 0, w = 10, area = 0 m

# D
# input1 and input2 come from the user and will be strings, must be converted
# Output will be float

# A
# Ask user for and receive inputs (Need to be sure to convert to floats)
# calculate the area ( l x w)
# convert the area to sq ft and assign this to a separate variable ( area * 10.7639)
# print the area in both units

# Code
print("Hi. I can calculate the area of your room for you. Please input the following information.")
length = float(input("What is the length of your room, in meters? "))
width = float(input("What is the width of your room, in meters? "))
area = length * width
area_ft = area * 10.7639
print(f"The area of your room is {area:.2f} square meters, and {area_ft:.2f} square feet.")