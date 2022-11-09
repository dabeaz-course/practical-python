# report.py
#
# Exercise 2.4

import csv
import sys

def readPortfolio(filename):
    portfolio = []
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        next(rows)
        for row in rows:
            name = row[0]
            shares = int(row[1])
            price = float(row[2])
            # holding = (name, shares, price) # tuple
            holding = {}
            holding['name'] = name
            holding['shares'] = shares
            holding['price'] = price
            portfolio.append(holding)

    return portfolio

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

stocks = readPortfolio(filename)
print(stocks)