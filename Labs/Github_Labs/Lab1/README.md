# Lab 1 - GitHub Actions CI/CD

Hrishikesh Prabhu | IE-7374 MLOps | Spring 2026

## About This Lab

This lab is about setting up a basic CI/CD pipeline using GitHub Actions. The idea is simple — write some Python functions, write tests for them, and let GitHub automatically run those tests every time you push code.

I started with the basic calculator functions from the course repo (add, subtract, multiply) and then added my own set of functions to make it more interesting.

## What I Added

I wrote 10 extra functions that go beyond basic math. Here's what they do:

- **celsius_to_fahrenheit / fahrenheit_to_celsius** — converts temperatures between C and F
- **percentage_change** — tells you the % increase or decrease between two values (handles divide by zero)
- **mean / median** — basic stats on a list of numbers, returns error for empty lists
- **is_palindrome** — checks if a word reads the same backwards (like "racecar")
- **count_vowels** — counts how many vowels are in a string
- **bmi_calculator** — calculates BMI from weight and height
- **flatten_list** — takes a nested list like [[1,2],[3,[4,5]]] and makes it flat [1,2,3,4,5]
- **grade_calculator** — gives you a letter grade (A/B/C/D/F) based on a score

Each function has proper error handling for edge cases like empty lists, zero division, negative numbers, etc.

## Project Structure

```
Lab1/
├── src/
│   └── calculator.py       # all the functions live here
├── test/
│   ├── test_pytest.py      # 27 tests using pytest
│   └── test_unittest.py    # 27 tests using unittest
├── workflows/              # yaml files for github actions
├── requirements.txt
└── README.md
```

## How to Run It Yourself

1. Clone the repo and go to Lab1
```bash
git clone https://github.com/MrHtp/MLOPS_github_lab1.git
cd MLOPS_github_lab1/Labs/Github_Labs/Lab1
```

2. Set up virtual environment
```bash
python3 -m venv lab_01
source lab_01/bin/activate
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Run the tests
```bash
pytest test/test_pytest.py
python3 -m unittest test.test_unittest
```

You should see all 27 tests passing for both.

## GitHub Actions

There are two workflows set up that run automatically when you push to main:

- One runs all the pytest tests
- Other one runs all the unittest tests

You can check the results in the Actions tab of this repo. Both are currently passing.

## What I Learned

- How to set up virtual environments to keep dependencies clean
- Writing tests with both pytest and unittest — pytest feels simpler but unittest gives more structure
- Setting up GitHub Actions YAML files and debugging them when paths are wrong (took a few tries to get right honestly)
- Importance of edge case testing — things like empty lists and zero division can break code silently if you don't test for them