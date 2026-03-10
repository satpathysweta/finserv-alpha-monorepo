import pytest
from decimal import Decimal
from src.interest_calculator import calculate_compound_interest, format_currency

def test_basic_interest():
    result = calculate_compound_interest(1000, 0.05, 2)
    assert result == Decimal("1102.5")

def test_precision():
    assert format_currency(100.055) == "$100.06"

# ── Edge-case tests (Gamma robust suite) ──────────────────────────

def test_zero_interest_rate():
    """Zero interest rate should return principal unchanged."""
    result = calculate_compound_interest(5000, 0, 10)
    assert result == Decimal("5000")

def test_negative_principal():
    """Negative principal (e.g. debt) should compound correctly."""
    result = calculate_compound_interest(-1000, 0.05, 2)
    assert result == Decimal("-1102.5")

def test_30_year_term_annual():
    """30-year term with annual compounding."""
    result = calculate_compound_interest(10000, 0.06, 30)
    expected = Decimal("10000") * (1 + Decimal("0.06")) ** 30
    assert result == expected

def test_30_year_term_monthly():
    """30-year term with monthly compounding (n=12)."""
    result = calculate_compound_interest(10000, 0.06, 30, n=12)
    expected = Decimal("10000") * (1 + Decimal("0.06") / 12) ** (12 * 30)
    assert result == expected

def test_zero_principal():
    """Zero principal should always return zero regardless of rate/time."""
    result = calculate_compound_interest(0, 0.05, 10)
    assert result == Decimal("0")
