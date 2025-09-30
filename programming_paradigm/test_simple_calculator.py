import unittest
from simple_calculator import SimpleCalculator


class TestSimpleCalculator(unittest.TestCase):
    """Unit tests for the SimpleCalculator class."""

    def setUp(self):
        """Create a SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    # --- Addition Tests ---
    def test_addition_positive_numbers(self):
        self.assertEqual(self.calc.add(2, 3), 5)

    def test_addition_negative_numbers(self):
        self.assertEqual(self.calc.add(-2, -3), -5)

    def test_addition_mixed_numbers(self):
        self.assertEqual(self.calc.add(-2, 5), 3)

    def test_addition_with_zero(self):
        self.assertEqual(self.calc.add(0, 7), 7)

    # --- Subtraction Tests ---
    def test_subtraction_positive_numbers(self):
        self.assertEqual(self.calc.subtract(10, 4), 6)

    def test_subtraction_negative_result(self):
        self.assertEqual(self.calc.subtract(4, 10), -6)

    def test_subtraction_with_zero(self):
        self.assertEqual(self.calc.subtract(7, 0), 7)

    def test_subtraction_of_same_numbers(self):
        self.assertEqual(self.calc.subtract(5, 5), 0)

    # --- Multiplication Tests ---
    def test_multiplication_positive_numbers(self):
        self.assertEqual(self.calc.multiply(3, 4), 12)

    def test_multiplication_negative_numbers(self):
        self.assertEqual(self.calc.multiply(-2, -3), 6)

    def test_multiplication_mixed_numbers(self):
        self.assertEqual(self.calc.multiply(-2, 3), -6)

    def test_multiplication_with_zero(self):
        self.assertEqual(self.calc.multiply(5, 0), 0)

    # --- Division Tests ---
    def test_division_normal_case(self):
        self.assertEqual(self.calc.divide(10, 2), 5)

    def test_division_fraction_result(self):
        self.assertAlmostEqual(self.calc.divide(7, 2), 3.5)

    def test_division_negative_numbers(self):
        self.assertEqual(self.calc.divide(-6, -3), 2)

    def test_division_mixed_signs(self):
        self.assertEqual(self.calc.divide(-9, 3), -3)

    def test_division_by_zero(self):
        self.assertIsNone(self.calc.divide(5, 0))

    def test_zero_divided_by_number(self):
        self.assertEqual(self.calc.divide(0, 7), 0)


if __name__ == "__main__":
    unittest.main()
