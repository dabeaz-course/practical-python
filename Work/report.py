# report.py
#
# Exercise 2.4

import csv

from rich.pretty import install
from rich.console import Console
print = Console(width=100).print
install(Console(width=100))


def read_portfolio(filename):
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        portfolio = []

        for row in rows:
            holding = {
                'name': row[0],
                'shares': int(row[1]),
                'price': float(row[2])
            }
            portfolio.append(holding)

        return portfolio

portfolio = read_portfolio('Work/Data/portfolio.csv')

def read_prices(filename):
    with open(filename, 'rt') as f:
        return {row[0]: row[1]
                for row in csv.reader(f)
                if row}

stock_prices = read_prices('Work/Data/prices.csv')


def get_stock_perf(stock):
    bought_price = float(stock['price'])
    mkt_price = float(stock_prices[stock['name']])
    shares = int(stock['shares'])
    return (bought_price - mkt_price) * shares


gain_loss = sum(get_stock_perf(stock) for stock in portfolio)
print(f'${gain_loss:,.2f}')
