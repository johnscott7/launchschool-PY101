# P
# Write a program that asks a user for their name, then greets the user
# If the user appends a ! to their name, the computer will yell the greeting

# E
# input = John, output is Hi John.
# input is Jack!, output is HI JACK!

# D
# input is a string
# output is a string

# A
# receive user input and assign to variable
# check whether input ends with a !
# print a lowercase response if not
# print an uppercase response if yes

# Code
user_name = input("Hi, what is your name? ")
if user_name.endswith('!'):
    print(f"HI, {user_name.upper()}")
else:
    print(f"Hi, {user_name}.")