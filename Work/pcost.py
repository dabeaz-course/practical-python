# pcost.py
#
# Exercise 1.27

total_cost = 0

with open('Data/portfolio.csv', 'rt') as f:
    next(f)
    for line in f:
        row = line.split(',')
        share = int(row[1])
        cost = float(row[2])
        total_cost += share*cost

print('Total cost ', total_cost)