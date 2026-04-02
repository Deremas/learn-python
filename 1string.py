# Strings
text = 'This is Abebe\'s task.'
print(text)

# Using double quotes to avoid escaping
text2 = "This is Abebe's task."
print(text2)

# Multiline string
multiline_text = """This is a multiline string.
It can span multiple lines."""
print(multiline_text)

# String concatenation and formatting

greeting = 'Hello'
name= 'Sam'

# Concatenation
message1 = greeting + ' ' + name
print(message1)

# String formatting
message2 = '{} {}'.format(greeting, name)
print(message2)

# f-strings (Python 3.6+)
message3 = f'{greeting} {name}'
print(message3)

# String methods
print(greeting.upper())  # Output: HELLO
print(greeting.lower())  # Output: hello
print(greeting.replace('l', 'x'))  # Output: Hexxo
print(greeting.split('e'))  # Output: ['H', 'llo']

# String indexing and slicing
print(greeting[0])  # Output: H
print(greeting[1:4])  # Output: llo
print(greeting[-1])  # Output: o
print(greeting[:3])  # Output: Hel
print(greeting[::2])  # Output: Hlo

# String length
print(len(greeting))  # Output: 5

# dir() function to list string methods
print(dir(str))
    # Output: ['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__']
print(dir(greeting))
    # Output: ['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
print(help(str))
    # Output: Help on class str in module builtins:
    # class str(object)
    #  |  str(object='') -> str
    #  |  str(bytes_or_buffer[, encoding[, errors]]) -> str
    #  |
    #  |  Create a new string object from the given object. If encoding or
    #  |  errors is specified, then the object must expose a data buffer
    #  |  that will be decoded using the given encoding and error handler.
    #  |  Otherwise, returns the result of object.__str__() (if defined)
    #  |  or repr(object).