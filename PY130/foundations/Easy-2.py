def even(num):
    return num % 2 == 0

numbers = [1, 3, 5, 7, 11, 13]

even_numbers = filter(even, numbers)
print(list(even_numbers))