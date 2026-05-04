string_list = ['a', 'longer', 'list', 'of', 'strings']

capitalized_string_list = (word.capitalize() for word in string_list if len(word) > 5)

print(tuple(capitalized_string_list))