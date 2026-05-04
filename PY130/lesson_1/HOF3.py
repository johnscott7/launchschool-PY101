def reduce(callback, iterable, value):
    for i in range(len(iterable)):
        value = callback(iterable[i], value)
    return value

'''
numbers = [10, 3, 5]
product = lambda number, accum: accum * number
print(reduce(product, numbers, 2))     # 300

First pass: number wil be 10, accum will be 2 (from reduce)
Second invocation of product: number will be 3, accum will be 20
Third invocation: number will be 60, accum will be 5

'''
numbers = (1, 2, 4, 8, 16)
total = lambda number, accum: accum + number
print(reduce(total, numbers, 0))        # 31

numbers = [10, 3, 5]
product = lambda number, accum: accum * number
print(reduce(product, numbers, 2))      # 300

colors = ['red', 'orange', 'yellow', 'green',
          'blue', 'indigo', 'violet']
rainbow = lambda color, accum: accum + color[0].upper()
print(reduce(rainbow, colors, ''))      # ROYGBIV