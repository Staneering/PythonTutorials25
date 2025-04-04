# Data Types in Python

# 1. Integer: Whole numbers (both positive and negative) without decimals.
# Integers are commonly used for counting, indexing, etc.

integer_num = 42
negative_integer = -10

# You can perform basic arithmetic operations with integers
sum_of_integers = integer_num + negative_integer  # Adding integers
difference_of_integers = integer_num - negative_integer  # Subtracting integers
product_of_integers = integer_num * negative_integer  # Multiplying integers
division_of_integers = integer_num / negative_integer  # Division of integers (results in float)

print("Integer Operations:")
print(f"Sum of integers: {sum_of_integers}")
print(f"Difference of integers: {difference_of_integers}")
print(f"Product of integers: {product_of_integers}")
print(f"Division of integers: {division_of_integers}")

# 2. Float: Numbers that represent decimal points or real numbers.
# Floats are used for measurements, scientific computations, or any time you need a more precise value.

float_num = 3.14159  # Pi value (approximately)
negative_float = -2.718  # Euler's number (approximately)

# Performing arithmetic with floats
sum_of_floats = float_num + negative_float  # Adding floats
product_of_floats = float_num * negative_float  # Multiplying floats
division_of_floats = float_num / negative_float  # Dividing floats

print("\nFloat Operations:")
print(f"Sum of floats: {sum_of_floats}")
print(f"Product of floats: {product_of_floats}")
print(f"Division of floats: {division_of_floats}")

# 3. String: A sequence of characters enclosed in either single or double quotes.
# Strings are used to represent text in Python.

greeting = "Hello"
name = "Alice"
sentence = greeting + ", " + name + "!"  # Concatenating strings

# You can access specific characters in a string using indexing
first_char = greeting[0]  # Access the first character
last_char = greeting[-1]  # Access the last character

# Strings are immutable, meaning you can't change an existing string directly, but you can create new strings.
modified_greeting = greeting.replace("Hello", "Hi")  # Replace a part of a string

print("\nString Operations:")
print(f"Concatenated sentence: {sentence}")
print(f"First character of greeting: {first_char}")
print(f"Last character of greeting: {last_char}")
print(f"Modified greeting: {modified_greeting}")

# 4. Boolean: Represents True or False.
# Booleans are typically used for decision-making (e.g., in conditional statements or loops).

is_sunny = True
is_raining = False

# Boolean operations
is_good_weather = is_sunny and not is_raining  # Checking if it's good weather (i.e., sunny and not raining)
is_bad_weather = not is_sunny or is_raining  # Checking if it's bad weather (i.e., not sunny or raining)

print("\nBoolean Operations:")
print(f"Is the weather good? {is_good_weather}")
print(f"Is the weather bad? {is_bad_weather}")

# 5. None: A special constant in Python that represents the absence of a value or a null value.
# It is often used to indicate that a variable has not been assigned any value yet.

no_value = None

print("\nNone Type:")
print(f"The value of no_value is: {no_value}")

# 6. Type Checking: You can check the type of a variable using the `type()` function.
# This is useful to confirm the data type of a value stored in a variable.

print("\nType Checking:")
print(f"The type of integer_num is: {type(integer_num)}")  # <class 'int'>
print(f"The type of float_num is: {type(float_num)}")  # <class 'float'>
print(f"The type of greeting is: {type(greeting)}")  # <class 'str'>
print(f"The type of is_sunny is: {type(is_sunny)}")  # <class 'bool'>
print(f"The type of no_value is: {type(no_value)}")  # <class 'NoneType'>
