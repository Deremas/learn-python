# Set
# A set is a collection which is unordered, unchangeable*, and unindexed. In Python sets are written with curly brackets.
# Creating a set
my_set = set()  # Empty set or
my_set = {}  # This creates an empty dictionary, not a set
print(my_set)  # Output: set() for the first case and {} for the second


# Note: Using {} creates an empty dictionary, not a set
my_set = {1, 2, 3}  # Set with integers
print(my_set)  # Output: {1, 2, 3}
# And using () creates an empty tuple, not a set
# print(my_set)  # Output: set()
my_set = {1, 2, 3, 'four', 'five'}  # Set with mixed data types
print(my_set)  # Output: {1, 2, 3, 'four', 'five'}
my_set = {1, 2, 3, (4, 5), 'six'}  # Set with nested tuple
print(my_set)  # Output: {1, 2, 3, (4, 5), 'six'}

courses = {'Math', 'Science', 'History', 'Art'}
print(courses)  # Output: {'Math', 'Science', 'History', 'Art

# About Unordering nature of sets for numbers and strings
numbers_set = {3, 1, 4, 2} 
print(numbers_set)  # Output: {1, 2, 3, 4} (the order may vary)
strings_set = {'banana', 'apple', 'cherry'}
print(strings_set)  # Output: {'apple', 'banana', 'cherry'} (the order may vary)

# Why is numbers not change their order in sets?
# The order of numbers in a set may appear to be sorted because of how Python internally manages sets, but it is not guaranteed. The order of elements in a set is determined by their hash values, and for small integers, the hash values are often the same as the integers themselves, which can give the appearance of being sorted. However, this is not a reliable behavior and should not be relied upon in practice.
#  Example:
my_set = {3, 1, 4, 2, 5, 6, 7, 8, 10946, 17711, 28657, 46368, 75025, 121393, 196418, 317811, 514229, 832040, 9, 10, 12, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765}
print(my_set)  # Output: {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12} (the order may vary)

# What is benefits of sets?
# Sets are useful for storing unique elements and performing operations like union, intersection, and difference.
#  Example:
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}
print(set_a.union(set_b))  # Output: {1, 2, 3, 4, 5, 6}
print(set_a.intersection(set_b))  # Output: {3, 4}
print(set_a.difference(set_b))  # Output: {1, 2}
print(set_b.difference(set_a))  # Output: {5, 6}

# set methods: add(), remove(), discard(), pop(), clear()
my_set = {1, 2, 3}
my_set.add(4)  # Add an element to the set
print(my_set)  # Output: {1, 2, 3, 4}
my_set.remove(2)  # Remove an element from the set (raises KeyError if the element is not found)
print(my_set)  # Output: {1, 3, 4}
my_set.discard(3)  # Remove an element from the set (does not raise an error if the element is not found)
print(my_set)  # Output: {1, 4}
my_set.pop()  # Remove and return an arbitrary element from the set
print(my_set)  # Output: {4} (the output may vary)
my_set.clear()  # Remove all elements from the set
print(my_set)  # Output: set()

# Does duplicates are allowed in sets?
# No, sets do not allow duplicate elements. If you try to add a duplicate element to a set, it will simply be ignored and the set will remain unchanged.
my_set = {1, 2, 3}
my_set.add(3)  # Attempt to add a duplicate element
print(my_set)  # Output: {1, 2, 3} (the duplicate element is ignored)