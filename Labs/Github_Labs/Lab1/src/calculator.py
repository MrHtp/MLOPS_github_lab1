def fun1(x, y):
    """Adds two numbers together."""
    return x + y

def fun2(x, y):
    """Subtracts y from x."""
    return x - y

def fun3(x, y):
    """Multiplies two numbers together."""
    return x * y

def fun4(x, y, z):
    """Adds three numbers together."""
    total_sum = x + y + z
    return total_sum

# ---- Custom Analytics Toolkit by Hrishikesh Prabhu ----

def celsius_to_fahrenheit(temp):
    """Converts Celsius to Fahrenheit."""
    return (temp * 9/5) + 32

def fahrenheit_to_celsius(temp):
    """Converts Fahrenheit to Celsius."""
    return (temp - 32) * 5/9

def percentage_change(old_val, new_val):
    """Calculates percentage change between two values.
    Returns 'Error' if old value is zero.
    """
    if old_val == 0:
        return "Error"
    return round(((new_val - old_val) / old_val) * 100, 2)

def mean(numbers):
    """Returns the mean of a list of numbers.
    Returns 'Error' if list is empty.
    """
    if not numbers:
        return "Error"
    return sum(numbers) / len(numbers)

def median(numbers):
    """Returns the median of a list of numbers.
    Returns 'Error' if list is empty.
    """
    if not numbers:
        return "Error"
    sorted_nums = sorted(numbers)
    n = len(sorted_nums)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_nums[mid - 1] + sorted_nums[mid]) / 2
    return sorted_nums[mid]

def is_palindrome(text):
    """Checks if a string is a palindrome (case-insensitive)."""
    cleaned = text.lower().replace(" ", "")
    return cleaned == cleaned[::-1]

def count_vowels(text):
    """Returns the count of vowels in a string."""
    return sum(1 for ch in text.lower() if ch in "aeiou")

def bmi_calculator(weight_kg, height_m):
    """Calculates BMI given weight in kg and height in meters.
    Returns 'Error' if height is zero or negative.
    """
    if height_m <= 0:
        return "Error"
    return round(weight_kg / (height_m ** 2), 2)

def flatten_list(nested):
    """Flattens a nested list into a single list.
    Example: [[1,2],[3,4]] -> [1,2,3,4]
    """
    result = []
    for item in nested:
        if isinstance(item, list):
            result.extend(flatten_list(item))
        else:
            result.append(item)
    return result

def grade_calculator(score):
    """Returns letter grade based on score.
    A: 90-100, B: 80-89, C: 70-79, D: 60-69, F: below 60
    Returns 'Invalid' for scores outside 0-100.
    """
    if score < 0 or score > 100:
        return "Invalid"
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    return "F"