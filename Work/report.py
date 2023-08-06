# report.py
#
# Exercise 2.4
import csv
from pprint import pprint

def read_portfolio(filename):
    portfolio = []
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        next(rows) # skip header
        for fields in rows:
            try:
                holding = (fields[0], int(fields[1]), float(fields[2]))
                portfolio.append(holding)
            except ValueError:
                print(f'Could not parse {fields}')
    return portfolio

def read_portfolio_2_5(filename):
    portfolio = []
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        next(rows) # skip header
        for fields in rows:
            try:
                holding = {
                    'name': fields[0],
                    'shares': int(fields[1]),
                    'price': float(fields[2])
                }
                portfolio.append(holding)
            except ValueError:
                print(f'Could not parse {fields}')
    return portfolio

def read_prices_2_6(filename):
    prices = {}
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        # next(rows) # skip header
        for row in rows:
            if (len(row) == 0):
                continue

            try:
                prices[row[0]] = float(row[1])
            except ValueError:
                print(f'Could not parse {row}')

    pprint(prices)
    return prices

def get_gainloss_2_7(stocksFilename, pricesFilename):
    prices = read_prices_2_6(pricesFilename)
    stocks = read_portfolio_2_5(stocksFilename)

    total_value = 0.0
    total_market_value = 0.0
    total_gain_loss = 0.0
    for stock in stocks:
        stock['current_value'] = stock['price'] * stock['shares']
        stock['market_value'] = prices[stock['name']] * stock['shares']
        stock['gain_loss'] = stock['market_value'] - stock['current_value']

        total_value += stock['current_value']
        total_market_value += stock['market_value']
        total_gain_loss += stock['gain_loss']

        print('{name:s} {gain_loss:,.2f}'.format_map(stock))

    print(f'Total value: {total_value:,.2f}')
    print(f'Total market value: {total_market_value:,.2f}')
    print(f'Total gain/loss: {total_gain_loss:,.2f}')

    return total_gain_loss