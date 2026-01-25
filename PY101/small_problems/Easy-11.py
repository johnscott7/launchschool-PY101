# P
# Write a function that determines and returns the UTF-16 string value of a string passed in a n argument
# The UTF-16 string value is the sum of the UTF-16 values of every character in the string
# ord can be used to determine the UTF-16 value of a character

# E
# 'Four score' should give 984
# '' is 0
# 'a' is 97

# D
# input will be a string
# output will be an integer

# A
# Receive a string passed into the function as an argument
# Either separate the string into multiple components, or, more simply,
# iterate through the characters in the string, calculating ord() on each chracter and passing that to a new variable
# Need to determine whether ord('a') needs to be converted to an int or can be added
# RETURN the variable (not print)

# Code
def utf16_value(string):
    total_value = 0
    for char in string:
        total_value += ord(char)
    return total_value


# These examples should all print True
print(utf16_value('Four score') == 984)
print(utf16_value('Launch School') == 1251)
print(utf16_value('a') == 97)
print(utf16_value('') == 0)

# The next three lines demonstrate that the code
# works with non-ASCII characters from the UTF-16
# character set.
OMEGA = "\u03A9"              # UTF-16 character 'Ω' (omega)
print(utf16_value(OMEGA) == 937)
print(utf16_value(OMEGA + OMEGA + OMEGA) == 2811)