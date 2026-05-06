def display_info(data, /, reverse=False, uppercase=False):
    if reverse == True:
            data = data[::-1]
    if uppercase == True:
            data = data.upper()
    return data

print(display_info("Launch", reverse=True)) # hcnuaL
print(display_info("School", uppercase=True)) # SCHOOL
print(display_info("cat", uppercase=True, reverse=True)) # TAC