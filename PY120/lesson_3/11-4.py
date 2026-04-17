num1 = int(input('Please enter a number: '))
if num1 < 0:
    raise ValueError('Number cannot be negative.')
print(f'Your number is {num1}.')