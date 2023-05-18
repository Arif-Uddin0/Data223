import pytest
import unittest

from TDD import Calculator

calc = Calculator()

def test_add():
    result = calc.add(2, 3)
    assert result == 5

def test_subtract():
    result = calc.subtract(5, 2)
    assert result == 3

def test_multiply():
    result = calc.multiply(4, 3)
    assert result == 12

def test_divide():
    result = calc.divide(10, 2)
    assert result == 5


class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        result = self.calc.add(2, 3)
        self.assertEqual(result, 5)

    def test_subtract(self):
        result = self.calc.subtract(5, 2)
        self.assertEqual(result, 3)

    def test_multiply(self):
        result = self.calc.multiply(4, 3)
        self.assertEqual(result, 12)

    def test_divide(self):
        result = self.calc.divide(10, 2)
        self.assertEqual(result, 5)


if __name__ == '__main__':
    unittest.main()