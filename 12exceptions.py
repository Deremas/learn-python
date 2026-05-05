# SyntaxError
# A SyntaxError occurs when the Python interpreter encounters code that does not conform to the syntax rules of the language. This can happen for various reasons, such as missing parentheses, incorrect indentation, or using reserved keywords as variable names. When a SyntaxError is raised, it indicates that there is a problem with the structure of the code, and it cannot be executed until the error is fixed. To resolve a SyntaxError, you need to carefully review your code and ensure that it follows the correct syntax rules of Python.
# Example of a SyntaxError:
# print("Hello, World!" # This line is missing a closing parenthesis, which will raise a SyntaxError.

# IndentationError
# An IndentationError occurs when the indentation of your code is not consistent. In Python, indentation is used to define the scope of loops, functions, and other code blocks. If you mix tabs and spaces or if the indentation level is not consistent, it will raise an IndentationError. To resolve an IndentationError, you need to ensure that your code is indented consistently using either tabs or spaces, and that all code blocks are properly aligned.
# Example of an IndentationError:
# def my_function():
# print("This line is not indented properly.") # This line should be indented to be part of the function body, but it is not, which will raise an IndentationError.

# IndexError
# An IndexError occurs when you try to access an index that is out of range for a list or other sequence type. This can happen when you try to access an index that is negative or greater than or equal to the length of the sequence. When an IndexError is raised, it indicates that you are trying to access an element that does not exist in the sequence. To resolve an IndexError, you need to ensure that you are accessing valid indices within the bounds of the sequence.
# Example of an IndexError:
my_list = [1, 2, 3]
# print(my_list[3]) # This line will raise an IndexError because there is no index 3 in the list (the valid indices are 0, 1, and 2).
# print(my_list[-4]) # This line will raise an IndexError because there is no index -4 in the list (the valid negative indices are -1, -2, and -3).

# KeyError
# A KeyError occurs when you try to access a key that does not exist in a dictionary. This can happen when you try to access a key that has not been defined in the dictionary or when you misspell a key name. When a KeyError is raised, it indicates that the key you are trying to access is not present in the dictionary. To resolve a KeyError, you need to ensure that you are using valid keys that exist in the dictionary and that you are spelling them correctly.
# Example of a KeyError:
my_dict = {"name": "Alice", "age": 30}
# print(my_dict["gender"]) # This line will raise a KeyError because there is no key "gender" in the dictionary.
# print(my_dict["name"]) # This line will successfully access the value associated with the key "name" without raising a KeyError, and it will print "Alice".

# TypeError
# A TypeError occurs when you try to perform an operation on a value of an inappropriate type. This can happen when you try to add a string and an integer, or when you try to call a function with arguments of the wrong type. When a TypeError is raised, it indicates that the operation you are trying to perform is not supported for the given types of values. To resolve a TypeError, you need to ensure that you are using compatible types for the operations you are performing and that you are passing the correct types of arguments to functions.
# Example of a TypeError:
# print("Hello" + 5) # This line will raise a TypeError because you cannot add a string and an integer together.
# print("Hello" + " " + "World!") # This line will successfully concatenate the strings together without raising a TypeError, and it will print "Hello World!".
# ValueError
# A ValueError occurs when a function receives an argument of the correct type but an inappropriate value. This can happen when you try to convert a string to an integer that does not represent a valid number, or when you pass an out-of-range value to a function. When a ValueError is raised, it indicates that the value provided is not suitable for the operation being performed. To resolve a ValueError, you need to ensure that the values you are using are valid and appropriate for the context in which they are being used.
# Example of a ValueError:
# int("abc") # This line will raise a ValueError because "abc" cannot be converted to an integer.
# print(int("123")) # This line will successfully convert the string "123" to the integer 123 without raising a ValueError.
# print(int("abc")) # This line will raise a ValueError because "abc" cannot be converted to an integer.

# try-except block
# A try-except block is a construct in Python that allows you to handle exceptions gracefully. It consists of a try block, where you write the code that may raise an exception, and one or more except blocks, where you specify how to handle specific types of exceptions. When an exception occurs in the try block, the program will immediately jump to the corresponding except block that matches the type of exception raised. This allows you to prevent your program from crashing and instead provide a way to handle errors and continue execution.
# Example of a try-except block:
try:
    x = int(input("What is x? ")) # This line will raise a ValueError if the input is not a valid integer.
    print(f"x is {x}") # This line will print the value of x if the input was successfully converted to an integer.
except ValueError:
    print("Invalid input. Please enter a valid integer.")

# NameError
# A NameError occurs when you try to use a variable or function name that has not been defined in the current scope. This can happen if you misspell a variable name, forget to define a variable before using it, or try to access a variable that is out of scope. When a NameError is raised, it indicates that the name you are trying to use is not recognized by the Python interpreter. To resolve a NameError, you need to ensure that all variables and functions you are using are properly defined and accessible in the current scope.
# Example of a NameError:
# print(x) # This line will raise a NameError because x has not been defined in the current scope.

# try:
#     x = int(input("What is x? ")) # This line will raise a ValueError if the input is not a valid integer.
# except ValueError:
#     print("Invalid input. Please enter a valid integer.")

# print(f"x is {x}") 
# Why it works for integers but not for strings?
# The reason it works for integers but not for strings in this case is because of the way the try-except block is structured. When you try to convert a string to an integer using int(), if the string is not a valid representation of an integer (like "abc"), it will raise a ValueError, which is caught by the except block. However, if you successfully convert a valid string (like "123") to an integer, it will not raise an exception, and the variable x will be assigned the value 123. In this case, when you print(f"x is {x}"), it will work because x has been defined and assigned a value. On the other hand, if you try to print(f"x is {x}") after a ValueError has been raised and caught, x will not have been assigned any value, and this will lead to a NameError when you try to access x outside of the except block.

# else block
# An else block can be used in conjunction with a try-except block to specify code that should be executed if no exceptions were raised in the try block. The else block is executed only if the try block completes successfully without any exceptions. This allows you to separate the code that handles exceptions from the code that should run when everything goes smoothly. The else block can be useful for performing actions that should only occur when there are no errors, such as printing a success message or executing additional logic that depends on the successful completion of the try block.
# Example of a try-except-else block:
try:
    x = int(input("What is x? ")) # This line will raise a ValueError if the input is not a valid integer.
except ValueError:
    print("Invalid input. Please enter a valid integer.")
else:
    print(f"x is {x}") # This line will print the value of x if the input was successfully converted to an integer without raising a ValueError.

# while loop with try-except
# You can use a while loop in combination with a try-except block to repeatedly prompt the user for input until they provide valid input. This is a common pattern for input validation, where you want to ensure that the user enters data in the correct format before proceeding with the rest of the program. The while loop will continue to execute until the user provides valid input that can be successfully processed without raising an exception.
# Example of a while loop with a try-except block for input validation:
while True:
    try:
        x = int(input("What is x? ")) # This line will raise a ValueError if the input is not a valid integer.
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
    else:
        print(f"x is {x}") # This line will print the value of x if the input was successfully converted to an integer without raising a ValueError.
        break # This will exit the while loop once valid input has been provided and processed successfully.

# Or 
# You can also structure the while loop to break immediately after successfully processing valid input, which can make the code cleaner and easier to read. In this case, the else block is not necessary, and you can simply place the print statement and break statement inside the try block after successfully converting the input to an integer.
while True:
    try:
        x = int(input("What is x? ")) # This line will raise a ValueError if the input is not a valid integer.
        break # This will exit the while loop once valid input has been provided and processed successfully.
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

print(f"x is {x}") # This line will print the value of x if the input was successfully converted to an integer without raising a ValueError.

# pass statement
# The pass statement is a null operation in Python. It is used as a placeholder when you need to write code that does nothing, but you want to maintain the structure of your code. The pass statement can be useful in situations where you are defining a function, class, or loop that you plan to implement later, but you want to avoid syntax errors by leaving the body empty. When the Python interpreter encounters a pass statement, it simply ignores it and continues executing the rest of the code.
# Example of using the pass statement:
def my_function():
    pass # This function does nothing for now, but it is defined and can be called without causing a syntax error.
class MyClass:
    pass # This class does nothing for now, but it is defined and can be instantiated without causing a syntax error.