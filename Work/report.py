# report.py
#
# Exercise 2.4

import csv

from rich.pretty import install
from rich.console import Console
print = Console(width=100).print
install(Console(width=100))


def read_portfolio(filename):
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)
        portfolio = []

        for row in rows:
            holding = (row[0], int(row[1]), float(row[2]))
            portfolio.append(holding)

        return portfolio

portfolio = read_portfolio('Work/Data/portfolio.csv')
