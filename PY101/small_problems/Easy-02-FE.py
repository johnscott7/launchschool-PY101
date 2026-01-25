# Process
# Print only odd numbers from 1 to 99, inclusive, with each number on a separate line
# will need upper end to be 100 then

# Further exploration:
# Add a way for the user to specify the starting and ending values of the odd numbers printed
def odd_nums_in_range(start, stop):
    if start % 2 == 0:
        start = start + 1
    for num in range(start, stop + 1, 2):
        print(num)

odd_nums_in_range(4, 99)
