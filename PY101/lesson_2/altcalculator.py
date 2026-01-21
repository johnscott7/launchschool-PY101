# Ask the user for the first number.
# Ask the user for the second number.
# Ask the user to choose an arithmetic operation.
# Perform the operation on the two numbers.
# Print the result to the terminal.

def prompt(message):
    return input(f'{message} \n ==> ')

print('Welcome to Calculator!')

num1 = int(prompt('Please input a number.'))
num2 = int(prompt('Please input another number.'))
operator = int(
    input(
        'Please specify an arithmetic operator using the number'
        ' 1, 2, 3, or 4 based on the following:\n'
        '1 for Add, 2 for Subtract, 3 for Multiply, 4 for Divide\n > '))

while invalid_number(number1):
    print("Hmm.. that doesn't look like a valid number")

while operator > 4 or operator < 1:
    operator = int
    (input(
        'You did not enter a number between 1-4. Please try again.\n > '))
if operator == 1: # 1 represents addition
    output = num1 + num2
elif operator == 2: # 2 represents subtraction
    output = num1 - num2
elif operator == 3: # 3 represents multiplication
    output = num1 * num2
else:
    if num2 == 0:
        output = (
            'an attempted division by zero. '
            'You have created a black hole in the universe. Goodbye.'
        )
    else:
        output = num1 / num2

print(f'The result is {output}')
