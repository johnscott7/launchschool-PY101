try:
    num1 = int(input('Please enter a number: '))
    num2 = int(input('Please enter a second number: '))
    result = num1 / num2
except (ZeroDivisionError, ValueError) as e:
    print(e)
else:
    print(f'The result is: {result}')
finally:
    print('End of the program.')