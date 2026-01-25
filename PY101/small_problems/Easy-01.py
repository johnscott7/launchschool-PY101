# Process
# Write a function that takes one integer and returns True if the absolute value is odd, False otherwise
# Input : an integer
# Output: True or False

# Example
# input 4, output False
# input 0, output False
# input -22, output False
# input 21, output True

# Data Structure
# Argument : int (can be negative)
# Return: bool

# Algorithm
# get absolute value of the integer
# check if its odd using modulus
# Return True or False

# Code

test_int = 42

def is_it_odd(test_int):
    if isinstance(test_int, int):
        abs(test_int)
        if test_int % 2 == 1:
            return True
        else:
            return False
    else:
        return False
    
print(is_it_odd(42))
print(is_it_odd(0))
print(is_it_odd(-21))
print(is_it_odd(7.7))
print(is_it_odd('dog'))
