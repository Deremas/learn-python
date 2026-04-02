# Conditionals

# Comparisons:
# Equal: == (checks if values are equal)
# Not equal: != (checks if values are not equal)
# Greater than: > (checks if the left value is greater than the right value)
# Less than: < (checks if the left value is less than the right value)
# Greater than or equal to: >= (checks if the left value is greater than or equal to the right value)
# Less than or equal to: <=  (checks if the left value is less than or equal to the right value)
# Object identity: is (checks if two variables point to the same object in memory)

# If statement
landuage = 'Python'
if landuage == 'Python':
    print('I love Python!')  # Output: I love Python!

# If-else statement
language = 'JavaScript'
if language == 'Python':
    print('I love Python!')
else:
    print('I do not love Python!')  # Output: I do not love Python!

# If-elif-else statement
language = 'Java'
if language == 'Python':
    print('I love Python!')
elif language == 'JavaScript':
    print('I love JavaScript!')
elif language == 'Java':
    print('I love Java!')
else:
    print('I do not love Python, JavaScript, or Java!')  # Output: I do not love Python, JavaScript, or Java!


# Boolean values
# Boolean values are a data type that can only have two possible values: True or False. They are often used in conditional statements to control the flow of a program.
# and: Returns True if both statements are true
# or: Returns True if one of the statements is true
# not: Reverse the result, returns False if the result is true

user = 'admin'
logged_in = True

if user == 'admin' and logged_in:
    print('Welcome, admin!')  # Output: Welcome, admin!
elif user == 'admin' or logged_in:
    print('Welcome, admin or logged in user!')  # Output: Welcome, admin or logged in user!
else:
    print('Access denied!')  # Output: Access denied!


# not operator
is_raining = False
if not is_raining:
    print('It is not raining, you can go outside!')  # Output: It is not raining, you can go outside!

# Object identity
a = [1, 2, 3]
b = a  # b points to the same list object as a
c = [1, 2, 3]  # c points to a different list object with the same content
print(id(a)) # Output: (memory address of the list object that a points to)
print(id(b)) # Output: (same memory address as a, since b points to the same object)
print(id(c)) # Output: (different memory address than a and b, since c points to a different object)  
print(a == b)  # Output: True (a and b have the same content)
print(a is b)  # Output: True (a and b point to the same object in memory)
print(a == c)  # Output: True (a and c have the same content)
print(a is c)  # Output: False (a and c point to different objects in memory)

# In Python, small integers and strings are cached by the interpreter, so they may point to the same memory location. However, this is an implementation detail and should not be relied upon in your code. Always use == to compare values for equality and is to compare object identity when necessary.

# False values in Python include:
# False
# None
# 0 (zero of any numeric type)
# 0.0 (zero float)
# 0j (zero complex)
# Empty sequences and collections (e.g., '', [], (), {}, set())
# An empty map (e.g., dict() or {}) 
# All other values are considered True in a boolean context.

# 