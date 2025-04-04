import pytest
from src.data_structures.sets import my_set

def test_set_addition():
    my_set.add(6)
    assert 6 in my_set

def test_set_removal():
    my_set.remove(3)
    assert 3 not in my_set

def test_set_membership():
    assert 2 in my_set
    assert 7 not in my_set

def test_set_operations():
    set2 = {4, 5, 6, 7, 8}
    assert my_set.union(set2) == {1, 2, 4, 5, 6, 7, 8}
    assert my_set.intersection(set2) == {4, 5, 6}
    assert my_set.difference(set2) == {1, 2}

def test_set_iteration():
    result = []
    for item in my_set:
        result.append(item)
    assert result == [1, 2, 4, 5, 6]
