'''
def double_numbers(numbers):
    for num in numbers:
        num *= 2 
    return numbers
'''
# Fix the above code 


def double_numbers(numbers):
    for i in range(0, (len(numbers))):
        numbers[i] = numbers[i] * 2 
    return numbers

my_list = [3, 6, 9, 12, 15]
result = double_numbers(my_list)
print(result)

# As a general rule, 'For X in Y' should only be used for read-access to elements, not write-access to the container. 