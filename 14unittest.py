# Unit test
# Unit testing is a software testing technique where individual units or components of a software application are tested in isolation to ensure that they work as expected. The main goal of unit testing is to validate that each unit of the software performs as designed, which helps to identify and fix bugs early in the development process.
# In Python, the built-in `unittest` module is commonly used for writing and running unit tests. Here's a simple example of how to use `unittest` to test a function that adds two numbers:

```pythonimport unittest
def add(a, b):
    return a + b
class TestAddFunction(unittest.TestCase):
    def test_add_positive_numbers(self):
        self.assertEqual(add(2, 3), 5)
    def test_add_negative_numbers(self):
        self.assertEqual(add(-1, -1), -2)
    def test_add_mixed_numbers(self):
        self.assertEqual(add(-1, 1), 0)
if __name__ == '__main__':
    unittest.main()
```
# In this example, we define a function `add` that takes two parameters and returns their sum. We then create a test case class `TestAddFunction` that inherits from `unittest.TestCase`. Inside this class, we define several test methods to check the behavior of the `add` function with different types of input (positive numbers, negative numbers, and mixed numbers). Finally, we call `unittest.main()` to run the tests when the script is executed.

# When you run this code, it will execute the tests and report the results, indicating whether each test passed or failed. This helps ensure that the `add` function works correctly under various conditions.

# assert
# The `assert` statement in Python is used to test if a condition is true. If the condition is false, it raises an `AssertionError` with an optional error message. This is commonly used in unit testing to verify that certain conditions hold true during the execution of tests. Here's an example of how to use `assert` in a unit test:

```pythonimport unittest
def multiply(a, b):
    return a * b
class TestMultiplyFunction(unittest.TestCase):
    def test_multiply_positive_numbers(self):
        self.assertEqual(multiply(2, 3), 6)
    def test_multiply_negative_numbers(self):
        self.assertEqual(multiply(-1, -1), 1)
    def test_multiply_mixed_numbers(self):
        self.assertEqual(multiply(-1, 1), -1)
if __name__ == '__main__':
    unittest.main()
```
# In this example, we define a function `multiply` that takes two parameters and returns their product. We then create a test case class `TestMultiplyFunction` that inherits from `unittest.TestCase`. Inside this class, we define several test methods to check the behavior of the `multiply` function with different types of input (positive numbers, negative numbers, and mixed numbers). We use `self.assertEqual()` to assert that the output of the `multiply` function matches the expected result for each test case. Finally, we call `unittest.main()` to run the tests when the script is executed.

# AssertionError
# An `AssertionError` is an exception that is raised when an `assert` statement fails. This typically occurs in unit testing when a test case does not meet the expected conditions. When an `AssertionError` is raised, it indicates that the test has failed, and it can include an optional error message to provide more context about the failure. Here's an example of how an `AssertionError` might occur in a unit test:
```pythonimport unittest
def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
class TestDivideFunction(unittest.TestCase):
    def test_divide_positive_numbers(self):
        self.assertEqual(divide(10, 2), 5)
    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            divide(10, 0)
if __name__ == '__main__':
    unittest.main()
```
# In this example, we define a function `divide` that takes two parameters and returns their quotient. If the second parameter is zero, it raises a `ValueError`. We then create a test case class `TestDivideFunction` that inherits from `unittest.TestCase`. Inside this class, we define two test methods: one to test dividing positive numbers and another to test dividing by zero. The second test method uses `self.assertRaises()` to assert that a `ValueError` is raised when attempting to divide by zero. If the `divide` function does not raise the expected exception, an `AssertionError` will be raised, indicating that the test has failed. Finally, we call `unittest.main()` to run the tests when the script is executed.
