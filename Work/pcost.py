# pcost.py
#
# Exercise 1.27
with open('Data/portfolio.csv', 'rt') as f:
    name, shares, price = next(f).split(',')
    Total_cost = 0.00
    for lines in f:
        name, shares, price = lines.split(',')
        Total_cost += int(shares) * float(price)
    print('Total cost', Total_cost)