import pytest

def test_arithmetic_operators():
    num1 = 8
    num2 = 4
    assert (num1 + num2) == 12
    assert (num1 - num2) == 4
    assert (num1 * num2) == 32
    assert (num1 / num2) == 2
    assert (num1 % num2) == 0
    assert (num1 // num2) == 2
    assert (num1 ** num2) == 4096

def test_comparison_operators():
    num1 = 5
    num2 = 10
    assert (num1 == num2) == False
    assert (num1 != num2) == True
    assert (num1 > num2) == False
    assert (num1 < num2) == True
    assert (num1 >= num2) == False
    assert (num1 <= num2) == True

def test_logical_operators():
    x = True
    y = False
    assert (x and y) == False
    assert (x or y) == True
    assert (not x) == False

def test_modulo_floor_division():
    num1 = 10
    num2 = 3
    assert (num1 % num2) == 1
    assert (num1 // num2) == 3

def test_string_multiplication():
    string = "hello"
    times = 3
    assert (string * times) == "hellohellohello"