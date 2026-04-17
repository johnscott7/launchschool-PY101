try:
    num1 = int(input('Please enter a number: '))
    num2 = int(input('Please enter a second number: '))
    result = num1 / num2
except ValueError:
    print('That was not a number.')
except ZeroDivisionError:
    print('Oops. You cannot divide by zero.')
else:
    print(f'No exceptions raised. Your number is {result}.')
finally:
    print('End of program.')