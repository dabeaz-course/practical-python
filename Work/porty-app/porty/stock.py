from .typedproperty import Float, Integer, String


class Stock:
    """
    Represent a single holding of stock.
    """
    name = String('name')
    shares = Integer('shares')
    price = Float('price')

    def __init__(self, name: str, shares: int, price: float) -> None:
        self.name = name
        self.shares = shares
        self.price = price

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}({self.name!r}, {self.shares!r}, {self.price!r})'

    @property
    def cost(self) -> float:
        return self.shares * self.price

    def sell(self, shares: int) -> None:
        self.shares -= shares
