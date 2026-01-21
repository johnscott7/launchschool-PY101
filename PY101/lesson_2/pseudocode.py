'''
1.  a function that returns the sum of two numbers
Pseudocode:
Assign a number to a variable
Assign another number to a variable
Define the function name
    return variable1 x variable2

Formal pseudocode:
START
SET variable1 = integer
SET variable2 = integer
SET function1
    return variable1 * variable 2

2. A function that takes a list of strings, 
and returns a string that is all those strings concatenated together

START
READ list1
SET new_variable = ''
FOR str_items in list1
    new_variable = new_variable + str_items
PRINT new_variable


3. A function that takes a list of integers, and returns a new list with every other element from the original list,
starting with the first element. For instance:
every_other([1,4,7,2,5]) # => [1,7,5]

Read a list of integers and assign to a variable
Create an empty list and assign a variable to it
Create a function 
Iterate through the collection using an index
    Use the even/odd divison rule to determine whether the element is added to the original list
    return the final list

START
# input: og_list (a list of integers)
SET new_list = []
# function: every_other
For num in range(0, len(og_list))
    IF num is even
        Add og_list[num] to new_list
return new_list
# execute every_other()
END




4. A function that determines the index of the 3rd occurence of a given character in a string.
For instance, if the given character is 'x' and the string is 'axbxcdxex', 
the function should return 6. If the given character does not occur at least 3 times, return None.

START
# input: some_string (a string), target_char(a character)
# function: third_rep
SET count = 0
FOR index from 0 to length of some_string
    IF some_string[index] == target_char
        Add one to the count
        IF count == three
            RETURN index
RETURN none
END



5. A function that takes two lists of numbers and returns the result of merging the lists. 
The elements of the first list should become the elements at the even indexes of the returned list,
while the elments of the second list should become the elements at the odd indexes. For instance:
    merge([1, 2, 3], [4, 5, 6]) # => [1, 4, 2, 5, 3, 6]

START
# Input: list_1 (a list of numbers), list_2 (a different list of numbers)
# function alt_num_list
SET new_list = [None] * ((len(list_1) + len(list_2)))
For index from 0 to len(list_1)-1
    SET moving_index = index * 2
    SET new_list[moving_index] = list_1[index]
For index from 0 to len(list_2)-1
    SET moving_index = (index * 2) + 1
    SET new_list[moving_index] = list_2[index]
RETURN new_list
END

'''