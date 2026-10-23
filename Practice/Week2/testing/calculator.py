# calculator.py
"""A tiny module we want to test."""


def add(a, b):
    return a + b


def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("cannot divide by zero")
    return a / b


def is_even(n):
    return n % 2 == 0


def pass_rate(results):
    """Percentage of 'pass' outcomes (case-insensitive); 0.0 for an empty list."""
    if not results:
        return 0.0
    passed = sum(1 for outcome in results if outcome.lower() == "pass")
    return passed / len(results) * 100