# Tuples
# A tuple is a collection which is ordered and unchangeable. In Python tuples are written with round brackets.
my_tuple = (1, 2, 3)
# Creating a tuple
my_tuple = () # Empty tuple or
my_tuple = tuple() # Empty tuple

print(my_tuple)  # Output: ()
my_tuple = (1, 2, 3) # Tuple with integers
print(my_tuple)  # Output: (1, 2, 3)
my_tuple = (1, 2, 3, 'four', 'five') # Tuple with mixed data types
print(my_tuple)  # Output: (1, 2, 3, 'four', 'five')
my_tuple = (1, 2, 3, [4, 5], 'six') # Tuple with nested list
print(my_tuple)  # Output: (1, 2, 3, [4, 5], 'six')

# Tuple indexing and slicing
print(my_tuple[0])  # Output: 1


# Mutable vs Immutable
# Tuples are immutable, which means that once a tuple is created, its elements cannot be changed.
# However, if a tuple contains a mutable object like a list, the contents of that mutable object can be changed.
my_tuple = (1, 2, 3, [4, 5], 'six')
print(my_tuple)  # Output: (1, 2, 3, [4, 5], 'six')
my_tuple[3][0] = 'changed'  # Changing the first element of the nested list
print(my_tuple)  # Output: (1, 2, 3, ['changed', 5], 'six')
# my_tuple[1] = 'changed'  # This will raise a TypeError because tuples are immutable

# Tuple methods
# Tuples have only two built-in methods: count() and index()
my_tuple = (1, 2, 3, 2, 4)
print(my_tuple.count(2))  # Output: 2 (counts the number of occurrences of 2 in the tuple)
print(my_tuple.index(3))  # Output: 2 (returns the index of the first occurrence of 3 in the tuple)