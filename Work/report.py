 # report.py
#
# Exercise 2.4
import csv
def read_portfolio(filename):
	list = []
	with open(filename, 'rt') as f:
		rows = csv.reader(f)
		header = next(rows)
		for row in rows:
			holding = (row[0], int(row[1]), float(row[2]))
			list.append(holding)
	return list
portfolio = read_portfolio('Data/portfolio.csv')
total = 0.0
for s in portfolio:
	total+= s[1] * s[2]
print(portfolio)
from pprint import pprint
pprint(portfolio)

prices = { }
prices['IBM'] = 92.45
prices['MSFT'] = 45.12
print(prices)
print(prices['MSFT'])

def read_prices(filename):
	dict = { }
	f = open(filename, 'rt')
	rows = csv.reader(f)
	for row in rows:
		try:
			print(row)
		except ValueError:
			print('Not a valid list', row)
prices = read_prices('Data/prices.csv')
