# report.py
#
# Exercise 2.4 - example with tuple unpacking and list of tuples

import csv

def read_portfolio(filename):
    '''Computes the total cost (shares*price) of a portfolio file'''
    portfolio = []

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for name,shares,price in rows:
            record = {}
            record['name'] = name
            record['shares'] = int(shares)
            record['price'] = float(price)
            portfolio.append(record)

    return portfolio


def read_prices(filename):
    '''Read prices form a file and store as dictionary.'''

    import csv

    prices = {}

    with open(filename,'rt') as f:
        rows = csv.reader(f)
        try:
            for key,value in rows:
                prices[key] = float(value)
        except ValueError:
            pass

    return prices


prices = read_prices('Data/prices.csv')
portfolio = read_portfolio('Data/portfolio.csv')


# Holdings total
total = 0.0

for row in portfolio:
    total += row['shares'] * row['price']

# Actuals

actuals = 0.0
for row in portfolio:
    actuals += row['shares'] * prices[row['name']]

print('Report Summary:')
print('Holdings:',total)
print('Actuals:',actuals)

print(f'Gain/Loss:{total-actuals:.2f}')



