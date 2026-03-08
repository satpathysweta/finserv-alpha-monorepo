import pytest
from src.interest_calculator import calculate_compound_interest, format_currency

def test_basic_interest():
    # This will fail because the code uses simple interest
    assert calculate_compound_interest(1000, 0.05, 2) == 1102.5

def test_precision():
    # This often fails with floats: format_currency(100.055) might result in 100.05 or 100.06
    assert format_currency(100.055) == "$100.06"
