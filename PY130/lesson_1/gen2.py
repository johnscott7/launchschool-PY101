def reciprocal_up_to(max_count):
    count = 1
    while count <= max_count:
        yield 1/count
        count +=1

reciprocator = reciprocal_up_to(7)
for value in reciprocator:
    print(value)