class Stock:
    """
    Represent a single holding of stock.
    """

    def __init__(self, name: str, shares: int, price: float) -> None:
        self.name = name
        self.shares = shares
        self.price = price

    def cost(self) -> float:
        return self.shares * self.price

    def sell(self, shares: int) -> None:
        self.shares -= shares
