word = 'smashmouth'

my_generator = (element for element in word[::-1])
print(list(my_generator))