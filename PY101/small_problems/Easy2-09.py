# P
# Build a program that randomly generates and prints Teddy's age. 
# To get the age, you should generate a random number between 200 and 100, inclusive.

# E
# Teddy is 69 years old!

# D
# no inputs here at all

# A
# import the random module to generate a random int
# it's that simple

# C

import random
teddy_age = random.randint(20, 100)
print(f'Teddy, you are {teddy_age} years old! '
      'Congratulations buddy, enjoy your day.')