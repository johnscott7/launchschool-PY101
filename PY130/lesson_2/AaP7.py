def register(username, /, age, *, password):
    return {'username': username, 'age': age, 'password': password}


print(register('entry1', 24, password = 'dogface123$'))