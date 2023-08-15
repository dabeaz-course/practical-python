# pcost.py
#
# Exercise 1.27
import csv

def pcost(filename):
    '''Returns the total cost of the portfolio'''
    with open(filename, 'rt') as f:
        lines = csv.reader(f)
        cost = 0.0
        header_line = next(lines)
        print(header_line)
        for line_no, line in enumerate(lines):
            record = dict(zip(header_line, line))
            try:
                shares = int(record['shares'])
                price = float(record['price'])
                cost += shares * price
            except ValueError:
                print(f'Could not parse line {line_no} with data: {line}')
    return cost