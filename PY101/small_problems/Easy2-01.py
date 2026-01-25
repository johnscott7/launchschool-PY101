# P
# Create a fucntion that takes two arguments: one list, one dictionary
# The list will contain two or more elements that combine to make a person's name
# The dictionary will contain two keys, 'title' and 'occupation', and the appropriate values

# Example
'''
greeting = greetings(
    ["John", "Q", "Doe"],
    {"title": "Master", "occupation": "Plumber"},
)
print(greeting)
# Hello, John Q Doe! Nice to have a Master Plumber around.
'''

# D
# input1 will be a list, it will have at least two strings, if not more
# input2 will be a dict, it  will have two key-value pairs, one for title and one for occupation

# A
# Create a function with two parametes
# Concatenate the string from the first parameter
# Extract the two values from the dictionary
# return the greeting using the concatenated string, and the two values from the dictionary

# Code

def greetings(name_list, job_dict):
    full_name = ''
    for name in name_list:
        full_name += name + ' '
    return (f"Hi {full_name.strip()}! Nice to have a {job_dict['title']} {job_dict['occupation']} around.")

print(greetings(
    ["John", "Q", "Doe"],
    {"title": "Master", "occupation": "Plumber"},
))
# Hello, John Q Doe! Nice to have a Master Plumber around.

# NOTE:
# The much easier solution to this is to use the string method .join
# That would look like this:
'''
def greetings(name_list, job_dict):
    full_name = " ".join(name_list)
    return (f"Hi {full_name}! Nice to have a {job_dict['title']} {job_dict['occupation']} around."
    )
'''