# Write a function that returns the next to last word in the string argument.
# Words are any sequence of non-blank characters
# Assume the input string will always contain at least two words

# Example
# 'it is snowing outside' -> return snowing

# Data
# input will be a string of multiple words

# A
# There is a split method that could theoretically be used here 
# -2 could be used, but that is second to last character

# Code
def penultimate(any_words):
    separated = any_words.split()
    return separated[-2]

# These examples should print True
print(penultimate("last word") == "last")
print(penultimate("Launch School is great!") == "is")