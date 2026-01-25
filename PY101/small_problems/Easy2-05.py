# Write a program that prompts the user for two positive numbers (floats), then
# prints the results of the following operations on those two numbers:
# addition, subtraction, product, quotient, floor quotient, remainder, and power
# Do not validate the input

# Example
# 2 and 4
# 6, -2, etc
# Each should be a separate print, not all in one go

# Data
# inputs will be assumed to be ints

# algorithm
# Receive the two inputs from the user
# print addition, subtraction, product, quotient, floor quotient, remainder, and power for the two numbers

print("Hi. I will be doing some math for you today.")
num1 = float(input("Input a number great than zero, please: "))
num2 = float(input("Input another number great than zero, please: "))
print(num1 + num2)
print(num1 - num2)
print(num1 * num2)
print(num1 / num2)
print(num1 // num2)
print(num1 % num2)
print(num1 ** num2)
