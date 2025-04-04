import pytest
from src.data_structures.dictionaries import my_dict

def test_dict_addition():
    my_dict["graduation_year"] = 2023
    assert my_dict["graduation_year"] == 2023

def test_dict_access():
    assert my_dict["name"] == "Alice"
    assert my_dict["age"] == 25

def test_dict_iteration():
    keys = list(my_dict.keys())
    values = list(my_dict.values())
    assert keys == ["name", "age", "city", "graduation_year"]
    assert values == ["Alice", 25, "New York", 2023]

def test_dict_check_key():
    assert "major" not in my_dict

def test_dict_remove():
    del my_dict["major"]
    assert "major" not in my_dict
