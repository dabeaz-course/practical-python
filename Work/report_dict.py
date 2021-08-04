# report_dict.py
#
# Exercise 2.4 - example with tuple unpacking and list of tuples

import csv

def read_portfolio(filename):
    '''Reads in portfolio and stores into a list of dictionaries.'''
    portfolio = []

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for rowno,line in enumerate(rows):
            try:
                record = dict(zip(headers,line))
                record['shares'] = int(record['shares'])
                record['price'] = float(record['price'])
                portfolio.append(record)
            except ValueError:
                print(f"Row:{rowno:>2d} Couldn't convert: {line}")

    return portfolio


def read_prices(filename):
    '''Read prices form a file and store as dictionary.'''

    import csv

    prices = {}

    with open(filename,'rt') as f:
        rows = csv.reader(f)

        try:
            for rowno,row in enumerate(rows):
                prices[row[0]] = float(row[1])
        except IndexError:
            print(f"Row:{rowno:>2d} Couldn't convert: {row}")

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



