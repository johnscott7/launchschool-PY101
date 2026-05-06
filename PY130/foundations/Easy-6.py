from functools import reduce

animals = ['dogs', 'cat', 'elephant', 'zebra', 'Madagascar']

def concatenator(element, accum):
    return element + accum

animal_word = reduce(concatenator, animals, '')

print(animal_word)
