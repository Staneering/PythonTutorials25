import pytest

def test_integer_float_operations():
    num1 = 5
    num2 = 3.14
    assert (num1 + num2) == 8.14
    assert (num1 - num2) == 1.8599999999999999
    assert (num1 * num2) == 15.7
    assert (num1 / num2) == 1.5923566878980892


def test_string_concatenation():
    first_name = "John"
    last_name = "Doe"
    assert (first_name + " " + last_name) == "John Doe"


def test_boolean_logic():
    x = True
    y = False
    assert (x and y) == False
    assert (x or y) == True
    assert not x == False


def test_data_type_conversion():
    str_num = "25"
    assert int(str_num) == 25
    assert float(str_num) == 25.0

def test_none_type():
    unknown = None
    assert type(unknown) == type(None)