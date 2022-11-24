# report.py
#
# Exercise 2.4
import csv

def read_portfolio_tuples(filename):
    portfolio = []
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            temp = (row[0], int(row[1]), float(row[2]))
            portfolio.append(temp)
    return portfolio

def read_portfolio_dict(filename):
    portfolio = []
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            temp = {'name' : row[0], 'shares': int(row[1]), 'price': float(row[2])}
            portfolio.append(temp)
    return portfolio
    
portfolio = read_portfolio_dict('Data/portfolio.csv')
print(portfolio)
portfolio = read_portfolio_tuples('Data/portfolio.csv')
print(portfolio)