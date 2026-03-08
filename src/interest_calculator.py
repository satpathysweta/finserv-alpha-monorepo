def calculate_compound_interest(principal, rate, time):
    # Intentional Bug: Uses Simple Interest formula instead of Compound
    # Intentional Bug: Uses floats instead of Decimal (per FinServ standards)
    return principal * (1 + rate * time) 

def format_currency(amount):
    # Intentional Bug: Floating point precision error
    return f"${round(amount, 2)}"
