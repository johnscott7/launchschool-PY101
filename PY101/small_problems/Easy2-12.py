# P
# Write a function that takes a number as an argument, and, if the number is positive, returns the negative
# If the argument is a negative number, return it as-is

# E
# (5) => -5
# (-3) => -3
# negative(0) => 0)

# D
# Assume the input will be an integer

# A
# Receive any integer as an input
# Detect absolute value (or just convert to absolute value regardless)
# Multiply by -1 and return value

# C
def negative(any_num):
    return (abs(any_num) * -1)

print(negative(5) == -5)      # True
print(negative(-3) == -3)     # True
print(negative(0) == 0)       # True