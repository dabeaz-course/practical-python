# report.py
#
# Exercise 2.4

import csv

from rich.console import Console
from rich.pretty import install

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


def read_prices(filename):
    with open(filename, 'rt') as f:
        return {row[0]: row[1]
                for row in csv.reader(f)
                if row}


def get_stock_perf(stock, mkt_prices):
    bought_price = float(stock['price'])
    current_price = float(mkt_prices[stock['name']])
    shares = int(stock['shares'])
    return (bought_price - current_price) * shares


def make_report(portfolio, mkt_prices):
    report = []
    for stock in portfolio:
        current_price = float(mkt_prices[stock['name']])
        change = current_price - stock['price']
        report.append((stock['name'], stock['shares'], current_price, change))
    return report


portfolio = read_portfolio('Work/Data/portfolio.csv')
mkt_prices = read_prices('Work/Data/prices.csv')
gain_loss = sum(get_stock_perf(stock, mkt_prices) for stock in portfolio)
report = make_report(portfolio, mkt_prices)

fields = ('Name', 'Shares', 'Price', 'Change')
header = ' '.join(f'{field:>10}' for field in fields)
divider = ' '.join('-' * 10 for _ in range(len(fields)))

print(header, divider, sep='\n')
for name, shares, price, change in report:
    print(f"{name:>10s} {shares:10d} {f'${price:.2f}':>10} {change:10.2f}")
