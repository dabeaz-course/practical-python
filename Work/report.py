# report.py
#
# Exercise 2.4

import csv


def read_portfolio(filename):

    portfolio = []
    with open(filename, "rt") as f:
        rows = csv.reader(f)
        headers = next(rows)

        for row in rows:
            # split_row = row.split(",")
            holding = {
                "name": row[0],
                "shares": int(row[1]),
                "price": float(row[2]),
            }
            portfolio.append(holding)

    return portfolio


def read_prices(filename):

    prices = dict()
    with open(filename, "rt") as f:
        rows = csv.reader(f)

        for row in rows:
            if row == []:
                continue
            else:
                prices[row[0]] = float(row[1])

    return prices


portfolio = read_portfolio("Data/portfolio.csv")
prices = read_prices("Data/prices.csv")

total_cost = 0
total_actual_value = 0
for stock in portfolio:
    total_cost += stock["shares"] * stock["price"]
    total_actual_value += stock["shares"] * prices[stock["name"]]

print(total_cost, total_actual_value)
