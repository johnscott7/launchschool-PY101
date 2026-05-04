string_list = ['a', 'list', 'of', 'strings']

capitalized_string_list = (word.capitalize() for word in string_list)

print(tuple(capitalized_string_list))