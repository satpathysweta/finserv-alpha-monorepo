from decimal import Decimal, ROUND_HALF_UP


def calculate_compound_interest(principal, rate, time, n=1):
    """Calculate compound interest using A = P(1 + r/n)^(nt) with decimal.Decimal."""
    P = Decimal(str(principal))
    r = Decimal(str(rate))
    t = Decimal(str(time))
    n_d = Decimal(str(n))
    A = P * (1 + r / n_d) ** (n_d * t)
    return A


def format_currency(amount):
    """Format amount as currency string with $ prefix, rounded to 2 decimal places."""
    d = Decimal(str(amount))
    rounded = d.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
    return f"${rounded}"
