# pcost.py
#
# Exercise 1.27

import sys

def portfolio_cost(filename):
    total_cost = 0

    with open(filename, 'rt') as f:

        next(f)
        for line in f:
            row = line.split(',')
            try:
                share = int(row[1])
                cost = float(row[2])
                total_cost += share*cost
            except ValueError:
                print("Couldn't parse", line)

    return total_cost
    

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

cost = portfolio_cost(filename)
print('Total cost : ', cost)