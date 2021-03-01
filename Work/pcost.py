# pcost.py
#
# Exercise 1.27

import os

f_path = "Data/portfolio.csv"
total_purchase_cost = 0

f = open(f_path, "rt")
headers = next(f)

for line in f:
    row = line.split(",")
    cost = int(row[1]) * float(row[2].strip())
    total_purchase_cost += cost

f.close()

print(f"Total purchase cost: {total_purchase_cost}")
