num = 42
print(type(num))

# Arithmetic operations
print(num + 10)  # Output: 52
print(num - 5)   # Output: 37
print(num * 2)   # Output: 84
print(num / 2)   # Output: 21.0
print(num // 2)  # Output: 21 (floor division)
print(num % 5)   # Output: 2 (modulus)
print(num ** 2)  # Output: 1764 (exponentiation)

# Increment and decrement
num += 1  # Increment by 1
print(num)  # Output: 43

num -= 1  # Decrement by 1
print(num)  # Output: 42

num *= 2
print(num)  # Output: 84.0 (still a float)

num /= 2
print(num)  # Output: 21.0 (now it's a float)

# Absolute value
print(abs(-5))  # Output: 5

# Rounding
print(round(3.14159, 2))  # Output: 3.14
print(round(3.7696, 3))  # Output: 3.770

# Comparison operators
print(num > 20)  # Output: True
num_1 = 10
num_2 = 20

#  Equal: == 
print(num_1 == num_2)  # Output: False
# Not equal: !=
print(num_1 != num_2)  # Output: True
# Greater than: >
print(num_1 > num_2)  # Output: False
# Less than: <
print(num_1 < num_2)  # Output: True
# Greater than or equal to: >=
print(num_1 >= num_2)  # Output: False
# Less than or equal to: <=
print(num_2 <= num_1)  # Output: False


# Type conversion
num = 21
print(type(num))  # Output: <class 'int'>
print("Type conversion:")
num_str = str(num)  # Convert number to string
print(num_str)  # Output: '21'
print(type(num_str))  # Output: <class 'str'>
num_int = int(float(num_str))  # Convert string back to integer
print(num_int)  # Output: 21
print(type(num_int))  # Output: <class 'int'>
num_float = float(num_int)  # Convert integer to float
print(num_float)  # Output: 21.0
print(type(num_float))  # Output: <class 'float'>

# dir() function to list number methods
# print(dir(int))

# # TReating numbers from strings
# num_str2 = '123'
# num_str3 = '45.67'
# num_from_str = int(num_str2)  # Convert string to integer
# print(num_from_str)  # Output: 123
# num_from_str2 = float(num_str3)  # Convert string to float

# print(num_str2 + num_str3)  # Output: '12345.67' (string concatenation)