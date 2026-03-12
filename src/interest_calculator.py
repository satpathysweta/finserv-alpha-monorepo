from decimal import Decimal, ROUND_HALF_UP


def calculate_compound_interest(principal, rate, time, n=1):
    """Calculate compound interest using A = P * (1 + r/n)^(n*t).

    All arithmetic is performed with decimal.Decimal to avoid
    floating-point precision drift mandated by FinServ standards.

    Args:
        principal: The initial investment amount.
        rate: Annual interest rate (e.g. 0.05 for 5%).
        time: Number of years.
        n: Compounding frequency per year (default: 1 for annual).

    Returns:
        Decimal result rounded to 2 decimal places.
    """
    p = Decimal(str(principal))
    r = Decimal(str(rate))
    t = Decimal(str(time))
    n_d = Decimal(str(n))

    amount = p * (1 + r / n_d) ** (n_d * t)
    return amount.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

def format_currency(amount):
    """Format a numeric amount as a USD currency string.

    Converts to Decimal first to ensure correct rounding behaviour
    (ROUND_HALF_UP) and avoid IEEE-754 precision errors.
    """
    d = Decimal(str(amount))
    rounded = d.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
    return f"${rounded}"
