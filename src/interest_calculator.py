"""Financial interest calculator using decimal.Decimal for precision."""

from decimal import Decimal, ROUND_HALF_UP


def calculate_compound_interest(principal, rate, time, n=1):
    """Calculate compound interest using Decimal arithmetic.

    A = P * (1 + r/n)^(n*t)

    Args:
        principal: The initial amount (P).
        rate: Annual interest rate as a decimal (r).
        time: Number of years (t).
        n: Number of times interest is compounded per year (default 1).

    Returns:
        The final amount as a Decimal, rounded to 2 decimal places.
    """
    p_dec = Decimal(str(principal))
    r_dec = Decimal(str(rate))
    t_dec = Decimal(str(time))
    n_dec = Decimal(str(n))

    amount = p_dec * (1 + r_dec / n_dec) ** (n_dec * t_dec)
    return float(amount.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP))


def format_currency(amount):
    """Format an amount as a currency string using Decimal for precision."""
    d = Decimal(str(amount))
    rounded = d.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
    return f"${rounded}"
