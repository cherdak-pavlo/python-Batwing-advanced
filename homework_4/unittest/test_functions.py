import unittest
from functions_to_test import Calculator


class TestFunctions(unittest.TestCase):

    def test_class_add(self):
        self.assertEqual(Calculator.add(32, 16), 48)
        self.assertEqual(Calculator.add(-16, 33), 17)

    def test_class_subtract(self):
        self.assertEqual(Calculator.subtract(58, 18), 40)
        self.assertEqual(Calculator.subtract(120, -20), 140)
        self.assertNotEqual(Calculator.subtract(-20, -20), -40)

    def test_class_multiply(self):
        self.assertEqual(Calculator.multiply(27, 2), 54)
        self.assertEqual(Calculator.multiply(100, -10), -1000)

    def test_class_divide(self):
        self.assertEqual(Calculator.divide(99, 3), 33)
        self.assertRaises(ValueError, Calculator.divide, 57, 0)


if __name__ == '__main__':
    unittest.main()
