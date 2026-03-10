from decimal import Decimal, ROUND_HALF_UP


def calculate_compound_interest(principal, rate, time):
    """Calculate compound interest: A = P(1 + r/n)^(nt), with n=1 (annual compounding)."""
    P = Decimal(str(principal))
    r = Decimal(str(rate))
    t = Decimal(str(time))
    n = Decimal("1")
    A = P * (1 + r / n) ** (n * t)
    return A


def format_currency(amount):
    """Format amount as currency string with $ prefix, rounded to 2 decimal places."""
    d = Decimal(str(amount))
    rounded = d.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
    return f"${rounded}"
