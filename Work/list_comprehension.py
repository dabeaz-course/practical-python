# List comprehension

from report_dict import read_portfolio, read_prices

portfolio = read_portfolio('Data/portfolio.csv')
prices = read_prices('Data/prices.csv')

more100 = [s for s in portfolio if s['shares'] > 100]
msftibm = [s for s in portfolio if s['name'] in ('MSFT','IBM')]
cost10k = [s for s in portfolio if s['shares']*s['price'] > 10000]
name_shares = [(s['name'],s['shares']) for s in portfolio]

# Set Comprehension. Using {} instead of [] creates a set
names = {s['name'] for s in portfolio} 

key_value = {s['name']: 0 for s in portfolio}

portfolio_prices = { name: prices[name] for name in names }


import csv
f = open('Data/portfoliodate.csv')
rows = csv.reader(f)
headers = next(rows)
select = ['name', 'shares', 'price']

indices = [ headers.index(colname) for colname in select ]
row = next(rows)

# This statement achieves much of what read_portfolio function does in a single line.
portfolio_list_comp = [ { colname: row[index] for colname, index in zip(select, indices) } for row in rows ]



def read_portfolio2(filename):
	"""
	Read in a portfolio using list comprehension.
	"""
	records = []
	with open(filename,'rt') as f:
		rows = csv.reader(f)
		headers = next(rows)
		select = ['name','shares','price']
		indices = [headers.index(colname) for colname in select]
		records = [ {colname:row[index] for colname, index in zip(select,indices)} for row in rows]

	return records