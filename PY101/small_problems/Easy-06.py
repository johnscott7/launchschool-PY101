# P
# Ask for an input from the user for an integer greater than zero
# Ask the user whether they want to calculate sum or product for all numbers between 1, and their chosen integer

# E
# Input1 = 7, Input2 = product, result = 5040
# Input1 = 1, Input2 = sum, result = 1
# Input1 = 7, Input2 = sum, result = 28

# D
# Input1 will be a string, convert to integer
# Input2 should be given as either an s or a p, s for sum, p for product
# Will need to explain that to the user, and convert input string to integer

# A
# Ask user for integer above 0
# Validate it is above zero, re-ask if it is not (optional for this problem)
# Ask user for sum or product
# validate it is 's' or 'p', re-ask if not (optional for this problem)
# if s, add all numbers together 
# if p, multiply all numbers together (inclusive of 1)
# Want to think about the addition/multiplication steps separately from the iteration steps, not sure how to separate these
# print the output (this is actually not specified in the program requirements). 

# C
print("Hi. I am your personal calculator.")
print("I can calculate either the sum or product of "
      "all numbers between 1 and your own specified integer.")
while True:
    start_int = int(input("Please input an integer greater than zero: "))
    if start_int > 0:
        break
    print("Please try again. Enter a number greater than zero.")
while True:
    operation_type = input("Type 's' to calculate "
                           "sum, or 'p' to calculate product: ")
    if operation_type in ('s', 'p'):
        break
    print("Pleae try that input again. Enter either 's' or 'p'.")
if operation_type == 's':
    sum_result = 0
    for i in range(1, start_int + 1):
        sum_result += i
    print(f'The sum of the integers between 1 and {start_int} is {sum_result}.')
if operation_type == 'p':
    prod_result = 1
    for i in range(1, start_int + 1):
        prod_result *= i
    print(f'The product of the integers between 1 and {start_int} is {prod_result}.')