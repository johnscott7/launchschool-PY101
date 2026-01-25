def sum_of_multiples(target, factors):
    multiples = []

    if not factors:
        factors = [3, 5]

    for factor in factors:
        current_multiple = factor

        while current_multiple < target:
            multiples.append(current_multiple)
            current_multiple += factor

    return sum(set(multiples))


# examples
print(sum_of_multiples(20, [3, 5]))  # 78
print(sum_of_multiples(20, [3]))     # 63
print(sum_of_multiples(20, [5]))     # 30
print(sum_of_multiples(20, []))      # 78
print(sum_of_multiples(1, []))       # 0
print(sum_of_multiples(20, [19]))    # 19