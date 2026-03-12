from decimal import Decimal
from src.interest_calculator import calculate_compound_interest, format_currency


def test_basic_interest():
    # Compound interest: A = 1000 * (1 + 0.05)^2 = 1102.50
    assert calculate_compound_interest(1000, 0.05, 2) == Decimal("1102.50")


def test_precision():
    # ROUND_HALF_UP: 100.055 -> $100.06
    assert format_currency(100.055) == "$100.06"


# ── Edge-case tests (Agent Gamma) ──────────────────────────────────────


def test_zero_principal():
    """Zero principal must always yield zero regardless of rate/time."""
    assert calculate_compound_interest(0, 0.05, 10) == Decimal("0.00")


def test_zero_rate():
    """A 0% interest rate must return the original principal unchanged."""
    assert calculate_compound_interest(1000, 0, 5) == Decimal("1000.00")


def test_zero_time():
    """Zero time horizon must return the original principal unchanged."""
    assert calculate_compound_interest(5000, 0.10, 0) == Decimal("5000.00")


def test_sub_annual_compounding():
    """Monthly compounding (n=12) must differ from annual compounding."""
    annual = calculate_compound_interest(1000, 0.12, 1, n=1)
    monthly = calculate_compound_interest(1000, 0.12, 1, n=12)
    # Monthly compounding yields more than annual
    assert monthly > annual
    # Expected: 1000 * (1 + 0.12/12)^12 = 1126.83
    assert monthly == Decimal("1126.83")


def test_format_currency_half_penny_rounds_up():
    """Exact half-cent values must round UP per ROUND_HALF_UP policy."""
    assert format_currency(99.995) == "$100.00"
    assert format_currency(0.005) == "$0.01"
    assert format_currency(1234.565) == "$1234.57"
