animals = ['dogs', 'cat', None, 'elephant', None, 'zebra']

def not_none_values(value):
    if value != None:
        return True
    return False

only_animals = filter(not_none_values, animals)
print(list(only_animals))