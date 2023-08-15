# pcost.py
#
# Exercise 1.27
import csv

def pcost(filename):
    '''Returns the total cost of the portfolio'''
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        cost = 0.0
        for line_no, row in enumerate(rows, start=1):
            try:
                shares = int(row[1])
                stock_cost = float(row[2])
                cost += shares * stock_cost
            except ValueError:
                print(f'Could not parse line {line_no} with data: {row}')
    return cost