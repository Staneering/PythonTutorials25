import pytest
from src.data_structures.lists import my_list

def test_list_addition():
    my_list.append(6)
    assert 6 in my_list

def test_list_modification():
    my_list[1] = 10
    assert my_list[1] == 10

def test_list_indexing():
    assert my_list[0] == 1
    assert my_list[-1] == 6

def test_list_slicing():
    assert my_list[:3] == [1, 10, 3]

def test_list_iteration():
    result = []
    for item in my_list:
        result.append(item)
    assert result == [1, 10, 3, 4, 5, 6]
