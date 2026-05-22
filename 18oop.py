# Object Oriented Programming
# OOP is a programming paradigm that uses objects and classes to structure code. It allows for better organization, reusability, and maintainability of code.

# Tuples are immutable, meaning that once they are created, their values cannot be changed. This is in contrast to lists, which are mutable and can be modified after creation.
# Why is Returning multiple comma separated values a tuple?
# When you return multiple comma-separated values in Python, it creates a tuple because tuples are designed to hold a fixed number of items. The comma is used to separate the values, and the parentheses are optional when returning multiple values. This allows for easy packing and unpacking of values, making it convenient for functions that need to return multiple pieces of data without needing to create a custom class or data structure.
# Example of returning multiple values as a tuple
def get_user_info():
    name = "Alice"
    age = 30
    return name, age  # This will return a tuple (name, age)
user_info = get_user_info()
print(user_info)  # Output: ('Alice', 30)
# Example of unpacking the returned tuple
name, age = get_user_info()
print(name)  # Output: Alice
print(age)   # Output: 30

# Instead of unpacking the returned tuple, you can also access the values using indexing
user_info = get_user_info()
print(user_info[0])  # Output: Alice
print(user_info[1])  # Output: 30
print(f"Name: {user_info[0]}, Age: {user_info[1]}")  # Output: Name: Alice, Age: 30

# Issue: trying to change a value inside a tuple
# A function may return multiple values like this:
# return name, house
#
# Python stores those returned values in a tuple.
# Tuples can be read with indexes:
# student[0] gives the name
# student[1] gives the house
#
# But tuples cannot be changed after they are created.
# So this causes an error:
# student[1] = "Ravenclaw"
#
# Error:
# TypeError: 'tuple' object does not support item assignment

# Example of the problem
student = ("Padma", "Gryffindor")
print(student[0])  # Output: Padma
print(student[1])  # Output: Gryffindor

# This would crash the program because student is a tuple:
# student[1] = "Ravenclaw"

# If you want to change a value later, use a list instead of a tuple.
# Lists are mutable, so their values can be updated.
student = ["Padma", "Gryffindor"]
student[1] = "Ravenclaw"
print(f"{student[0]} from {student[1]}")  # Output: Padma from Ravenclaw

# Short rule:
# Use a tuple when the values should stay fixed.
# Use a list when the values may need to change.

# Even in returining multiple values, if you want to change the values later, you can return a list instead of a tuple. like:
def get_student_info():
    name = "Padma"
    house = "Gryffindor"
    return [name, house]  # This will return a list [name, house]
student_info = get_student_info()
print(student_info)  # Output: ['Padma', 'Gryffindor']
student_info[1] = "Ravenclaw"
print(f"{student_info[0]} from {student_info[1]}")  # Output: Padma from Ravenclaw

# In summary, tuples are immutable and are used when you want to return multiple values that should not change, while lists are mutable and are used when you want to return multiple values that may need to be updated later.

# Dictionaries (Dicts) are a collection of key-value pairs. They are mutable, meaning that you can change their contents after they have been created. Dicts are useful for storing and organizing data in a way that allows for fast lookups based on keys.
# Example of a dictionary
student = {
    "name": "Padma",
    "house": "Gryffindor",
    "age": 20
}
print(student)  # Output: {'name': 'Padma', 'house': 'Gryffindor', 'age': 20}
print(student["name"])  # Output: Padma
print(student["house"])  # Output: Gryffindor
print(student["age"])   # Output: 20

# Classes are a fundamental part of object-oriented programming (OOP) in Python. 
# A class is a blueprint for creating objects, which are instances of the class. Classes can have attributes (data) and methods (functions) that operate on the data. They allow you to model real-world entities and their behaviors in your code.
# Creating a class in Python is done using the `class` keyword, followed by the class name (it starts with a capital letter by convention). Inside the class, you can define an `__init__` method, which is a special method that is called when an object is created. This method is used to initialize the attributes of the object.
# Example of a class
class Student:
    ...

def get_student_info():
    # student = Student()
    # student.name = input("Name: ")
    # student.house = input("House: ")
    # Other good syntax:
    name = input("Name: ")
    house = input("House: ")
    student = Student(name, house)
    return student

def main():
    student = get_student_info()
    # if student.name == "Padma":
    #      student.house = "Ravenclaw"
    print(f"{student.name} from {student.house}")

if __name__ == "__main__":
    main()


# Class vs Object:
# A class is a blueprint or template for creating objects. It defines the structure and behavior of the objects that will be created from it. 
# An object, on the other hand, is an instance of a class. It is a specific realization of the class with actual values for its attributes.
# Instance mean here: When you create an object from a class, that object is called an instance of the class. Each instance can have its own unique values for the attributes defined in the class. For example, if you have a class called `Student`, you can create multiple instances of that class, each representing a different student with their own name and house.
# Example of class vs object
class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house
# Creating an instance of the Student class
student1 = Student("Padma", "Gryffindor")
student2 = Student("Harry", "Gryffindor")
print(student1.name)  # Output: Padma
print(student1.house)  # Output: Gryffindor
print(student2.name)  # Output: Harry
print(student2.house)  # Output: Gryffindor

# Methods
# Methods are functions that are defined inside a class and operate on instances of that class. They can access and modify the attributes of the instance. Methods are used to define the behaviors of the objects created from the class.
# __init__ and instance methods:
# The `__init__` method is a special method in Python classes that is called when an object is created. It is used to initialize the attributes of the object. The `self` parameter in the `__init__` method refers to the instance of the class that is being created. It allows you to set the attributes of the instance using the values passed to the `__init__` method.

# IF we don't use __init__ method and self parameter, we would have to manually set the attributes for each instance of the class, which can be cumbersome and error-prone. The `__init__` method provides a convenient way to initialize the attributes of an object when it is created, ensuring that each instance has the necessary data to function properly. for self parameter, it allows us to access the attributes and methods of the instance within the class, making it possible to define behaviors that operate on the instance's data.

# Validating input in __init__ method:
class Student:
    def __init__(self, name, house):
        if not name:
            raise ValueError("Missing name")
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self.name = name
        self.house = house
# Example of creating a student with valid input
try:
    student1 = Student("Padma", "Gryffindor")
    print(student1.name)  # Output: Padma
    print(student1.house)  # Output: Gryffindor
except ValueError as e:
    print(e)
# Example of creating a student with invalid input
try:
    student2 = Student("", "Gryffindor")
except ValueError as e:
    print(e)  # Output: Missing name

# Purpose of self parameter:
# The `self` parameter in Python class methods is a reference to the instance of the class that is being created or accessed. It allows you to access and modify the attributes and methods of the instance within the class. When you define a method in a class, you need to include `self` as the first parameter, even though you don't pass it when calling the method. This is because Python automatically passes the instance as the first argument to the method when it is called on an object.

# Purpose of raise keyword:
# The `raise` keyword in Python is used to trigger an exception. It allows you to signal that an error has occurred in your code and to provide information about the error. When you use `raise`, you can specify the type of exception you want to raise, along with an optional error message. This is useful for validating input, handling errors, and ensuring that your code behaves as expected. For example, if you want to validate that a user has entered a valid name and house when creating a `Student` object, you can use `raise` to throw a `ValueError` if the input is invalid, as shown in the previous example. This helps to prevent the creation of objects with invalid data and allows you to handle errors gracefully in your code.

# __str__ method:
# The `__str__` method in a Python class is a special method that is called when you use the `str()` function on an instance of the class or when you print the instance. It is used to define a human-readable string representation of the object. By implementing the `__str__` method, you can control how the object is represented as a string, which can be useful for debugging and displaying information about the object in a user-friendly way. For example, if you have a `Student` class, you can implement the `__str__` method to return a string that includes the student's name and house, making it easier to understand the output when you print a `Student` object. Here's an example:
class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house
    def __str__(self):
        return f"{self.name} from {self.house}"
def main():
    student = Student("Padma", "Gryffindor")
    print(student)  # Output: Padma from Gryffindor

if __name__ == "__main__":
    main()

# What happens if you don't implement the __str__ method?
# If you don't implement the `__str__` method in a Python class, when you try to print an instance of that class or convert it to a string using the `str()` function, you will get a default string representation of the object that includes the class name and the memory address of the instance. This default representation is not very informative and can be difficult to understand, especially when you have multiple instances of the same class. For example, if you have a `Student` class without a `__str__` method, printing an instance of the class would result in output like `<__main__.Student object at 0x7f8b8c2d9d0>`, which does not provide any useful information about the student's name or house. Implementing the `__str__` method allows you to provide a more meaningful and human-readable representation of the object, making it easier to understand the output when you print an instance of the class.

# Properties:
# Properties in Python are a way to manage the access and modification of an object's attributes. They allow you to define methods that are accessed like attributes, providing a way to add logic for getting, setting, and deleting attributes. This is useful for encapsulating the internal state of an object and controlling how attributes are accessed and modified. By using properties, you can ensure that certain conditions are met when getting or setting an attribute, and you can also provide a way to compute the value of an attribute on the fly. For example, you can use properties to validate input when setting an attribute or to compute a value based on other attributes when getting an attribute. This helps to maintain the integrity of the object's state and allows for more flexible and maintainable code. Here's an example of using properties in a `Student` class:
# decorator @property is used to define a method as a property, allowing you to access it like an attribute. The setter method is defined using the @property_name.setter decorator, which allows you to set the value of the property while also performing validation or other logic.
class Student:
