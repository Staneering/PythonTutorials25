import pytest

def add_numbers(a, b):
    return a + b

def test_add_numbers():
    assert add_numbers(2, 3) == 5
    assert add_numbers(-1, 1) == 0

def find_max(a, b):
    return a if a > b else b

def test_find_max():
    assert find_max(2, 3) == 3
    assert find_max(5, 3) == 5


def greet(name="Guest"):
    return f"Hello, {name}!"

def test_greet():
    assert greet("Alice") == "Hello, Alice!"
    assert greet() == "Hello, Guest!"

def get_name_and_length(name):
    return name, len(name)

def test_get_name_and_length():
    assert get_name_and_length("Python") == ("Python", 6)
    assert get_name_and_length("Test") == ("Test", 4)


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def test_factorial():
    assert factorial(0) == 1
    assert factorial(5) == 120
    assert factorial(3) == 6



