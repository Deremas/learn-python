# Functions
# Functions are reusable blocks of code that perform a specific task. They help to break down complex problems into smaller, manageable pieces, and they promote code reusability and modularity.
# In Python, you can define a function using the def keyword, followed by the function name and parentheses. The code block within the function is indented.
# Defining a function
    # def function_name(parameters):
    #     # code to execute
# Empty function
def empty_function():
    pass  # The pass statement is used as a placeholder for future code. It does nothing when executed.

# Example of a simple function that takes no parameters and returns a greeting message
def greet():
    return "Hello, World!"
print(greet())  # Output: Hello, World!

# Applying methods to the return value of a function
print(greet().upper())  # Output: HELLO, WORLD! (applying the upper() method to the return value of the greet() function)
print(greet().lower())  # Output: hello, world! (applying the lower() method to the return value of the greet() function)
print(greet().split(", "))  # Output: ['Hello', 'World!'] (applying the split() method to the return value of the greet() function)

# Function with parameters
def greet_person(name):
    # return '{} is a great person!'.format(name)
    return f"Hello, {name}!"
print(greet_person("Alice"))  # Output: Hello, Alice! (calling the greet_person() function with the argument "Alice")
print(greet_person("Bob").upper())  # Output: HELLO, BOB! (calling the greet_person() function with the argument "Bob" and applying the upper() method to the return value)

# Default parameter values
def greet_person(name="Guest"):
    return f"Hello, {name}!"
print(greet_person())  # Output: Hello, Guest! (calling the greet_person() function without an argument, so it uses the default value "Guest")
print(greet_person("Alice"))  # Output: Hello, Alice! (calling the greet_person() function with the argument "Alice", which overrides the default value)