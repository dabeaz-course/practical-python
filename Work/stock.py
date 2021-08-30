#!/usr/bin/env python3
#stock.py

# Exercise 4.1: Objects as Data Structures

class Stock(object):

	'''
	When using __slots__, python will make an optimization on a data structure.
	It also restricts the class from manipulation (adding attributes)
	'''
	__slots__ = ('name','_shares','price','change','total_cost')

	def __init__(self, name, shares, price, change=None):
		self.name = name
		self._shares = shares
		self.price = price
		self.change = change
		self.total_cost = self.cost

	def sell(self, num_shares):
		'''Function to sell shares'''
		self.shares -= num_shares

	@property
	def cost(self):
		'''Cost of existing shares'''
		return self._shares * self.price

	@property
	def shares(self):
		'''Return shares'''
		return self._shares

	@shares.setter
	def shares(self, value):
		if not isinstance(value, int):
			raise TypeError('Expected int')
		self._shares = value

	def __repr__(self):
		return f'Stock({self.name},{self.shares},{self.price})'

class MyStock(Stock):

	def __init__(self, name, shares, price, factor):
		super().__init__(name,shares,price)
		self.factor = factor

	def panic(self):
		self.sell(self.shares)

	def cost(self):
		return self.factor *  super().cost

