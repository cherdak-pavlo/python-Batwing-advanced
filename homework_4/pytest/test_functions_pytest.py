import pytest
from functions_to_test import Calculator


def test_add():
    assert Calculator.add(1337, 228) == 1565
    assert Calculator.add(-20, 25) == 5


def test_subtract():
    assert Calculator.subtract(1337, 228) == 1109
    assert Calculator.subtract(-20, 25) != 5


def test_multiply():
    assert Calculator.multiply(18, 2) == 36
    assert Calculator.multiply(-20, 2) != -41


def test_divide():
    assert Calculator.divide(10, 2) != 0
    assert Calculator.divide(10, 2) == 5
    with pytest.raises(ValueError):
        Calculator.divide(4, 0)
