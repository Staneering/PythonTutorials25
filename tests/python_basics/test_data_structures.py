import pytest

# Test for Exercise 1: List Sum
def test_list_sum():
    nums = [1, 2, 3, 4, 5]
    assert sum(nums) == 15

# Test for Exercise 2: List Indexing
def test_list_indexing():
    fruits = ["apple", "banana", "cherry"]
    assert fruits[0] == "apple"
    assert fruits[-1] == "cherry"

# Test for Exercise 3: Dictionary Lookup
def test_dictionary_lookup():
    fruit_colors = {"apple": "red", "banana": "yellow", "cherry": "red"}
    assert fruit_colors["apple"] == "red"
    assert fruit_colors["banana"] == "yellow"

# Test for Exercise 4: List Comprehension
def test_list_comprehension():
    squares = [x**2 for x in range(1, 6)]
    assert squares == [1, 4, 9, 16, 25]

# Test for Exercise 5: Merge Two Lists
def test_merge_lists():
    list1 = [1, 2, 3]
    list2 = [4, 5, 6]
    merged_list = list1 + list2
    assert merged_list == [1, 2, 3, 4, 5, 6]
