list1 = [1, 2, 3, 5, 0, 7, 'dog']
def element_inverter(lst):
    new_list = []
    for num in lst:
        try:
            new_num = 1 / num
        except (ZeroDivisionError, ValueError, TypeError):
            new_num = None
        new_list.append(new_num)
    return new_list

print(element_inverter(list1))