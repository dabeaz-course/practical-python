from .typedproperty import String, Integer, Float

class Stock:

    if __debug__:
        name = String('name')
        shares = Integer('shares')
        price = Float('price')

    '''
    An instance of a stock holding consisting of name, shares, and price.
    '''
    def __init__(self, name, shares, price):
        self.name   = name
        self.shares = shares
        self.price  = price

    @property
    def cost(self):
        '''
        Return the cost as shares*price
        '''
        return self.shares * self.price

    @cost.setter
    def cost(self, value):
        if not isinstance(value, float):
            raise TypeError('Expected an int')
        self._cost = value

    def sell(self, nshares):
        '''
        Sell a number of shares
        '''
        self.shares -= nshares

    @property
    def shares(self):
        return self._shares

    @shares.setter
    def shares(self, value):
        if not isinstance(value, int):
            raise TypeError('Expected an int')
        self._shares = value

    def __repr__(self):
        return f'Stock({self.name!r}, {self.shares!r}, {self.price!r})'
