# Lists in Python
# Creating a list
my_list =[] # Empty list or
my_list = list() # Empty list

print(my_list)  # Output: []

my_list = [1, 2, 3] # List with integers
print(my_list)  # Output: [1, 2, 3]
my_list = [1, 2, 3, 'four', 'five'] # List with mixed data types 
print(my_list)  # Output: [1, 2, 3, 'four', 'five']

my_list = [1, 2, 3, [4, 5], 'six'] # List with nested list
print(my_list)  # Output: [1, 2, 3, [4, 5], 'six']

# List indexing and slicing
print(my_list[0])  # Output: 1

courses = ['Math', 'Science', 'History', 'Art']
print(courses[1])  # Output: Science
print(courses[3])  # Output: Art

# Negative indexing
print(courses[-1])  # Output: Art
print(courses[-2])  # Output: History

# List slicing
print(courses[1:3])  # Output: ['Science', 'History']
print(courses[:2])  # Output: ['Math', 'Science']
print(courses[2:])  # Output: ['History', 'Art']
print(courses[::2])  # Output: ['Math', 'History'] it skips every second element and returns the first and third element
print(courses[::-1])  # Output: ['Art', 'History', 'Science', 'Math'] it reverses the list
print(courses[1:4:2])  # Output: ['Science', 'Art'] it returns the second and fourth element by skipping one element in between
print(courses[1::2])  # Output: ['Science', 'Art'] it returns the second and fourth element by skipping one element in between

# Adding and removing elements
courses.append('Music')  # Add an element to the end of the list
print(courses)  # Output: ['Math', 'Science', 'History', 'Art', 'Music']
courses.insert(2, 'Literature')  # Insert an element at a specific index
print(courses)  # Output: ['Math', 'Science', 'Literature', 'History', 'Art', 'Music']
courses.remove('Science')  # Remove an element by value
print(courses)  # Output: ['Math', 'Literature', 'History', 'Art', 'Music']
courses.pop()  # Remove the last element
print(courses)  # Output: ['Math', 'Literature', 'History', 'Art']
courses.pop(1)  # Remove an element at a specific index
print(courses)  # Output: ['Math', 'History', 'Art']

# Extending a list
more_courses = ['Physics', 'Chemistry']
other_courses = ['Biology', 'Economics']
courses.extend(more_courses)  # Extend the list by adding elements from another list at the end of the list
print(courses)  # Output: ['Math', 'History', 'Art', 'Physics', 'Chemistry'] 
print(courses + other_courses)  # Output: ['Math', 'History', 'Art', 'Physics', 'Chemistry', 'Biology', 'Economics']  
courses += other_courses  # Extend the list by adding elements from another list at the end of the list
print(courses)  # Output: ['Math', 'History', 'Art', 'Physics', 'Chemistry', 'Biology', 'Economics']

# inserting a list into another list
new_lists = ['Amharic', 'English']
courses.insert(1, new_lists)
print(courses)  # Output: ['Math', ['Amharic', 'English'], 'History', 'Art', 'Physics', 'Chemistry', 'Biology', 'Economics']
print(courses.pop(1))
print(courses)
courses.extend(new_lists)
print(courses)  # Output: ['Math', 'History', 'Art', 'Physics', 'Chemistry', 'Biology', 'Economics', 'Amharic', 'English']

# Sorting a list
our_list = [3, 1, 4, 2]
# our_list.sort()
# print(our_list)  # Output: [1, 2, 3, 4]
# our_list.sort(reverse=True)
# print(our_list) # Output: [4, 3, 2, 1]

# Sort without modifying the original list
sorted_list = sorted(our_list)
print(our_list)  # Output: [3, 1, 4, 2]
print(sorted_list)  # Output: [1, 2, 3, 4]
sorted_list_desc = sorted(our_list, reverse=True)
print(sorted_list_desc)  # Output: [4, 3, 2, 1]

# FInd the index of an element
print(courses.index('Art'))  # Output: 2
print(our_list.index(4))  # Output: 2

# Check if an element is in the list
print('Math' in courses)  # Output: True
print('Geography' in courses)  # Output: False

# List length
print(len(courses))  # Output: 9
print(len(our_list))  # Output: 4

# Printing all items of the list using a loop
for course in courses:
    print(course)
# Printing all items of the list using a loop with index
for i in range(len(courses)):
    print(f'Course {i}: {courses[i]}')
# Priting all items of the list using enumerate
for index, course in enumerate(courses):
    print(index, course)
    print(f'Course {index}: {course}')
for index, course in enumerate(courses, start=1):
    print(f'Course {index}: {course}')

# Changing an element in the list
courses[0] = 'Algebra'
print(courses)  # Output: ['Algebra', 'History', 'Art', 'Physics', 'Chemistry', 'Biology', 'Economics', 'Amharic', 'English']
print(len(courses))

# Changing list into strings
courses_str = ', '.join(courses)  # Join list elements into a string with a separator
print(courses_str)  # Output: 'Algebra, History, Art, Physics, Chemistry, Biology, Economics, Amharic, English'
courses_list = courses_str.split(', ')  # Split the string back into a list using the same separator
print(courses_list)  # Output: ['Algebra', 'History', 'Art', 'Physics', 'Chemistry', 'Biology', 'Economics', 'Amharic', 'English']

random_str = 'Sol, Luna, Mars, Venus, Jupiter, Saturn, Uranus, Neptune'
planets = random_str.split(', ')  # Split the string into a list of planets
print(planets)  # Output: ['Sol', 'Luna', 'Mars', 'Venus', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
hiphen_courses_str = '-'.join(courses)  # Join list elements into a string with a different separator
print(hiphen_courses_str)  # Output: 'Algebra-History-Art-Physics-Chemistry-Biology-Economics-Amharic-English'

hiphen_str = 'Abebe-Worku-12345-Engineer-Ethiopia-Addis Ababa'
hiphen_list = hiphen_str.split('-') # Split the string into a list using the hiphen as a separator
print(hiphen_list)  # Output: ['Abebe', 'Worku', '12345', 'Engineer', 'Ethiopia', 'Addis Ababa']