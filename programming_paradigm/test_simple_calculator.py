from simple_calculator import SimpleCalculator 
import unittest


class TestSimpleCalculator(unittest.TestCase):
    def test_addition(self):
        result = SimpleCalculator.add(5, 3)
        self.assertEqual(result, 8) 
    def test_subtract_positive(self):
        result = SimpleCalculator.subtract(5, 3)
        self.assertEqual(result, 2) 
    def test_multiplication_positive(self):
        result = SimpleCalculator.multiply(5, 3)
        self.assertEqual(result, 15)
    def test_division_positive(self, a, b):
        assert b != 0, "Error: Division by zero!"

    SimpleCalculator()