# File I/O
# File I/O (Input/Output) in Python allows you to read from and write to files. Here are some common operations for working with files in Python:
# 1. Opening a file - You can use the built-in `open()` function to open a file. It takes the file name and mode as arguments. The mode can be 'r' for reading, 'w' for writing, 'a' for appending, and 'b' for binary mode.
```pythonfile = open('example.txt', 'r') # opens the file in read mode
```
# 2. Reading from a file - You can read the contents of a file using methods like `read()`, `readline()`, or `readlines()`.
```pythoncontent = file.read() # reads the entire content of the file
line = file.readline() # reads one line from the file
lines = file.readlines() # reads all lines and returns a list of lines
```
# 3. Writing to a file - You can write to a file using the `write()` method. If the file is opened in write mode ('w'), it will overwrite the existing content. If it's opened in append mode ('a'), it will add to the existing content.
```pythonfile = open('example.txt', 'w') # opens the file in write mode
file.write('Hello, World!') # writes a string to the file
```
# 4. Closing a file - It's important to close a file after you're done with it to free up system resources. You can use the `close()` method to close the file.
```pythonfile.close() # closes the file
```
# 5. Using `with` statement - A better way to handle files is to use the `with` statement, which ensures that the file is properly closed after its suite finishes, even if an exception is raised.
```pythonwith open('example.txt', 'r') as file:
    content = file.read() # reads the entire content of the file
```
# In this example, the file is automatically closed after the block of code is executed, even if an error occurs. This is a recommended practice for working with files in Python.

