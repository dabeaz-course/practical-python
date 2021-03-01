# pcost.py
#
# Exercise 1.27

import sys


def portfolio_cost(filename):
    total_purchase_cost = 0

    f = open(f_path, "rt")
    headers = next(f)

    for line in f:
        row = line.split(",")
        cost = int(row[1]) * float(row[2].strip())
        total_purchase_cost += cost

    f.close()

    return total_purchase_cost


if len(sys.argv) == 2:
    f_path = sys.argv[1]
else:
    f_path = "Data/portfolio.csv"

cost = portfolio_cost(f_path)
print(f"Total purchase cost: {cost}")
