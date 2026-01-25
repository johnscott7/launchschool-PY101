# P
# Build a program that displays when the user will retire and how many years she has to work until retirement.

# E
# input 30 and 70, output 40 years

# D
# User age and targeted retirement age should be user inputs
# Both will be strings, need to be converted to int

# A
# Ask user for their age, convert to int
# Ask user for their desired retirement age, convert to int
# Subtract the difference 
# Obtain the current year using the datetime module
# Add 

# C
from datetime import datetime
user_age = int(input("How old are you, friend? "))
retirement_age = int(input("What age do you expect to retire? "))
years_left = retirement_age - user_age
current_year = datetime.now().year
retirement_year = current_year + (years_left)
print(f"It's {current_year}. You will retire in {retirement_year}."
      f" You have only {years_left} years of work to go! Not long now.")