# Object Oriented Programming/OOP
class Employee:

    def __init__(self, first, last, pay):
        self.first = first.title()
        self.last = last.title()
        self.pay = pay
        self.email = first.lower() + '.' + last.lower() + '@company.com'
    
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'User', 60000)

print(emp_1.email)
print(emp_2.email)

# print Full Name
print(emp_1.fullname())
print(emp_2.fullname())


# Inheritance
# Inheritance means that we can create a class that inherits all the methods and properties from another class. The parent class is the class being inherited from, also called base class. The child class is the class that inherits from another class, also called derived class.
# Creating a subclass of Employee called Developer
class Developer(Employee):
    
    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang

dev_1 = Developer('Dereje', 'Masresha', 100000, 'Python')
dev_2 = Developer('Talja', 'Kalfu', 670000, 'Go')

# print(dev_1.email)
# print(dev_2.email)

# print(dev_1.fullname())
# print(dev_2.fullname())

# print(dev_1.prog_lang)
# print(dev_2.prog_lang)

class Manager(Employee):

    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_employee(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)
    
    def remove_employee(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)
    
    def print_employees(self):
        for emp in self.employees:
            print('-->', emp.fullname())

manager_1 = Manager('Sue', 'Smith', 90000, [dev_1])
print(manager_1.fullname())
print(manager_1.email)
manager_1.add_employee(dev_2)
manager_1.print_employees()

# isintance vs issubclass
print(isinstance(manager_1, Manager)) # True
print(isinstance(manager_1, Employee)) # True
print(isinstance(dev_1, Manager)) # False
print(isinstance(dev_1, Employee)) # True

print(issubclass(Developer, Employee)) # True
print(issubclass(Manager, Employee)) # True
print(issubclass(Manager, Developer)) # False

# isinstance and issubclass are built-in functions in Python that are used to check the type of an object or class. isinstance checks if an object is an instance of a class or a subclass thereof, while issubclass checks if a class is a subclass of another class.

# Difference
# isinstance is used to check the type of an object, while issubclass is used to check the relationship between classes.

# Decorators
# Decorators are a powerful and useful tool in Python that allow you to modify the behavior of a function or class. They are often used to add functionality to existing code without modifying the original code. A decorator is a function that takes another function as an argument and extends its behavior without explicitly modifying it.
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()

# In this example, we have a decorator function called my_decorator that takes a function as an argument and defines a wrapper function that adds some behavior before and after the original function is called. The @my_decorator syntax is used to apply the decorator to the say_hello function. When we call say_hello(), it will execute the wrapper function defined in the decorator, which will print the additional messages before and after calling the original say_hello function.

# Its expression without decorator
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

def say_hello():
    print("Hello!")

say_hello = my_decorator(say_hello)
say_hello()

# Advantage of using decorators is that they allow you to modify the behavior of a function or class without changing its source code. This can be particularly useful when you want to add functionality to existing code or when you want to apply the same behavior to multiple functions or classes without repeating code. Decorators also help in keeping your code clean and organized by separating concerns and allowing you to reuse code effectively.

# Decorators in class with muptile arguments
# Decorators can also be used in classes to modify the behavior of methods. When using decorators in classes, you can pass multiple arguments to the decorator function. Here's an example:


class MyClass:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print(f"Calling {self.func.__name__} with arguments: {args} and keyword arguments: {kwargs}")
        return self.func(*args, **kwargs)

@MyClass
def say_hello(name):
    print(f"Hello, my name is {name}!")

say_hello("John")

@MyClass
def list_fruits(name, *fruits):
    print(f"{name} has the following fruits: {', '.join(fruits)}")

list_fruits("Alice", "apple", "banana", "orange", "grape")

# Decorators are often used for logging.
# They work like interceptors: they catch a function call, do something before it,
# run the original function, then do something after it.

# Without a decorator, we must repeat the logging code in every function.
def create_user_without_decorator(username):
    print(f"Calling create_user_without_decorator with username: {username}")
    print(f"Creating user: {username}")
    print("Finished create_user_without_decorator")


def delete_user_without_decorator(username):
    print(f"Calling delete_user_without_decorator with username: {username}")
    print(f"Deleting user: {username}")
    print("Finished delete_user_without_decorator")


create_user_without_decorator("Sam")
delete_user_without_decorator("Sam")


# With a decorator, the logging code is written once and reused.
def logger(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with arguments: {args} and keyword arguments: {kwargs}")
        result = func(*args, **kwargs)
        print(f"Finished {func.__name__}")
        return result

    return wrapper


@logger
def create_user(username):
    print(f"Creating user: {username}")


@logger
def delete_user(username):
    print(f"Deleting user: {username}")


create_user("John")
delete_user("John")

# property decorator, setter, deleter, getter
# The @property decorator in Python is used to define a method as a property, which allows you to access it like an attribute. This is useful for creating read-only attributes or for adding logic when getting or setting an attribute. The @property decorator can be used in conjunction with the @setter and @deleter decorators to define setter and deleter methods for the property.
# The @property decorator allows you to define a method that can be accessed like an attribute. The @setter decorator allows you to define a method that is called when you try to set the value of the property. The @deleter decorator allows you to define a method that is called when you try to delete the property.
class Employee:
    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property
    def email(self):
        # return f"{self.first.lower()}.{self.last.lower()}@company.com"
        return '{}.{}@company.com'.format(self.first.lower(), self.last.lower())

    @property
    def fullname(self):
        return f"{self.first} {self.last}"

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print('Name deleted!')
        self.first = None
        self.last = None

emp_1 = Employee('Corey', 'Schafer')
print(emp_1.email)
print(emp_1.fullname)

emp_1.fullname = 'John Doe'
print(emp_1.email)
print(emp_1.fullname)
print(emp_1.first)
print(emp_1.last)

del emp_1.fullname

# How is getter applied in the above code?
# In the above code, the getter is applied using the @property decorator. The email and fullname methods are defined as properties, which means they can be accessed like attributes. When you access emp_1.email or emp_1.fullname, it calls the corresponding method and returns the value. The @property decorator allows you to define a method that can be accessed like an attribute, making it easier to work with class attributes while still allowing for additional logic when getting their values.