# P
# Write a function that takes a non-empty string argument and returns the middle character(s) of the string. 
# If the string has an odd length, return exactly one character.
# IF the string has an even length, return two characters.

# E
# 'I Love Python!!!' => "Py"

# D
# Input will be a string

# A
# Receive string input as argument passed to function
# Evaluate length of string
# If odd, find the central character of string
# If even, find the two central-most characters of the string
# Return the selected character(s)

# C
def center_of(string_of_words):
    midpoint = len(string_of_words) // 2
    if len(string_of_words) % 2 == 0:       # Even
        near_mid = len(string_of_words) // 2
        return string_of_words[midpoint - 1:midpoint +1]
    else: # odd
        return string_of_words[midpoint]

print(center_of('I Love Python!!!') == "Py")    # True
print(center_of('Launch School') == " ")        # True
print(center_of('Launchschool') == "hs")        # True
print(center_of('Launch') == "un")              # True
print(center_of('Launch School is #1') == "h")  # True
print(center_of('x') == "x")                    # True