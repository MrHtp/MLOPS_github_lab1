import unittest
from src.calculator import (
    fun1, fun2, fun3, fun4,
    celsius_to_fahrenheit, fahrenheit_to_celsius,
    percentage_change, mean, median,
    is_palindrome, count_vowels, bmi_calculator,
    flatten_list, grade_calculator
)

class TestCalculator(unittest.TestCase):

    # Original tests
    def test_fun1(self):
        self.assertEqual(fun1(2, 3), 5)

    def test_fun2(self):
        self.assertEqual(fun2(5, 3), 2)

    def test_fun3(self):
        self.assertEqual(fun3(3, 4), 12)

    def test_fun4(self):
        self.assertEqual(fun4(2, 3, 5), 10)

    # ---- Custom Tests by Hrishikesh Prabhu ----

    # Temperature conversions
    def test_celsius_to_fahrenheit_boiling(self):
        self.assertEqual(celsius_to_fahrenheit(100), 212)

    def test_celsius_to_fahrenheit_freezing(self):
        self.assertEqual(celsius_to_fahrenheit(0), 32)

    def test_fahrenheit_to_celsius(self):
        self.assertEqual(fahrenheit_to_celsius(212), 100)

    # Percentage change
    def test_percentage_change_increase(self):
        self.assertEqual(percentage_change(50, 75), 50.0)

    def test_percentage_change_decrease(self):
        self.assertEqual(percentage_change(100, 80), -20.0)

    def test_percentage_change_zero_base(self):
        self.assertEqual(percentage_change(0, 50), "Error")

    # Mean and Median
    def test_mean(self):
        self.assertEqual(mean([10, 20, 30, 40, 50]), 30.0)

    def test_mean_empty(self):
        self.assertEqual(mean([]), "Error")

    def test_median_odd(self):
        self.assertEqual(median([3, 1, 4, 1, 5]), 3)

    def test_median_even(self):
        self.assertEqual(median([1, 2, 3, 4]), 2.5)

    def test_median_empty(self):
        self.assertEqual(median([]), "Error")

    # String functions
    def test_palindrome_true(self):
        self.assertTrue(is_palindrome("Racecar"))

    def test_palindrome_false(self):
        self.assertFalse(is_palindrome("Python"))

    def test_count_vowels(self):
        self.assertEqual(count_vowels("Hrishikesh"), 3)

    def test_count_vowels_none(self):
        self.assertEqual(count_vowels("rhythm"), 0)

    # BMI
    def test_bmi_normal(self):
        self.assertEqual(bmi_calculator(70, 1.75), 22.86)

    def test_bmi_zero_height(self):
        self.assertEqual(bmi_calculator(70, 0), "Error")

    # Flatten list
    def test_flatten_simple(self):
        self.assertEqual(flatten_list([[1, 2], [3, 4]]), [1, 2, 3, 4])

    def test_flatten_deep(self):
        self.assertEqual(flatten_list([[1, [2, 3]], [4]]), [1, 2, 3, 4])

    # Grade calculator
    def test_grade_a(self):
        self.assertEqual(grade_calculator(95), "A")

    def test_grade_b(self):
        self.assertEqual(grade_calculator(85), "B")

    def test_grade_f(self):
        self.assertEqual(grade_calculator(45), "F")

    def test_grade_invalid(self):
        self.assertEqual(grade_calculator(110), "Invalid")

if __name__ == '__main__':
    unittest.main()