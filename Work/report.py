# report.py
#
# Exercise 2.4

import csv
import sys
from pprint import pprint


def read_portfolio(filename):
    portfolio = []
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            holding = {'name': row[0], 'shares': int(row[1]), 'price': float(row[2])}
            portfolio.append(holding)
        return portfolio


def read_prices(filename):
    prices = {}
    with open(filename) as f:
        rows = csv.reader(f)
        for row in rows:
            try:
                prices[row[0]] = float(row[1])
            except IndexError:
                pass
        return prices


# total_cost = 0.0
# for line in portfolio:
#     total_cost += line['shares'] * line['price']
#
# current_value = 0.0
# for line in portfolio:
#     n = line['name']
#     current_value += line['shares'] * prices[n]
#
#
# print('Original cost', total_cost)
# print('Current value', current_value)
# gain = current_value - total_cost
# print('Gain', gain)
# if gain > 0:
#     print('Hooray!')
# else:
#     print('Oh no')

def make_report(portfolio, prices):
    stonks = []
    for s in portfolio:
        name = s['name']
        shares = s['shares']
        price = prices[s['name']]
        change = price - s['price']
        line = (name, shares, price, change)
        stonks.append(line)
    return stonks

portfolio = read_portfolio('Data/portfolio.csv')
prices = read_prices('Data/prices.csv')

report = make_report(portfolio, prices)

for name, shares, price, change in report:
        print(f'{name:>10s} {shares:>10d} {price:>10.2f} {change:>10.2f}')