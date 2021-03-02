# pcost.py
#
# Exercise 1.27

import sys
import csv
from report import read_portfolio


def portfolio_cost(filename):
    """Calculate total cost of stocks portfolio
    """
    total_purchase_cost = 0
    portfolio = read_portfolio(filename)

    return sum([row["shares"] * row["price"] for row in portfolio])


if len(sys.argv) == 2:
    f_path = sys.argv[1]
else:
    f_path = "Data/portfolio.csv"

cost = portfolio_cost(f_path)
print(f"Total purchase cost: {cost}")
