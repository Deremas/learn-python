# ==================================================
# STRING AND DATE FORMATTING IN PYTHON
# ==================================================
# String formatting is the process of creating a new string by inserting values into a template string.
# It allows you to create dynamic strings that can include variables, expressions, and formatted data.
# There are several ways to format strings in Python:
# 1. f-strings (formatted string literals) - introduced in Python 3.6
# Example: 
name = "Alice"; age = 30; print(f"My name is {name} and I am {age} years old.")
# 2. str.format() method - available in Python 2.7 and 3.x
# Example:
print("My name is {} and I am {} years old.".format(name, age))
# 3. % operator (old-style formatting) - available in Python 2.x and 3.x (not recommended for new code)
# Example:
print("My name is %s and I am %d years old." % (name, age))
# 4. Template strings - available in Python 3.2+ (useful for internationalization)
# Example:
from string import Template
template = Template("My name is $name and I am $age years old.")
print(template.substitute(name=name, age=age))

# Date formatting can be done using the datetime module and f-strings or str.format() method.
from datetime import datetime
today = datetime.now()
print(f"Today's date is {today:%B %d, %Y}.")  # Custom format: Month day, Year
print("Today's date is {:%B %d, %Y}.".format(today))

# including weekday and day of the year on above example
print(f"Today is {today:%A, %B %d, %Y} and it's the {today:%j} day of the year.")