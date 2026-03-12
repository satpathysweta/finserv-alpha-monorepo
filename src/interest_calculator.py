from decimal import Decimal, ROUND_HALF_UP

def calculate_compound_interest(principal, rate, time):
    return principal * (1 + rate) ** time

def format_currency(amount):
    rounded = Decimal(str(amount)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
    return f"${rounded}"
