# pcost.py
#
# Exercise 1.27
total_cost = 0.0

with open('Data/portfolio.csv', 'rt') as f:
    headers = next(f)
    for line in f:
        row = line.split(',')
        print(row)
        shares = int(row[1])
        price = float(row[2])
        total_cost += shares * price

print('Total cost is', round(total_cost, ndigits=2))