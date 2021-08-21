#!/usr/bin/env python3
#stock.py

# Exercise 4.1: Objects as Data Structures

class Stock():

	def __init__(self, name, shares, price, change=None):

		self.name = name
		self.shares = shares
		self.price = price
		self.change = change
		self.cost = self.cost()

	def sell(self, num_shares):
		'''Function to sell shares'''
		self.shares -= num_shares

	def cost(self):
		'''Cost of existing shares'''
		return self.shares * self.price
