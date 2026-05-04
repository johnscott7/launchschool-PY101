def describe_pet(animal_type, /, *, name = ' '):
    print(f'I am a {animal_type} and my name is {name}.')

describe_pet("dog", name = "Lucy")