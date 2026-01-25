# Write a function that returns a list containing every other element of a list that is passed in as an argument.
# The values in the returned list should be those values in the 1st/3rd/5th/7th etc

# Example
# [2, 3, 4, 5, 6]) == [2, 4, 6]) 

# Data
# Input will be a list
# The function parameter will be a single value, and that value will be a list


def oddities(lst):
    full_list = []
    for i in range(0, len(lst)):
        if i % 2 == 0:
            full_list.append(lst[i])
    return full_list

print(oddities([2, 3, 4, 5, 6]) == [2, 4, 6])  # True
print(oddities([1, 2, 3, 4]) == [1, 3])        # True
print(oddities(["abc", "def"]) == ['abc'])     # True
print(oddities([123]) == [123])                # True
print(oddities([]) == [])                      # True