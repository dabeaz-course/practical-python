class Stock:

    def __init__(self, name, shares, price):

        self.name = name
        self.shares = shares
        self.price = price

    def __repr__(self):
        return f"Stock({self.name}, {self.shares}, {self.price})"

    def cost(self):
        return self.shares * self.price

    def sell(self, amount):
        self.shares -= amount


class NewStock(Stock):

    def yow(self):
        print('Yow!')
