import pytest
from src.data_structures.tuples import my_tuple

def test_tuple_access():
    assert my_tuple[1] == 20
    assert my_tuple[-1] == "banana"

def test_tuple_immutable():
    try:
        my_tuple[2] = 40
    except TypeError:
        pass  # Expected error
    else:
        pytest.fail("Tuple should be immutable")

def test_tuple_length():
    assert len(my_tuple) == 5

def test_tuple_count():
    assert my_tuple.count("apple") == 1

def test_tuple_unpacking():
    a, b, c, d, e = my_tuple
    assert a == 10
    assert e == "banana"
