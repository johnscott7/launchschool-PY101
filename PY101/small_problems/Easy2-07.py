# Write a function xor that takes two arguments, returns True if exactly one of its arguments is truthy, otherwise False

# xor will operator as the so-called exclusive or (one of the two, not both)
# 5 and 0 => False
# 5 or 0 => True
# 5 xor 0 => True

# Examples
# Input True, False. Output True
# Inputs False, True. Output True
# Inputs True, True. Output False
# Input False, False. Output False

# Data
# Input type can be any, need to identify truthiness

# Algorithm
# Will need to manually evaluate all four scenarios (TF, TT, FT, FF) and return True/False for each

def xor(value1, value2):
    if value1:
        if value2:
            return False
        return True
    if not value1:
        if value2:
            return True
        return False


print(xor(5, 0) == True)
print(xor(False, True) == True)
print(xor(1, 1) == False)
print(xor(True, True) == False)