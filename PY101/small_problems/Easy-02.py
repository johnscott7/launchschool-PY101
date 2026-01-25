# Process
# Print only odd numbers from 1 to 99, inclusive, with each number on a separate line
# will need upper end to be 100 then

# E
# 1
# 3
# 5
# 99

# D
# no inputs here
# outputs are integers, not sure if \n will be needed or print can handle that

# A
# Could use for num in range, with a check for even/odd using modulus
# Bonus question asks for iterating over only odd numbers
# Could achieve this with a while loop using modulus, adding to the index
# Or could simply begin with 1, add a two step, stop when we reach 100

# C
for num in range(1, 100, 2):
    print(num)
