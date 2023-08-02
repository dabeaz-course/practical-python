# pcost.py
#
# Exercise 1.27

def pcost():
    with open('Data/portfolio.csv', 'rt') as f:
        next(f) # skip header
        cost = 0.0
        for line in f:
            row = line.split(',')
            shares = int(row[1])
            stock_cost = float(row[2])
            cost += shares * stock_cost
    return cost

print(f'Total cost ${pcost():,.2f}')