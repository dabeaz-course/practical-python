# pcost_csv.py

# Exercise 1.27
# Modified to use csv imported library.
# Handles csv files natively, gets rid of double quotes
# No need to split by delimitter.

# run with python3 -i pcost_csv.py
# inputs: portfolio_cost('Data/portfolio.csv') 
#		  portfolio_cost('Data/missing.csv')    <-- uses try, except catch.

import csv
import sys

def portfolio_cost(filename):
	'Using csv library to parse csv.'
	with open(filename,'rt') as file:

		rows = csv.reader(file)
		header = next(rows)
		total_cost = 0

		for rowno,line in enumerate(rows,start=1):
			record = dict(zip(header,line))
			try:
				nshares = int(record['shares'])
				price = float(record['price'])
				total_cost += nshares * price
			except ValueError:
				print(f"Row:{rowno:>2d} Couldn't convert: {line}")

		return total_cost



if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

cost = portfolio_cost(filename)
print('Total cost:', cost)