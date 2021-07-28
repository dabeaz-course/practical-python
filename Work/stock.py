class Stock:
    """
    Represent a single holding of stock.
    """

    def __init__(self, name: str, shares: int, price: float) -> None:
        self.name = name
        self.shares = shares
        self.price = price
