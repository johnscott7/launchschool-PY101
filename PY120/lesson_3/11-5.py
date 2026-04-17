class NegativeNumberError(ValueError):
    def __init__(self, message="Negative numbers are not allowed"):
        super().__init__(message)

num1 = int(input('Please enter a number: '))
if num1 < 0:
    raise NegativeNumberError()
print(f'Your number is {num1}.')