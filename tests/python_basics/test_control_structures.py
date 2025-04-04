import pytest

def test_if_else_condition():
    number = 5
    if number > 0:
        result = "Positive"
    elif number < 0:
        result = "Negative"
    else:
        result = "Zero"
    
    assert result == "Positive"


def test_even_or_odd():
    number = 4
    result = "Even" if number % 2 == 0 else "Odd"
    assert result == "Even"

    number = 7
    result = "Even" if number % 2 == 0 else "Odd"
    assert result == "Odd"


def test_grade_evaluation():
    grade = 85
    if 90 <= grade <= 100:
        result = "A"
    elif 80 <= grade < 90:
        result = "B"
    elif 70 <= grade < 80:
        result = "C"
    elif 60 <= grade < 70:
        result = "D"
    else:
        result = "F"

    assert result == "B"


import pytest

def test_nested_if_statements():
    age = 20
    if age >= 18:
        if age >= 21:
            result = "Eligible to vote and drink"
        else:
            result = "Eligible to vote but not to drink"
    else:
        result = "Not an adult"

    assert result == "Eligible to vote but not to drink"

import pytest

def test_while_loop_countdown():
    n = 5
    countdown = []
    while n > 0:
        countdown.append(n)
        n -= 1
    assert countdown == [5, 4, 3, 2, 1]

