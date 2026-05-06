data = [['x', 'y', 'z'], ['a', 'b', 'c'], [1, 2, 3]]

my_generator = (element for sublist in data for element in sublist)

print(list(my_generator))
