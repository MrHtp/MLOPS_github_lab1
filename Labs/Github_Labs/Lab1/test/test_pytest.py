from src.calculator import (
    fun1, fun2, fun3, fun4,
    celsius_to_fahrenheit, fahrenheit_to_celsius,
    percentage_change, mean, median,
    is_palindrome, count_vowels, bmi_calculator,
    flatten_list, grade_calculator
)

# Original tests
def test_fun1():
    assert fun1(2, 3) == 5

def test_fun2():
    assert fun2(5, 3) == 2

def test_fun3():
    assert fun3(3, 4) == 12

def test_fun4():
    assert fun4(2, 3, 5) == 10

# ---- Custom Tests by Hrishikesh Prabhu ----

# Temperature conversions
def test_celsius_to_fahrenheit_boiling():
    assert celsius_to_fahrenheit(100) == 212

def test_celsius_to_fahrenheit_freezing():
    assert celsius_to_fahrenheit(0) == 32

def test_fahrenheit_to_celsius():
    assert fahrenheit_to_celsius(212) == 100

# Percentage change
def test_percentage_change_increase():
    assert percentage_change(50, 75) == 50.0

def test_percentage_change_decrease():
    assert percentage_change(100, 80) == -20.0

def test_percentage_change_zero_base():
    assert percentage_change(0, 50) == "Error"

# Mean and Median
def test_mean():
    assert mean([10, 20, 30, 40, 50]) == 30.0

def test_mean_empty():
    assert mean([]) == "Error"

def test_median_odd():
    assert median([3, 1, 4, 1, 5]) == 3

def test_median_even():
    assert median([1, 2, 3, 4]) == 2.5

def test_median_empty():
    assert median([]) == "Error"

# String functions
def test_palindrome_true():
    assert is_palindrome("Racecar") == True

def test_palindrome_false():
    assert is_palindrome("Python") == False

def test_count_vowels():
    assert count_vowels("Hrishikesh") == 3

def test_count_vowels_none():
    assert count_vowels("rhythm") == 0

# BMI
def test_bmi_normal():
    assert bmi_calculator(70, 1.75) == 22.86

def test_bmi_zero_height():
    assert bmi_calculator(70, 0) == "Error"

# Flatten list
def test_flatten_simple():
    assert flatten_list([[1, 2], [3, 4]]) == [1, 2, 3, 4]

def test_flatten_deep():
    assert flatten_list([[1, [2, 3]], [4]]) == [1, 2, 3, 4]

# Grade calculator
def test_grade_a():
    assert grade_calculator(95) == "A"

def test_grade_b():
    assert grade_calculator(85) == "B"

def test_grade_f():
    assert grade_calculator(45) == "F"

def test_grade_invalid():
    assert grade_calculator(110) == "Invalid"