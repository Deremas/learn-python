# global

balance = 0

def main():
    print(f'Balance: {balance}')
    deposit(100)
    print(f'Balance: {balance}')
    withdraw(50)
    print(f'Balance: {balance}')

def deposit(amount):
    global balance
    balance += amount

def withdraw(amount):
    global balance
    balance -= amount

if __name__ == "__main__":
    main()

# If  balance -= amount used in deposit and withdraw functions, it will cause an error because balance is a global variable and we are trying to modify it inside the functions without declaring it as global. To fix this, we need to declare balance as global inside the deposit and withdraw functions.
# UnboundLocalError: local variable 'balance' referenced before assignment in function 'deposit'
# UnboundLocalError: local variable 'balance' referenced before assignment in function 'withdraw'

class Account:
    def __init__(self):
        self._balance = 0

    @property
    def balance(self):
        return self._balance

    def deposit(self, amount):
        self._balance += amount
    
    def withdraw(self, amount):
        self._balance -= amount
    
def main():
    account = Account()
    print("Balance:", account.balance)
    account.deposit(100)
    account.withdraw(50)
    print("Balance:", account.balance)

if __name__ == "__main__":
    main()

# constants notation in python:
# In Python, constants are typically defined using uppercase letters with underscores separating words. This convention helps to indicate that the value is intended to be constant and should not be changed throughout the program. For example, you might define a constant for the speed of light as follows:
SPEED_OF_LIGHT = 299792458  # in meters per second
# By using uppercase letters, it is clear to other developers that SPEED_OF_LIGHT is a constant and should not be modified. However, it's important to note that Python does not enforce immutability for constants, so it's still possible to change the value of SPEED_OF_LIGHT if you choose to do so. Therefore, it's a good practice to treat constants as immutable and avoid modifying their values in your code.

class Cat:
    MEOWS = 4

    def meow(self):
        for _ in range(Cat.MEOWS):
            print("Meow!")

cat = Cat()
cat.meow()

# type hints
# Type hints in Python are a way to indicate the expected data types of variables, function parameters, and return values. They are not enforced by the Python interpreter but can be used by developers and tools to improve code readability and catch potential type-related errors. Type hints are added using the typing module, which provides various type annotations. For example, you can use type hints to specify that a function takes two integers and returns an integer:
from typing import List
def add_numbers(a: int, b: int) -> int:
    return a + b
# In this example, the function add_numbers takes two parameters a and b, both of which are expected to be integers, and it returns an integer. Type hints can also be used for more complex data structures, such as lists or dictionaries:
def process_data(data: List[int]) -> None:
    for item in data:
        print(item)
# In this case, the function process_data takes a parameter data, which is expected to be a list of integers, and it does not return any value (indicated by None). Type hints can help improve code clarity and assist with static type checking when using tools like mypy.
# Example for user input with type hints:
def meow(n: int) -> str:
    for _ in range(n):
        print("Meow!")

number = int(input("Enter the number of meows: "))
meow(number)

# docstrings
# Docstrings in Python are a way to document your code by providing a string literal that describes the purpose and usage of a function, class, or module. They are enclosed in triple quotes (""" """) and are typically placed immediately after the definition of the function, class, or module. Docstrings can be accessed using the __doc__ attribute of the object they describe. For example:
def add_numbers(a: int, b: int) -> int:
    """
    Adds two numbers and returns the result.
    
    :param a: The first number to add.
    :type a: int
    :param b: The second number to add.
    :type b: int
    :return: The sum of a and b.
    :rtype: int
    """
    return a + b

# command-line program using argparse
import argparse

parser = argparse.ArgumentParser(description='A simple command-line program to add two numbers.')
parser.add_argument('-a', default=3, type=int, help='The first number to add.')
parser.add_argument('-b', default=5, type=int, help='The second number to add.')
args = parser.parse_args()

result = add_numbers(args.a, args.b)
print(f'The sum of {args.a} and {args.b} is: {result}')
# run like this: python 20et-cetra.py -a 10 -b 20
# If we run the program without providing any arguments, it will use the default values of 3 and 5 for a and b, respectively, and output:
# The sum of 3 and 5 is: 8
# If we run the program with the arguments -a 10 and -b 20, it will output:
# The sum of 10 and 20 is: 30

# If we use positional arguments instead of optional arguments, we can modify the code as follows:
# import argparse
# parser = argparse.ArgumentParser(description='A simple command-line program to add two numbers.')
# parser.add_argument('c', type=int, help='The first number to add.')
# parser.add_argument('d', type=int, help='The second number to add.')
# args = parser.parse_args()
# result = add_numbers(args.c, args.d)
# print(f'The sum of {args.c} and {args.d} is: {result}')
# run like this: python 20et-cetra.py 10 20
# If we run the program without providing any arguments, it will raise an error because the positional arguments are required. We need to provide two integers as arguments when running the program. For example:
# python 20et-cetra.py 7 3
# The sum of 7 and 3 is: 10

# for help message, we can run the program with the -h or --help flag:
# python 20et-cetra.py -h
# Output:
# usage: 20et-cetra.py [-h] [-a A] [-b B]
# A simple command-line program to add two numbers.
# optional arguments:
#   -h, --help  show this help message and exit
#   -a A        The first number to add.
#   -b B        The second number to add.

# unpacking arguments
# If we have a function that takes multiple arguments, we can use unpacking to pass a list or tuple of values as arguments to the function. For example:
def add_numbers(a: int, b: int) -> int:
    return a + b
numbers = (10, 20)
result = add_numbers(*numbers)
print(f'The sum of {numbers[0]} and {numbers[1]} is: {result}')
# In this example, we have a tuple numbers that contains the values 10 and 20. By using the * operator, we unpack the tuple and pass its elements as separate arguments to the add_numbers function. The output will be:
# The sum of 10 and 20 is: 30
# This allows us to easily pass a list or tuple of values to a function without having to specify each argument individually.
def calculate(a: int, b: int, c: int) -> int:
    return a + b + c
values = [1, 2, 3]
result = calculate(*values)
print(f'The sum of {values[0]}, {values[1]}, and {values[2]} is: {result}')
# In this example, we have a list values that contains the values 1, 2, and 3. By using the * operator, we unpack the list and pass its elements as separate arguments to the calculate function. The output will be:
# The sum of 1, 2, and 3 is: 6

# What mean *args and **kwargs in Python?
# In Python, *args and **kwargs are used to allow a function to accept an arbitrary number of positional and keyword arguments, respectively.
# *args allows a function to accept any number of positional arguments. It collects the extra positional arguments into a tuple  or list and allows you to access them within the function. For example:
def my_function(*args):
    for arg in args:
        print(arg)
my_function(1, 2, 3)
# In this example, the function my_function can accept any number of positional arguments. When we call my_function(1, 2, 3), it will print each of the arguments on a new line:
# 1
# 2
# 3

# **kwargs allows a function to accept any number of keyword arguments. It collects the extra keyword arguments into a dictionary and allows you to access them within the function. For example:
def my_function(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
    print(kwargs) # This will print the entire dictionary of keyword arguments
my_function(name="Alice", age=30, city="New York")
# In this example, the function my_function can accept any number of keyword arguments. When we call my_function(name="Alice", age=30, city="New York"), it will print each of the keyword arguments and their corresponding values:
# name: Alice
# age: 30
# city: New York

# You can also combine *args and **kwargs in the same function to allow for both positional and keyword arguments. For example:
def my_function(*args, **kwargs):
    print("Positional arguments:")
    for arg in args:
        print(arg)
    print("Keyword arguments:")
    for key, value in kwargs.items():
        print(f"{key}: {value}")
my_function(1, 2, 3, name="Alice", age=30)
# In this example, the function my_function can accept both positional and keyword arguments. When we call my_function(1, 2, 3, name="Alice", age=30), it will print the positional arguments followed by the keyword arguments:
# Positional arguments:
# 1
# 2
# 3
# Keyword arguments:
# name: Alice
# age: 30

# yelling
def main():
    # yell(["This", "is", "a", "yell!"])
    yell("This", "is", "a", "yell!")

# def yell(words):
def yell(*words):
    uppercase_words = []
    for word in words:
        uppercase_words.append(word.upper())
    print(*uppercase_words)

if __name__ == "__main__":
    main()



# map in python
# The map function in Python is a built-in function that applies a given function to each item of an iterable (such as a list) and returns an iterator that yields the results. The syntax for the map function is:
# map(function, iterable, ...)
# The function parameter is the function that you want to apply to each item of the iterable. The iterable parameter is the iterable (such as a list) that you want to process. You can also pass multiple iterables to the map function, and it will apply the function to the corresponding items from each iterable. For example:
# using map in yell function

def main():
    yell("My", "goal", "is", "being", "better", "in", "programming", "and", "getting", "100K", "salary", "per", "month")

def yell(*words):
    uppercase_words = map(str.upper, words)
    print(*uppercase_words)

if __name__ == "__main__":
    main()

# list comprehension
# List comprehension is a concise way to create lists in Python. It allows you to generate a new list by applying an expression to each item in an iterable, while optionally filtering items using a condition. The syntax for list comprehension is:

# [expression for item in iterable if condition]

# For example, if we want to create a list of squares for the numbers from 0 to 9, we can use list comprehension like this:
squares = [x**2 for x in range(10)]
print(squares)
# Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
# In this example, the expression is x**2, which calculates the square of each number. The item is x, which iterates over the range of numbers from 0 to 9. The condition is not specified in this case, so all items are included in the resulting list.

# yelling with list comprehension
def main():
    yell("This", "is", "really", "cool!")

def yell(*words):
    uppercase_words = [word.upper() for word in words]
    print(*uppercase_words)

if __name__ == "__main__":
    main()

# filter in python
# The filter function in Python is a built-in function that constructs an iterator from elements of an iterable for which a specified function returns true. The syntax for the filter function is:
# filter(function, iterable)
# The function parameter is a function that takes an item from the iterable and returns a boolean value (True or False). The iterable parameter is the iterable (such as a list) that you want to filter. The filter function will return an iterator that yields only the items from the iterable for which the function returns True. For example, if we want to filter out even numbers from a list of integers, we can use the filter function like this:
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = filter(lambda x: x % 2 == 0, numbers)
print(list(even_numbers))
# Output: [2, 4, 6, 8, 10]

# yelling with filter
def main():
    yell("This", "is", "really", "cool!")

def yell(*words):
    uppercase_words = filter(lambda word: len(word) > 3, words)
    uppercase_words = map(str.upper, uppercase_words)
    print(*uppercase_words)

if __name__ == "__main__":
    main()

# dictionary comprehension
# Dictionary comprehension is a concise way to create dictionaries in Python. It allows you to generate a new dictionary by applying an expression to each item in an iterable, while optionally filtering items using a condition. The syntax for dictionary comprehension is:
# {key_expression: value_expression for item in iterable if condition}
# For example, if we want to create a dictionary that maps numbers from 0 to 9 to their squares, we can use dictionary comprehension like this:
squares_dict = {x: x**2 for x in range(10)}
print(squares_dict)
# Output: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}
# In this example, the key_expression is x, which represents the number from the range. The value_expression is x**2, which calculates the square of the number. The item is x, which iterates over the range of numbers from 0 to 9. The condition is not specified in this case, so all items are included in the resulting dictionary.

# enumerate in python
# The enumerate function in Python is a built-in function that adds a counter to an iterable and returns it as an enumerate object. This allows you to loop through the items of the iterable while keeping track of the index of each item. The syntax for the enumerate function is:
# enumerate(iterable, start=0)
# The iterable parameter is the iterable (such as a list) that you want to enumerate. The start parameter is an optional argument that specifies the starting index for the enumeration (default is 0). When you use enumerate in a loop, it will yield pairs of index and item for each item in the iterable. For example:
fruits = ['apple', 'banana', 'cherry']
for index, fruit in enumerate(fruits):
    print(f"{index + 1}: {fruit}")
# Output:
# 1: apple
# 2: banana
# 3: cherry

# yelling with enumerate
def main():
    yell("This", "is", "really", "cool!")

def yell(*words):
    for index, word in enumerate(words):
        if len(word) < 5:
            print(f"{index + 1}: {word.upper()}")
if __name__ == "__main__":
    main()

# generators in python
# A generator in Python is a special type of iterable that allows you to generate values on-the-fly, rather than storing them all in memory at once. Generators are defined using a function that contains one or more yield statements. When the generator function is called, it returns an iterator object that can be used to iterate over the generated values. Each time the yield statement is executed, the current state of the generator is saved, and the value specified by yield is returned to the caller. The next time the generator is iterated, it resumes execution from where it left off, allowing you to generate the next value. For example:
def main():
    n = int(input("What is n? "))
    for s in sheep(n):
        print(s)

def sheep(n):
    for i in range(n):
        yield "sheep" * i

if __name__ == "__main__":
    main()