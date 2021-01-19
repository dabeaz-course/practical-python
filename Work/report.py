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
            record = dict(zip(headers, row))
            holding = {
                'name': record['name'],
                'shares': int(record['shares']),
                'price': float(record['price'])
            }
            portfolio.append(holding)

        return portfolio


def read_prices(filename):
    with open(filename, 'rt') as f:
        return {row[0]: row[1]
                for row in csv.reader(f)
                if row}


def get_stock_perf(stock, mkt_prices):
    name, shares, price = stock.values()
    change = float(price) - float(mkt_prices[name])
    return change * int(shares)


def make_report(portfolio, mkt_prices):
    report = []
    for stock in portfolio:
        name, shares, price = stock.values()
        current_price = float(mkt_prices[name])
        change = current_price - price
        report.append((name, shares, current_price, change))
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


# from collections import Counter

# holdings = Counter()

# for stock in portfolio:
#     holdings[stock['name']] += stock['shares']

# portfolio2 = read_portfolio('Work/Data/portfolio2.csv')
# holdings2 = Counter()

# for stock in portfolio2:
#     holdings2[stock['name']] += stock['shares']

# print(holdings, holdings2, holdings + holdings2)
