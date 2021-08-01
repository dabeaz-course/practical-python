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

def make_report(portfolio, prices):
    '''Adjust Portfolio to include change in price and current price.

       Args: portfolio list of dictionaries. Expecting name, shares, price as keys.
       Return: adj_portolio list of dictionaries, with additional key 'change'
    '''

    adj_portfolio = []
    for row in portfolio:
        row['change'] = prices[row['name']]-row['price']
        row['price'] = prices[row['name']]
        adj_portfolio.append(row)

    return adj_portfolio


prices = read_prices('Data/prices.csv')
portfolio = read_portfolio('Data/portfolio.csv')
report = make_report(portfolio, prices)


# Holdings total
total = []
for row in portfolio:
    total.append(row['shares'] * row['price'])

# Actuals
actuals = []
for row in portfolio:
    actuals.append(row['shares'] * prices[row['name']])




headers = ('Name', 'Shares', 'Price', 'Change')

print(f'{headers[0]:>10s} {headers[1]:>10s} {headers[2]:>10s} {headers[3]:>10s}')
print(f'{"":->10s} {"":->10s} {"":->10s} {"":->10s}')


for p in report:
    price = p['price']
    p['price'] = f'${price:.2f}'
    print('{name:>10s} {shares:>10d} {price:>10s} {change:>10.2f}'.format_map(p))



