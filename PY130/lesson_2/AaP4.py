def calculate_average(*args):
    total = 0
    for arg in args:
        total += arg
    return total / len(args) if args else None

print(calculate_average(1, 2, 3, 4, 5, 7, 10))