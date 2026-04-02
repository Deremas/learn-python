# Dictionary
# A dictionary is a collection which is unordered, changeable and indexed. In Python dictionaries are written with curly brackets, and they have keys and values.
# Creating a dictionary
my_dict = {}  # Empty dictionary or
my_dict = dict()  # Empty dictionary
print(my_dict)  # Output: {}
my_dict = {'name': 'Alice', 'age': 30, 'city': 'New York'}  # Dictionary with string keys and values
print(my_dict)  # Output: {'name': 'Alice', 'age': 30, 'city': 'New York'}
my_dict = {1: 'one', 2: 'two', 3: 'three'}  # Dictionary with integer keys and string values
print(my_dict)  # Output: {1: 'one', 2: 'two', 3: 'three'}

# Accessing the values of dic
print(my_dict[1])  # Output: 'one' (accessing value using key)
print(my_dict.get(2))  # Output: 'two' (accessing value using get() method)

# Adding and updating key-value pairs
my_dict[4] = 'four'  # Adding a new key-value pair
print(my_dict)  # Output: {1: 'one', 2: 'two', 3: 'three', 4: 'four'}
my_dict[2] = 'TWO'  # Updating the value of an existing key
print(my_dict)  # Output: {1: 'one', 2: 'TWO', 3: 'three', 4: 'four'}
print(my_dict.get(5, 'Key not found'))  # Output: 'Key not found' (using get() with a default value)

# Update with update() method
my_dict.update({5: 'five', 6: 'six', 2: 'TWO updated', 8: 'eight'})  # Updating multiple key-value pairs
print(my_dict)  # Output: {1: 'one', 2: 'TWO updated', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 8: 'eight'}

# Update existing keys with update() method
my_dict.update({2: 'TWO updated again', 3: 'THREE updated'})  # Updating existing key-value pairs
print(my_dict)  # Output: {1: 'one', 2: 'TWO updated again', 3: 'THREE updated', 4: 'four', 5: 'five', 6: 'six', 8: 'eight'}

# How can i change the keys of a dictionary?
# You cannot change the keys of a dictionary directly, but you can achieve this by creating a new dictionary with the desired keys and copying the values from the old dictionary.
old_dict = {'name': 'Alice', 'age': 30, 'city': 'New York'}
new_dict = {'full_name': old_dict['name'], 'age': old_dict['age'], 'location': old_dict['city']}
print(new_dict)  # Output: {'full_name': 'Alice', 'age': 30, 'location': 'New York'}

print(new_dict.keys())  # Output: dict_keys(['full_name', 'age', 'location']) (returns a view object of the keys in the dictionary)
print(new_dict.values())  # Output: dict_values(['Alice', 30, 'New York']) (returns a view object of the values in the dictionary)
print(new_dict.items())  # Output: dict_items([('full_name', 'Alice'), ('age', 30), ('location', 'New York')]) (returns a view object of the key-value pairs in the dictionary)

for key in new_dict:
    print(key)  # Output: full_name, age, location (iterating over the keys in the dictionary)
    
# for key, value in new_dict:
#     print(key, value)  # This will raise a ValueError because iterating over a dictionary only gives you the keys, not the key-value pairs. You should use new_dict.items() to iterate over key-value pairs.
for key, value in new_dict.items():
    print(key, value)