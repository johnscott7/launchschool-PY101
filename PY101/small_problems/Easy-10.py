# P
# Write a function computing the sum of all numbers between 1 and some other number, but
# including only numbers that are multiples of 3 or 5

# E
# input is 20, output is 98
 # (3 + 5 + 6 + 9 + 10 + 12 + 15 + 18 + 20)

# D
# input will be a single integer
# output will also be an integer, a summed calculation from many integers

# A
# Define the range of values from 1 to specified integers
# Calculate all multiples of 3 in this range
# Calculate all multiples of 5 in this range
# Pass to a set to eliminate duplicates
# Sum the set

# Code
def multisum(num):
    list_of_nums = []
    for i in range(1, i + 1):
        if i % 3 == 0:
            list_of_nums.append(i)
        if i % 5 == 0:
            list_of_nums.append(i)
    return sum(set(list_of_nums))


# These examples should all print True
print(multisum(10) == 33)
print(multisum(5) == 8)
print(multisum(10) == 33)
print(multisum(1000) == 234168)