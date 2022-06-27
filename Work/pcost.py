# pcost.py
#
# Exercise 1.27

cost = 0

with open('Data/portfolio.csv', 'rt') as f:
    next(f)
    for line in f:
        row = line.split(',')
        cost += row[1]*row[2]

print('Total cost ', cost)