string_list = ['a', 'longer', 'list', 'of', 'strings']


def capitalizer(words):
    for word in words:
        if len(word) > 5:
            yield word.capitalize()

print(tuple(capitalizer(string_list)))