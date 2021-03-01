# pcost.py
#
# Exercise 1.27

import sys
import csv


def portfolio_cost(filename):
    total_purchase_cost = 0

    with open(f_path, "rt") as f:
        rows = csv.reader(f)
        headers = next(rows)

        for i, row in enumerate(rows, start=1):
            record = dict(zip(headers, row))
            try:
                nshares = int(record["shares"])
                price = float(record["price"])
                total_purchase_cost += nshares * price
            except ValueError:
                print(f"Row {rowno}: Bad row: {row}")

    return total_purchase_cost


if len(sys.argv) == 2:
    f_path = sys.argv[1]
else:
    f_path = "Data/portfolio.csv"

cost = portfolio_cost(f_path)
print(f"Total purchase cost: {cost}")
