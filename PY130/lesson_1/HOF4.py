def reduce(callback, iterable, start):
    accum = start
    for item in iterable:
        accum = callback(item, accum)

    return accum


numbers = [10, 3, 5]
result = lambda number, accum: accum + number**2
print(reduce(result, numbers, 0)) # 134