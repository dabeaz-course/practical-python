
import csv

from collections import Counter


def read_portfolio(filename):
	"""
	Read csv file and convert to a dictionary.
	"""

	portfolio = []

	with open(filename, 'rt') as f:
		
		data = csv.reader(f)
		header = next(data)

		for rowno, row in enumerate(data):
			try:
				record = dict(zip(header,row))
				record['shares'] = int(record['shares'])
				record['price'] = float(record['price'])
				portfolio.append(record)
			except ValueError:
				print(f'Row:{rowno} had an issue, here is the record: {row}')

		return portfolio


def count_shares(portfolio):

	holdings = Counter()

	for record in portfolio:
		holdings[record['name']] += record['shares']

	return holdings

def print_report(holdings):

	headers = ['Name','Shares']
	print(f'{headers[0]:>10s}{headers[1]:>10s}')

	for row in holdings:
		shares = holdings[row]
		print(f"{row:>10s}{shares:>10d}")




portfolio = read_portfolio('Data/portfolio.csv')
counts = count_shares(portfolio)
print_report(counts)
