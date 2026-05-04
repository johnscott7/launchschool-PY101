string_list = ['a', 'list', 'of', 'strings']

def capitalizer(words):
    for word in words:
        yield word.capitalize()

print(tuple(capitalizer(string_list)))