# Loops

# for loop
# is a common convention for a variable that is used as an index in a loop, but it can be any valid variable name. In this case, we are using i as the loop variable that takes on the values from 0 to 4 (inclusive) in each iteration of the loop.
for i in range(5):
    print(i)

# for loop with step value
# _ is a common convention for a variable that is not used in the loop body that means "I don't care about this variable" since we are not using it in the loop body, we can use _ as a placeholder variable name.
for _ in range(1, 10, 2):
    print("Hmmm")

# other way
print("Hmmm" * 5) # this will print "Hmmm" 5 times in a row without spaces in between. If you want to have spaces between each "Hmmm", you can modify the code like this:
print("Hmmm " * 5) # this will print "Hmmm " 5 times in a row with a space after each "Hmmm".

print("Hmmm\n" * 5) # this will print "Hmmm" 5 times in a row with a newline character after each "Hmmm", resulting in each "Hmmm" being printed on a new line.

print("Hmmm", end="") # this will print "Hmmm" without adding a newline character at the end, so if you run this code multiple times, it will print "Hmmm" on the same line without spaces in between. If you want to have spaces between each "Hmmm", you can modify the code like this:
print("Hmmm", end=" ") # this will print "Hmmm" with a space after it, so if you run this code multiple times, it will print "Hmmm" on the same line with spaces in between.

print("Hmmm", end="\n") # this will print "Hmmm" with a newline character at the end, so if you run this code multiple times, it will print "Hmmm" on separate lines.

print("Hmmm" * 4, end="") # this will print "Hmmm" 4 times in a row without adding a newline character at the end, so if you run this code multiple times, it will print "HmmmHmmmHmmmHmmm" on the same line without spaces in between. If you want to have spaces between each "Hmmm", you can modify the code like this:
print("Hmmm " * 4, end="") # this will print "Hmmm " 4 times in a row with a space after each "Hmmm", so if you run this code multiple times, it will print "Hmmm Hmmm Hmmm Hmmm" on the same line with spaces in between.
print("\n", end="") # this will print a newline character without adding an additional newline character at the end, so if you run this code multiple times, it will print a blank line on the console.
print("Hmmm\n" * 4, end="") # this will print "Hmmm" 4 times in a row with a newline character after each "Hmmm", resulting in each "Hmmm" being printed on a new line, and it will not add an additional newline character at the end of the output.

# Unsing sep value in print function
print("Hmmm" * 4, sep=" ", end="") # this will print "Hmmm" 4 times in a row with a newline character after each "Hmmm", resulting in each "Hmmm" being printed on a new line, and it will not add an additional newline character at the end of the output. The sep="" argument is not necessary in this case since we are not using multiple arguments in the print function, but it does not affect the output in this specific case.

# How Separator works?
# The sep parameter in the print function is used to specify the separator that will be inserted between the values that are being printed. By default, the sep parameter is set to a single space (" "), which means that if you print multiple values in a single print statement, they will be separated by a space. For example:
print("Hello", "World") # this will print "Hello World" with a space between "Hello" and "World" because the default separator is a space.
print("Hello", "World", sep="-") # this will print "Hello-World" with a hyphen between "Hello" and "World" because we specified the separator as a hyphen using the sep parameter.
# So, the sep parameter allows you to customize how the values are separated when printed, and it can be set to any string value that you want to use as a separator.

# separator with newline character
print("Hello", "World", sep="\n") # this will print "Hello" and "World" on separate lines because we specified the separator as a newline character using the sep parameter. The output will look like this:
# Hello
# World

print("Hmmm\n" * 4)

# Loop in list
students = ["Alice", "Bob", "Charlie", "David", "Eve"]

for student in students:
    print(student)

for i in range(len(students)):
    print(students[i])

# Dictionary loop
student_grades = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78,
    "David": 90,
    "Eve": 88
}
for student in student_grades:
    print(student) # this will print the keys of the dictionary, which are the student names.
for student in student_grades:
    print(student_grades[student]) # this will print the values of the dictionary, which are the student grades.
for student, grade in student_grades.items():
    print(f"{student}: {grade}") # this will print both the keys and values of the dictionary in a formatted string. The output will look like this:
# Alice: 85
# Bob: 92
# Charlie: 78
# David: 90
# Eve: 88

# why .items() is used in the above code?
# The .items() method is used in the above code to retrieve both the keys and values from the student_grades dictionary in a single loop. When you call .items() on a dictionary, it returns a view object that contains tuples of (key, value) pairs. In the loop, we can unpack these tuples into two variables, student and grade, which allows us to access both the key (student name) and the value (student grade) in each iteration of the loop. This is a convenient way to iterate through a dictionary when you need to work with both keys and values at the same time.

# methods of dictionary (all methods of dictionary are listed below)
# 1. keys() - returns a view object that displays a list of all the keys in the dictionary.
print(student_grades.keys()) # this will print the keys of the dictionary, which are the student names.
# 2. values() - returns a view object that displays a list of all the values in the dictionary.
print(student_grades.values()) # this will print the values of the dictionary, which are the student grades.
# 3. items() - returns a view object that displays a list of all the key-value pairs in the dictionary as tuples.
print(student_grades.items()) # this will print the items of the dictionary, which are the key-value pairs as tuples. The output will look like this:
# dict_items([('Alice', 85), ('Bob', 92), ('Charlie', 78), ('David', 90), ('Eve', 88)])
# 4. get() - returns the value for the specified key if the key is in the dictionary. If the key is not found, it returns None or a specified default value.
print(student_grades.get("Alice")) # this will print the value associated with the key "Alice", which is 85. If the key does not exist in the dictionary, it will return None by default, or you can specify a default value to return instead.
print(student_grades.get("Alice", "Not Found"))
print(student_grades.get("Frank", "Not Found")) # this will print "Not Found" because the key "Frank" does not exist in the dictionary, and we specified "Not Found" as the default value to return when the key is not found.
# 5. update() - updates the dictionary with the key-value pairs from another dictionary or an iterable of key-value pairs.
print(student_grades) # this will print the original dictionary before the update.
new_grades = {
    "Frank": 80,
    "Grace": 95,
    "Alice": 88
}
student_grades.update(new_grades) # this will update the student_grades dictionary with the key-value pairs from the new_grades dictionary.
print(student_grades) # this will print the updated dictionary after the update, which now includes the new key-value pairs for "Frank" and "Grace". The output will look like this: # {'Alice': 88, 'Bob': 92, 'Charlie': 78, 'David': 90, 'Eve': 88, 'Frank': 80, 'Grace': 95}

# 6. pop() - removes the specified key and returns the corresponding value. If the key is not found, it raises a KeyError or returns a specified default value.
print(student_grades) # this will print the current dictionary before popping a key.
removed_grade = student_grades.pop("Alice") # this will remove the key "Alice" from the dictionary and return its corresponding value, which is 88.
print(removed_grade) # this will print the value that was removed, which is 88.
print(student_grades) # this will print the dictionary after popping the key "Alice", which will no longer include "Alice" and its corresponding grade. The output will look like this:
# {'Bob': 92, 'Charlie': 78, 'David': 90, 'Eve': 88, 'Frank': 80, 'Grace': 95}

# 7. popitem() - removes and returns an arbitrary key-value pair from the dictionary as a tuple. If the dictionary is empty, it raises a KeyError.
removed_item = student_grades.popitem() # this will remove and return an arbitrary key-value pair from the dictionary as a tuple. The specific key-value pair that is removed may vary each time you run the code, as it is arbitrary.
print(removed_item) # this will print the key-value pair that was removed as a tuple. The output will look like this:
# ('Grace', 95) # this is just an example, the actual output may vary
print(student_grades) # this will print the dictionary after popping an arbitrary key-value pair, which will no longer include the removed key-value pair. The output will look like this:
# {'Bob': 92, 'Charlie': 78, 'David': 90, 'Eve': 88, 'Frank': 80} # this is just an example, the actual output may vary depending on which key-value pair was removed.

# 8. clear() - removes all key-value pairs from the dictionary, leaving it empty.
print(student_grades) # this will print the current dictionary before clearing it.
student_grades.clear() # this will remove all key-value pairs from the dictionary, leaving it empty.
print(student_grades) # this will print the dictionary after clearing it, which will be empty. The output will look like this:
# {}

# 9. copy() - returns a shallow copy of the dictionary.
student_grades_copy = student_grades.copy() # this will create a shallow copy of the student_grades dictionary and assign it to the variable student_grades_copy.
print(student_grades_copy) # this will print the copied dictionary, which will be the same as the original dictionary at the time of copying. The output will look like this:
# {'Bob': 92, 'Charlie': 78, 'David': 90, 'Eve': 88, 'Frank': 80} # this is just an example, the actual output may vary depending on the state of the original dictionary at the time of copying.

# 10. fromkeys() - creates a new dictionary with the specified keys and a default value for all keys.
keys = ["Alice", "Bob", "Charlie"]
default_value = 0
new_dict = dict.fromkeys(keys, default_value) # this will create a new dictionary with the specified keys from the list and a default value of 0 for all keys.
print(new_dict) # this will print the new dictionary created using fromkeys(). The output will look like this:
# {'Alice': 0, 'Bob': 0, 'Charlie': 0}

# 11. setdefault() - returns the value of the specified key if it is in the dictionary. If the key is not found, it inserts the key with a specified default value and returns that value.
student_grades.setdefault("Alice", 85) # this will return the value of the key "Alice" if it is in the dictionary. If "Alice" is not found, it will insert "Alice" with a default value of 85 and return that value.
print(student_grades) # this will print the dictionary after using setdefault(). If "Alice" was already in the dictionary, it will not be modified. If "Alice" was not in the dictionary, it will be added with the default value of 85. The output will look like this:
# {'Bob': 92, 'Charlie': 78, 'David': 90, 'Eve': 88, 'Frank': 80, 'Alice': 85} # this is just an example, the actual output may vary depending on the state of the dictionary before using setdefault().

# 12. del statement - removes a key-value pair from the dictionary using the del statement.
print(student_grades) # this will print the current dictionary before deleting a key-value pair.
del student_grades["Bob"] # this will remove the key "Bob" and its corresponding value from the dictionary using the del statement.
print(student_grades) # this will print the dictionary after deleting the key "Bob", which will no longer include "Bob" and its corresponding grade. The output will look like this:
# {'Charlie': 78, 'David': 90, 'Eve': 88, 'Frank': 80, 'Alice': 85} # this is just an example, the actual output may vary depending on the state of the dictionary before using the del statement.

# 13. len() - returns the number of key-value pairs in the dictionary.
print(len(student_grades)) # this will print the number of key-value pairs in the student_grades dictionary. The output will look like this:
# 5 # this is just an example, the actual output may vary depending on the state of the dictionary at the time of calling len().

# 14. in operator - checks if a key is in the dictionary.
print("Alice" in student_grades) # this will check if the key "Alice" is in the student_grades dictionary and return True if it is, or False if it is not. The output will look like this:
# True # this is just an example, the actual output may vary depending on the state of the dictionary at the time of checking.
print("Bob" in student_grades) # this will check if the key "Bob" is in the student_grades dictionary and return True if it is, or False if it is not. The output will look like this:
# False # this is just an example, the actual output may vary depending on the state of the dictionary at the time of checking.

# 15. not in operator - checks if a key is not in the dictionary.
print("Alice" not in student_grades) # this will check if the key "Alice" is not in the student_grades dictionary and return True if it is not, or False if it is. The output will look like this:
# False # this is just an example, the actual output may vary depending on the state of the dictionary at the time of checking.
print("Bob" not in student_grades) # this will check if the key "Bob" is not in the student_grades dictionary and return True if it is not, or False if it is. The output will look like this:
# True # this is just an example, the actual output may vary depending on the state of the dictionary at the time of checking.

# 16. dict() constructor - creates a new dictionary from a sequence of key-value pairs or from keyword arguments.
new_dict_from_pairs = dict([("Alice", 85), ("Bob", 92), ("Charlie", 78)]) # this will create a new dictionary from a list of key-value pairs using the dict() constructor.
print(new_dict_from_pairs) # this will print the new dictionary created from the list of key-value pairs. The output will look like this:
# {'Alice': 85, 'Bob': 92, 'Charlie': 78}
new_dict_from_kwargs = dict(Alice=85, Bob=92, Charlie=78) # this will create a new dictionary from keyword arguments using the dict() constructor.
print(new_dict_from_kwargs) # this will print the new dictionary created from keyword arguments. The output will look like this:
# {'Alice': 85, 'Bob': 92, 'Charlie': 78}

# 17. dict comprehension - creates a new dictionary using a comprehension syntax.
squared_numbers = {x: x**2 for x in range(5)} # this will create a new dictionary where the keys are numbers from 0 to 4 and the values are the squares of those numbers using a dictionary comprehension.
print(squared_numbers) # this will print the new dictionary created using a dictionary comprehension. The output will look like this:
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# 18. dict() with zip() - creates a new dictionary by zipping together two sequences of keys and values.
keys = ["Alice", "Bob", "Charlie"]
values = [85, 92, 78]
zipped_dict = dict(zip(keys, values)) # this will create a new dictionary by zipping together the keys and values using the dict() constructor and the zip() function.
print(zipped_dict) # this will print the new dictionary created by zipping together the keys and values. The output will look like this:
# {'Alice': 85, 'Bob': 92, 'Charlie': 78}

# 19. dict() with fromkeys() - creates a new dictionary with specified keys and a default value for all keys.
keys = ["Alice", "Bob", "Charlie"]

