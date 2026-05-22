
##########################################################################
##########################################################################
# pytest
##########################################################################
##########################################################################
# pytest is a popular testing framework for Python that allows you to write simple and scalable test cases. It provides a powerful and flexible way to write tests, making it easier to identify and fix bugs in your code. Here's an example of how to use pytest to test a function that calculates the factorial of a number:

```pythondef factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result
def test_factorial():
    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(5) == 120
    try:
        factorial(-1)
    except ValueError as e:
        assert str(e) == "Factorial is not defined for negative numbers"
```
# Testing using folders (__init__.py)
# In pytest, you can organize your tests into folders to keep your test suite structured and manageable. To make a folder a Python package, you need to include an `__init__.py` file in that folder. This allows pytest to discover and run the tests contained within that folder. Here's an example of how to set up a test folder structure with an `__init__.py` file:
```
my_project/
├── src/
│   └── my_module.py
└── tests/
    ├── __init__.py
    └── test_my_module.py
```
# In this example, we have a project structure where the source code is located in the `src` folder and the tests are located in the `tests` folder. The `__init__.py` file in the `tests` folder allows pytest to recognize it as a package, enabling you to run the tests contained in `test_my_module.py`. You can run the tests using the command line by navigating to the root directory of your project and executing:
```pytest tests/
```
# This command will discover and run all the test files in the `tests` folder, including `test_my_module.py`, and report the results of the tests. By organizing your tests in this way, you can maintain a clean and efficient testing structure for your Python projects.