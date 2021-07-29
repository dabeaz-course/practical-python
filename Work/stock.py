class Stock:
    """
    Represent a single holding of stock.
    """
    __slots__ = ('name', '_shares', 'price')

    def __init__(self, name: str, shares: int, price: float) -> None:
        self.name = name
        self.shares = shares
        self.price = price

    @property
    def shares(self) -> int:
        return self._shares

    @shares.setter
    def shares(self, value: int) -> None:
        if not isinstance(value, int):
            raise TypeError('Expected int')
        self._shares = value

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}({self.name!r}, {self.shares!r}, {self.price!r})'

    @property
    def cost(self) -> float:
        return self.shares * self.price

    def sell(self, shares: int) -> None:
        self.shares -= shares
