# P
# A function that takes two strings as arguments, determines length of the two strings, then returns the result of
# Concatenation of the shorter string, the longer string, and the shorter string again.
# Assume the strings are different lengths.

# Example
# str1 = 'dog, str2 = 'elephant', output = 14
# str1 = 'hi', str2 = 'hello', output = 9

# Data
# Two inputs, both strings
# Output will be length of a string, so an integer

# A
# 
# Calculate length of both strings
# Compare the two lengths to determine which string is shorter
# Calculate (2 * shorter string length) + (longer string length)
# Return this length
# Do not worry about scenario where they are the same length for this problem

# C
def str_concat_length(string_1, string_2):
    if len(string_1) > len(string_2):
        long_string = string_1
        short_string = string_2
        return short_string+long_string+short_string
    else:
        long_string = string_2
        short_string = string_1
        return short_string+long_string+short_string

print(str_concat_length('hi', 'hello'))
print(str_concat_length('dog', 'elephant'))