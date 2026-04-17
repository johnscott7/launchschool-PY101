numbers = [1, 2, 3, 4, 5]

def sixth_element(num_list):
    if len(num_list) >= 6:
        return num_list[5]
    else:
        return None

def safe_sixth_element(num_list):
    try:
        return num_list[5]
    except IndexError:
        return None

print(safe_sixth_element(numbers))
print(sixth_element(numbers))