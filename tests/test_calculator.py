import math
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from app.calculator import add, cos, divide, multiply, pow, set_precision, sin, sqrt, subtract


class TestAdd(unittest.TestCase):
    def test_two_numbers(self):
        self.assertEqual(add([1, 2]), 3.0)

    def test_decimal_precision(self):
        self.assertEqual(add([0.1, 0.2]), 0.3)

    def test_multiple_numbers(self):
        self.assertEqual(add([1, 2, 3]), 6.0)

    def test_too_few_numbers(self):
        with self.assertRaises(ValueError):
            add([5])


class TestSubtract(unittest.TestCase):
    def test_two_numbers(self):
        self.assertEqual(subtract([10, 3]), 7.0)

    def test_sequential(self):
        self.assertEqual(subtract([10, 3, 2]), 5.0)

    def test_too_few_numbers(self):
        with self.assertRaises(ValueError):
            subtract([5])


class TestMultiply(unittest.TestCase):
    def test_two_numbers(self):
        self.assertEqual(multiply([2, 3]), 6.0)

    def test_multiple_numbers(self):
        self.assertEqual(multiply([2, 3, 4]), 24.0)

    def test_too_few_numbers(self):
        with self.assertRaises(ValueError):
            multiply([5])


class TestDivide(unittest.TestCase):
    def test_two_numbers(self):
        self.assertEqual(divide([10, 2]), 5.0)

    def test_sequential(self):
        self.assertEqual(divide([24, 2, 3]), 4.0)

    def test_division_by_zero(self):
        with self.assertRaises(ValueError):
            divide([10, 0])

    def test_too_few_numbers(self):
        with self.assertRaises(ValueError):
            divide([5])


class TestPow(unittest.TestCase):
    def test_positive_base(self):
        self.assertEqual(pow(2, 3), 8.0)

    def test_negative_base_integer_exponent(self):
        self.assertEqual(pow(-2, 3), -8.0)

    def test_negative_base_fractional_exponent(self):
        with self.assertRaises(ValueError):
            pow(-2, 0.5)


class TestSqrt(unittest.TestCase):
    def test_perfect_square(self):
        self.assertEqual(sqrt(9), 3.0)

    def test_negative_number(self):
        with self.assertRaises(ValueError):
            sqrt(-1)


class TestSetPrecision(unittest.TestCase):
    def test_valid_precision(self):
        self.assertEqual(set_precision(10), "Precision set to 10")

    def test_below_range(self):
        with self.assertRaises(ValueError):
            set_precision(-1)

    def test_above_range(self):
        with self.assertRaises(ValueError):
            set_precision(29)


class TestSin(unittest.TestCase):
    def test_zero(self):
        self.assertEqual(sin(0), 0.0)

    def test_half_pi(self):
        self.assertAlmostEqual(sin(math.pi / 2), 1.0)


class TestCos(unittest.TestCase):
    def test_zero(self):
        self.assertEqual(cos(0), 1.0)

    def test_pi(self):
        self.assertAlmostEqual(cos(math.pi), -1.0)


if __name__ == "__main__":
    unittest.main()
