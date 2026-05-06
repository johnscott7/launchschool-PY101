def build_profile(first_name, last_name, **kwargs):
    final_dict = {'first_name': first_name, 'last_name': last_name}
    for key, value in kwargs.items():
        final_dict[key] = value
    return final_dict

print(build_profile("Max", "Hawkins", location="San Francisco", field="Software Engineering"))
# {'first_name': 'Max', 'last_name': 'Hawkins', 'location': 'San Francisco', 'field': 'Software Engineering'}