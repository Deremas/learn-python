# F-Strings
name = "Alice"
age = 30
print(f"My name is {name} and I am {age} years old.")

# Using format() method
print("My name is {} and I am {} years old.".format(name, age))

# Using % operator
print("My name is %s and I am %d years old." % (name, age))
# Why s and d? s is for string and d is for decimal (integer)

# Formatting numbers
pi = 3.14159
print(f"Pi is approximately {pi:.2f}.")  # 2 decimal places

# Using f-strings with expressions
radius = 5
area = 3.14159 * radius ** 2
print(f"The area of a circle with radius {radius} is approximately {area:.2f}.")

# F-strings 
# can also include function calls
person = {"name": "Bob", "age": 25}
sentence = 'My name is {} and I am {} years old.'.format(person["name"], person["age"])
sentence_f = 'My name is {name} and I am {age} years old.'.format(**person)
# why **person? It unpacks the dictionary so that the keys can be used as variable names in the format string.

person2 = {"name": "Charlie", "age": 35}

# print(f'My name is {person2['name']} and I am {person2['age']} years old.')

# This works in Python 3.12+ because f-strings were improved.
# Python now understands that the quotes inside { } are part of the dictionary key.
#
# {person2['name']} is treated as a normal Python expression.
#
# In Python 3.11 or older, this may give a SyntaxError.
#
# Best practice:
# Use different quote types for cleaner and safer code:

print(f"My name is {person2['name']} and I am {person2['age']} years old.")

# Birthday formatting
from datetime import datetime
birthday = datetime(1990, 2, 15)
print(f"My birthday is on {birthday}")  # Default format
print(f"My birthday is on {birthday:%B %d, %Y}")  # Custom format
print(f"My birthday is on {birthday:%b %d, %y}")  # Short month and year
print(f"My birthday is on {birthday:%Y-%m-%d}")  # ISO format
# %B - Full month name
# %b - Abbreviated month name
# %d - Day of the month (zero-padded)
# %Y - Year with century
# %y - Year without century (zero-padded)

# Why is custom and ISO format year, month, day output same with different formats?
# The output appears the same because both formats ultimately display the same date components (year, month, day).
# The difference is in the representation: %Y-%m-%d is the ISO format, while %B %d, %Y is a more human-readable format.
