import pytest
import demo


def test_remove_1():
    assert demo.remove([1, 2, 3, 4], 3) == [1, 2, 4]


def test_remove_2():
    assert demo.remove([1, 2, 3, 4], 5) == [1, 2, 3, 4]


def test_remove_3():
    assert demo.remove([1, 2, 3, 4], 5) == [1, 2, 3, 4]
