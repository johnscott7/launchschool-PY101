# P
# Write a function that takes a year (any int greater than 0) and returns True if the year is a leap year, or False if not.
# Use the following simplified rules for calculating a leap year
# if divisible by 400, leap year
# if divisible by 100 but not 400, not leap year
# if divisible by 4 but not 100, leap year
# all other years not leap year

# E
# is_leap_year(4) #True
# is_leap_year(1000) #False)

# D input will be an int > 0
# output will be bool

# A
# functino should receive a year (int > 0)
# Calculate if int / 400, if yes, return True
# If not divisible by 400, calculate if divisibule by 100, if yes, return False
# If not divisible by 100, calculate if divisible by 4, if yes, return True
# Otherwise, return False

# Code
def is_leap_year(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False

print(is_leap_year(1) == False)
print(is_leap_year(2) == False)
print(is_leap_year(3) == False)
print(is_leap_year(4) == True)
print(is_leap_year(1000) == False)
print(is_leap_year(1100) == False)
print(is_leap_year(1200) == True)
print(is_leap_year(1300) == False)
print(is_leap_year(1751) == False)
print(is_leap_year(1752) == True)
print(is_leap_year(1753) == False)
print(is_leap_year(1800) == False)
print(is_leap_year(1900) == False)
print(is_leap_year(2000) == True)
print(is_leap_year(2023) == False)
print(is_leap_year(2024) == True)
print(is_leap_year(2025) == False)