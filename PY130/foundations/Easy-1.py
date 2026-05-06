def square(x):
    return x * x

numbers = [1, 3, 5, 7, 11, 13]

my_list = map(square, numbers)
print(list(my_list))
