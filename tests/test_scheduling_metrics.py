import pytest


def test_basic_math_examples():
    assert 2 + 2 == 4
    assert 5 * 3 == 15


def test_simple_performance_formula():
    avg_wait = (5 + 3 + 2) / 3
    avg_turn = (10 + 7 + 6) / 3
    assert round(avg_wait, 2) == 3.33
    assert round(avg_turn, 2) == 7.67
