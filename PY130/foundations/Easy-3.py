numbers = [1, 3, 5, 7, 11, 13, 17]
total = lambda number, accum: accum + number

def reduce(sum, numbers, start):
    accum = start
    for item in numbers:
        accum = sum(item, accum)
    
    return accum

print(reduce(total, numbers, 0))