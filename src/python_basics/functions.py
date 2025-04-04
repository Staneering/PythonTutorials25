# Functions in Python

# 1. Simple function that adds two numbers
def add_numbers(a, b):
    return a + b

# 2. Function to find the maximum of two numbers
def find_max(a, b):
    return a if a > b else b

# 3. Function with default argument
def greet(name="Guest"):
    return f"Hello, {name}!"

# 4. Function returning multiple values
def get_name_and_length(name):
    return name, len(name)

# 5. Recursive function to calculate factorial
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Testing the functions
print(add_numbers(5, 7))  # 12
print(find_max(3, 9))  # 9
print(greet("Alice"))  # "Hello, Alice!"
print(greet())  # "Hello, Guest!"
print(get_name_and_length("Python"))  # ("Python", 6)
print(factorial(5))  # 120
