# pcost.py
#
# Exercise 1.27

def pcost(filename):
    '''Returns the total cost of the portfolio'''
    with open(filename, 'rt') as f:
        next(f) # skip header
        cost = 0.0
        for line in f:
            try:
                fields = line.split(',')
                shares = int(fields[1])
                stock_cost = float(fields[2])
                cost += shares * stock_cost
            except ValueError:
                print(f'Could not parse {line}')
    return cost

print(f'Total cost ${pcost("Data/portfolio.csv"):,.2f}')