def find_person(**kwargs):
    for name, profession in kwargs.items():
        if name == "Antonina":
            print(f'{name} is a {profession}')
            break
    else:
        print(f'Antonina not found.')

find_person(Jack = 'engineer', Anthony = 'blacksmith', Darryl = 'manager', Antonina = 'developer')
