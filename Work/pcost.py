# pcost.py
#
# Exercise 1.27
import csv

def pcost(filename):
    '''Returns the total cost of the portfolio'''
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        next(rows) # skip header
        cost = 0.0
        for fields in rows:
            try:
                shares = int(fields[1])
                stock_cost = float(fields[2])
                cost += shares * stock_cost
            except ValueError:
                print(f'Could not parse {fields}')
    return cost