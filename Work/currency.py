def usd(value: float) -> str:
    """Format a number as USD."""
    neg = '-' if value < 0 else ''
    return f"{neg}${abs(value):,.2f}"