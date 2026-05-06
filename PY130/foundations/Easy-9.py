def my_counter(max_num):
    num = 1
    while num <= max_num:
        yield num
        num += 1

my_generator = my_counter(5)
print(list(my_generator))