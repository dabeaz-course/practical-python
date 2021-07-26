import csv
import sys


def portfolio_cost(filename):
    total_cost = 0.0
    with open(filename) as f:
        rows = csv.reader(f)
        next(rows)
        for row_number, row in enumerate(rows, start=1):
            name, shares, price = row
            try:
                shares = int(shares)
                price = float(price)
            except ValueError:
                print(f'Row {row_number}: Could\'t convert: {row!r}')
                continue
            total_cost += shares * price
    return total_cost


if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

cost = portfolio_cost(filename)
print(f'Total cost: {cost}')
