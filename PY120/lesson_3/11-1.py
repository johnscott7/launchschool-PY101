num1 = input('Please enter a number: ')
try:
    num1 = int(num1)
except ValueError:
    print('That was not a number.')
    exit()
num2 = input('Please enter a second number: ')
try:
    num2 = int(num2)
except ValueError:
    print('That was not a number.')
    exit()

try:
    result = num1 / num2
except ZeroDivisionError:
    print('Oops. You cannot divide by zero.')
else:
    print(f'Your number is {result}.')