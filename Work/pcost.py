# pcost.py
#
# Exercise 1.27

def portfolio_cost(filename):
    total_cost = 0

    with open(filename, 'rt') as f:

        next(f)
        for line in f:
            row = line.split(',')
            share = int(row[1])
            cost = float(row[2])
            total_cost += share*cost

    return total_cost


cost = portfolio_cost('Data/portfolio.csv')
print('Total cost : ', cost)