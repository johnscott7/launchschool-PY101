def join_or(num_list, separator=', ', final_connector='or'):
    if len(num_list) == 0:
        return ""
    if len(num_list) == 1:
        return str(num_list[0])
    if len(num_list) == 2:
        return f"{num_list[0]} {final_connector} {num_list[1]}"
    full_string = ''
    for num in num_list[0:-1]:
        full_string += str(num)
        full_string += separator
    full_string += 'or '
    full_string += str(num_list[-1])
    return full_string

print(join_or([1, 2]))
print(join_or([1, 2, 3]))
print(join_or([1, 2, 3], "; "))
print(join_or([1, 2, 3], ", ", "and"))