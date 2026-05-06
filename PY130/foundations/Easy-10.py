def user_speaks():
    while True:
        words = input("Say something! Or say 'stop': ")
        if words == 'stop':
            break
        yield words

for user_input in user_speaks():
    print(user_input)