# Libraries
# Libraries are collections of pre-written code that provide additional functionality to your programs. They allow you to perform complex tasks without having to write all the code from scratch. 
# Modules are files containing Python code that define functions, classes, and variables. You can import modules into your program to use the functionality they provide.
# Library vs Module
# A library is a collection of modules that provide a wide range of functionality for various tasks, while a module is a single file that contains code for specific functionality. In other words, a library is a larger collection of code that may include multiple modules, whereas a module is a smaller unit of code that can be imported and used in your program. For example, the Python Standard Library is a collection of modules that provide various functionalities such as file handling, regular expressions, and data manipulation, while a specific module like "math" provides functions for mathematical operations.
# Importing Libraries
# To use a library or module in your Python program, you need to import it. You can import a library or module using the import statement. For example, to import the math module, you can use the following code:

# random module
# The random module is a built-in Python library that provides functions for generating random numbers and performing random operations. It includes functions for generating random integers, floating-point numbers, and selecting random items from a list. The random module is commonly used in various applications such as games, simulations, and data analysis where randomness is required. To use the random module, you can import it using the import statement and then call its functions to generate random values or perform random operations in your program.
import random
# Example of using the random module to generate a random integer between 1 and 10:
random_integer = random.randint(1, 10)
print(random_integer) # This will print a random integer between 1 and 10 each time you run the program.

# Methods of random module
# The random module provides several methods for generating random numbers and performing random operations. Some of the commonly used methods include:
# random() - returns a random floating-point number between 0.0 and 1.0.
# randint(a, b) - returns a random integer N such that a <= N <= b.
# choice(seq) - returns a random element from the non-empty sequence seq.
# shuffle(x) - shuffles the sequence x in place.
# sample(population, k) - returns a list of k unique elements chosen from the population sequence or set.

# Example of using some of the methods from the random module:
# Generate a random floating-point number between 0.0 and 1.0
random_float = random.random()
print(random_float) # This will print a random floating-point number between 0.0 and 1.0 each time you run the program.
# Generate a random integer between 1 and 10
random_integer = random.randint(1, 10)
print(random_integer) # This will print a random integer between 1 and 100 each time you run the program.
# Select a random element from a list
my_list = ['apple', 'banana', 'cherry', 'date']
random_element = random.choice(my_list)
print(random_element) # This will print a random element from the list each time you run the program.
# Shuffle the list
shuffled_list = ["Abay", "Tana", "Awash", "Omo", "Baro", "Wabi Shebele", "Koka"]
random.shuffle(shuffled_list)
print(shuffled_list) # This will print the list in a random order each time you run the program.
# Select a random sample of 2 elements from the list
random_sample = random.sample(my_list, 2)
print(random_sample) # This will print a list of 2 unique random elements from the original list each time you run the program.
# End of random module examples

# from keyword
# The from keyword is used in Python to import specific functions, classes, or variables from a module or library. It allows you to import only the specific components you need, rather than importing the entire module. This can help to reduce memory usage and improve code readability by making it clear which components are being used in your program. For example, if you only need the randint function from the random module, you can use the from keyword to import just that function like this:
from random import randint

# statistics module
# The statistics module is a built-in Python library that provides functions for calculating mathematical statistics of numerical data. It includes functions for calculating measures of central tendency (mean, median, mode), measures of dispersion (variance, standard deviation), and other statistical properties of data. The statistics module is commonly used in data analysis and scientific computing to perform statistical calculations on datasets. To use the statistics module, you can import it using the import statement and then call its functions to perform various statistical operations on your data.
import statistics
# Example of using the statistics module to calculate the mean, median, and mode of a list of numbers:
data = [1, 2, 3, 4, 5, 5]
mean = statistics.mean(data)
median = statistics.median(data)
mode = statistics.mode(data)
print(f"Mean: {mean}, Median: {median}, Mode: {mode}") # This will print the mean, median, and mode of the list of numbers each time you run the program. In this example, the output will be:
# Mean: 3.3333333333333335, Median: 3.5, Mode: 5

# system module
# The system module is a built-in Python library that provides functions for interacting with the operating system. It allows you to perform various tasks such as accessing environment variables, working with file paths, and executing system commands. The system module is commonly used for tasks that require interaction with the underlying operating system, such as managing files and directories, handling command-line arguments, and performing system-level operations. To use the system module, you can import it using the import statement and then call its functions to perform various operations related to the operating system.
import sys
# Example of using the system module to access command-line arguments:
# This program will print the command-line arguments passed to it when executed.
print("Command-line arguments:", sys.argv) 
# When you run this program from the command line and provide some arguments, it will print those arguments as a list. For example, if you run the program like this:
# python my_program.py arg1 arg2 arg3
# The output will be:
# Command-line arguments: ['my_program.py', 'arg1', 'arg2', 'arg3']

try:
    # Example of using the system module to access an environment variable
    home_directory = sys.getenv("HOME")
    print("Home Directory:", home_directory) 
    # This will print the value of the HOME environment variable, which typically contains the path to the user's home directory. The output will vary depending on the operating system and user configuration.
except AttributeError:
    print("The sys module does not have a getenv function. Please use os.getenv instead.")

# sys module does not have a getenv function, so you should use the os module to access environment variables instead. Here's an example of how to use the os module to access an environment variable:
import os
# Example of using the os module to access an environment variable
home_directory = os.getenv("DESKTOP")
print("Home Directory:", home_directory) 
# This will print the value of the HOME environment variable, which typically contains the path to the user's home directory. The output will vary depending on the operating system and user configuration.

# why is "DESKTOP" is not working as an environment variable?
# The "DESKTOP" environment variable may not be set on your system, which is why it is not working. Environment variables are specific to the operating system and user configuration, and not all systems may have a "DESKTOP" environment variable defined. To check if the "DESKTOP" environment variable is set on your system, you can use the following code:

# argv method
# The argv method is a part of the sys module in Python and is used to access command-line arguments passed to a Python script. It is a list that contains the command-line arguments as strings. The first element of the list (argv[0]) is the name of the script itself, and the subsequent elements (argv[1], argv[2], etc.) are the additional arguments passed to the script. You can use the argv method to retrieve and process command-line arguments in your Python programs, allowing you to customize the behavior of your script based on user input from the command line.

print("Command-line arguments:", sys.argv)
# When you run this program from the command line and provide some arguments, it will print those arguments as a list. For example, if you run the program like this:
# python my_program.py arg1 arg2 arg3
# The output will be:
# Command-line arguments: ['my_program.py', 'arg1', 'arg2', 'arg3']
# This shows that the argv method successfully captures the command-line arguments passed to the script, allowing you to access and use them in your program as needed.
# Example of using the argv method to access command-line arguments and perform a simple operation:
if len(sys.argv) > 1:
    # If there are command-line arguments provided, print the first argument
    print("First command-line argument:", sys.argv[1])
else:
    print("No command-line arguments provided.")
# When you run this program from the command line and provide some arguments, it will print the first argument passed to the script. For example, if you run the program like this:
# python my_program.py arg1 arg2 arg3
for arg in sys.argv[1:]: # This will iterate through all the command-line arguments except the first one (which is the script name) and print each argument on a new line.
    print(arg)

# Slicing
# Slicing is a technique in Python that allows you to extract a portion of a sequence (such as a list, string, or tuple) by specifying a range of indices. The syntax for slicing is [start:stop:step], where start is the index to begin the slice, stop is the index to end the slice (exclusive), and step is the interval between indices. Slicing can be used to create new sequences based on existing ones, and it provides a convenient way to access specific parts of a sequence without modifying the original data. For example, if you have a list of numbers and you want to extract a subset of those numbers, you can use slicing to achieve that.
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Example of using slicing to extract a portion of the list
sliced_list = my_list[2:7] # This will extract the elements from index
# 2 to index 6 (7 is exclusive) from the original list and create a new list called sliced_list.
print(sliced_list) # This will print the sliced list, which contains the elements [3, 4, 5, 6, 7] from the original list.


# sys.exit()  # 35 min
# The sys.exit() function is used to exit a Python program. It allows you to terminate the program and optionally provide an exit status code. When sys.exit() is called, it raises a SystemExit exception, which can be caught and handled if needed. The exit status code can be used to indicate whether the program exited successfully (usually with a status code of 0) or if there was an error (with a non-zero status code). For example, you can use sys.exit(0) to indicate a successful exit, or sys.exit(1) to indicate an error. When sys.exit() is called, the program will stop executing any further code and will exit immediately.
# Example of using sys.exit() to exit a program with a specific exit status code:
# import sys
# # Check if a command-line argument is provided
# if len(sys.argv) > 1:
#     print("First command-line argument:", sys.argv[1])
#     exit_status = 0  # Successful exit status, without stopping this lesson file.
# else:
#     print("No command-line arguments provided.")
#     exit_status = 1  # Error exit status, without stopping this lesson file.
# print("Exit status would be:", exit_status)
# When you run this program from the command line and provide some arguments, it will print the first argument and exit with a status code of 0. If you run the program without providing any arguments, it will print a message indicating that no arguments were provided and exit with a status code of 1. The exit status code can be used by other programs or scripts to determine the outcome of the program's execution.


####################################################################
####################################################################
# Packages
####################################################################
####################################################################
# Packages are a way to organize and structure your Python code into reusable modules. A package is a directory that contains multiple modules, which are individual Python files that define functions, classes, and variables. Packages allow you to group related modules together, making it easier to manage and maintain your code. They also provide a way to avoid naming conflicts by using namespaces. To create a package, you need to create a directory with an __init__.py file inside it, which can be empty or contain initialization code for the package. You can then import modules from the package using the dot notation (e.g., import my_package.my_module) to access the functionality provided by the modules within the package.
# Third-party packages are libraries that are developed and maintained by the Python community, rather than being included in the standard library. These packages can be installed using package managers like pip and provide additional functionality for various tasks such as data analysis, web development, machine learning, and more. Examples of popular third-party packages include NumPy for numerical computing, Pandas for data manipulation, Flask for web development, and TensorFlow for machine learning. Third-party packages can greatly enhance the capabilities of your Python programs and allow you to leverage the work of other developers to solve complex problems efficiently.
# To install a third-party package, you can use the pip package manager. For example, to install the NumPy package, you can run the following command in your terminal or command prompt:
# pip install numpy
# Once you have installed a third-party package, you can import it into your Python program using the import statement. For example, to import the NumPy package, you can use the following code:
# import numpy as np

# pypi.org
# PyPI (Python Package Index) is a repository of software packages for the Python programming language. It is the official third-party software repository for Python and contains a vast collection of packages that can be easily installed and used in Python projects. PyPI allows developers to share their code with the community and provides a convenient way for users to find and install packages that meet their needs. You can search for packages on the PyPI website (https://pypi.org/) and use the pip package manager to install them in your Python environment. For example, if you want to install the requests package, you can run the following command:
# pip install requests

# cowsay package
# The cowsay package is a fun and whimsical Python library that allows you to generate ASCII art of a cow (or other characters) saying a message. It provides a simple interface to create amusing text-based messages with a cow character. You can install the cowsay package using pip and then use it in your Python programs to add a touch of humor to your output. For example, you can use the cowsay package to make the cow say "Hello, World!" like this:
import cowsay
import sys
if len(sys.argv) > 1:
    for arg in sys.argv[1:]:
        cowsay.cow(arg)
else:
    cowsay.cow("Hello, World!")
# This will print an ASCII art of a cow saying "Hello, World!" in the console. The cowsay package also includes other characters and options for customizing the appearance of the cow and the message it says, making it a fun and entertaining way to add some personality to your Python programs.

# API and API calls
# An API (Application Programming Interface) is a set of rules and protocols that allows different software applications to communicate and interact with each other. It defines how different software components should interact and exchange data. An API call is a request made by a client application to an API server to access specific functionality or data provided by the API. API calls typically involve sending a request to a specific endpoint of the API, along with any necessary parameters or data, and receiving a response from the server that contains the requested information or performs the desired action. APIs are commonly used in web development, mobile app development, and other software applications to enable integration and communication between different systems and services.
# Example of making an API call using the requests library to retrieve data from a public API:
# import requests
# let us call from apple itunes search API to search for a song
# JSON
# JSON (JavaScript Object Notation) is a lightweight data interchange format that is easy for humans to read and write, and easy for machines to parse and generate. It is commonly used for transmitting data between a server and a web application as an alternative to XML. JSON represents data as key-value pairs, where keys are strings and values can be various data types such as strings, numbers, arrays, or other JSON objects. When making an API call, the response from the server is often in JSON format, which can be easily parsed and processed in Python using libraries like requests or json.
# let us prepare a code with sys arg, json format, and API call to search for a song using the Apple iTunes Search API:
import requests
import sys
import json
if len(sys.argv) > 1:
    song_name = " ".join(sys.argv[1:])
    api_url = "https://itunes.apple.com/search"
    params = {
        "term": song_name,
        "entity": "song",
        "limit": 1,
    }
    response = requests.get(api_url, params=params)
    if response.status_code == 200:
        # let us format the response in JSON format
        data = response.json() # This converts the response from the API call into a Python dictionary.
        print(json.dumps(data, indent=4)) # This prints the API response as formatted JSON.
        if data["resultCount"] > 0:
            song = data["results"][0]
            print(f"Top result for '{song_name}':")
            print(f"Artist: {song['artistName']}")
            print(f"Track: {song['trackName']}")
            print(f"Album: {song['collectionName']}")
        else:
            print(f"No results found for '{song_name}'.")
    else:
        print("Error making API call.")


####################################################################
# __name__ and "__main__" summary
####################################################################
# Every Python file gets a special variable called __name__.
#
# If you run this file directly:
# python 13libraries.py
#
# Python sets:
# __name__ = "__main__"
#
# If another file imports this file:
# import 13libraries
#
# Python sets __name__ to the module/file name instead.
#
# Purpose:
# The line below lets us choose which code should run only when this
# file is executed directly. It prevents test code, print statements,
# API calls, and command-line code from running automatically when the
# file is imported into another file.
#
# Common structure:
# def main():
#     # Put the script/program code here.
#     pass
#
# if __name__ == "__main__":
#     main()
#
# This makes the file useful in two ways:
# 1. You can run it directly as a program.
# 2. You can import its functions into another file without running the
#    whole program automatically.
#
# If a file has many functions, even 20 or more, you do not need to put
# all of them inside main(). Define your reusable functions normally at
# the top level of the file, then call only the functions you want from
# main().
#
# Good pattern:
# def helper_one():
#     pass
#
# def helper_two():
#     pass
#
# def main():
#     helper_one()
#     helper_two()
#
# if __name__ == "__main__":
#     main()
#
# In this pattern:
# - helper_one() and helper_two() can be imported by another file.
# - main() runs only when this file is executed directly.
# - importing the file does not automatically run the whole script.
#
# Note:
# Use == for comparison. Do not use = here.
# Correct:   if __name__ == "__main__":
# Incorrect: if __name__ = "__main__":


def main_demo():
    print("This demo runs only when this file is run directly.")


if __name__ == "__main__":
    main_demo()
