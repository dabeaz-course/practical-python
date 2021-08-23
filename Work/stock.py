#!/usr/bin/env python3
#stock.py

# Exercise 4.1: Objects as Data Structures

class Stock(object):

	def __init__(self, name, shares, price, change=None):
		self.name = name
		self.shares = shares
		self.price = price
		self.change = change
		self.total_cost = self.cost()

	def sell(self, num_shares):
		'''Function to sell shares'''
		self.shares -= num_shares

	def cost(self):
		'''Cost of existing shares'''
		return self.shares * self.price

class MyStock(Stock):

	def __init__(self, name, shares, price, factor):
		super().__init__(name,shares,price)
		self.factor = factor

	def panic(self):
		self.sell(self.shares)

	def cost(self):
		return self.factor *  super().cost()

