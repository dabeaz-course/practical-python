# report_dict.py
#
# Exercise 2.4 - example with tuple unpacking and list of tuples

import csv
import sys
from collections import defaultdict

def read_portfolio(filename):
    '''Reads in portfolio and stores into a list of dictionaries.
       Args: (string) filename ex: 'Data/portfolio.csv' 
       Return: (dictonary) List of dictonaries.
    '''
    portfolio = []
    try:
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
    except FileNotFoundError as err:
        print(f'File does not exist: {err}')

    return portfolio


def read_prices(filename):
    '''Read prices form a file and store as dictionary.'''

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
        adj_portfolio.append(({
            'name':row['name'],
            'price':row['price'],
            'shares':row['shares'],
            'cost': row['price']*row['shares'],
            'change':prices[row['name']]-row['price']            
            }))

    return adj_portfolio



if len(sys.argv) > 2:
    try:
        portfolio_fname = sys.argv[1]
        prices_fname = sys.argv[2]    

        portfolio = read_portfolio(portfolio_fname)
        prices = read_prices(prices_fname)
        report = make_report(portfolio, prices)
    except IndexError:
        print(f'Not enough parameters')
else:
    prices = read_prices('Data/prices.csv')
    portfolio = read_portfolio('Data/portfolio.csv')
    report = make_report(portfolio, prices)





# Holdings total
total_list = []
for row in portfolio:
    total_list.append(row['shares'] * row['price'])


cost = sum([row['shares'] * float(row['price']) for row in portfolio])

# Actuals

actuals_list = []
for row in portfolio:
    actuals_list.append(row['shares'] * prices[row['name']])

actuals = sum([prices[row['name']]* row['shares'] for row in portfolio])


headers = ('Name', 'Shares', 'Price', 'Cost', 'Change')
print(f'{headers[0]:>10s} {headers[1]:>10s} {headers[2]:>10s} {headers[3]:>10s} {headers[4]:>10s}')
print(f'{"":->10s} {"":->10s} {"":->10s} {"":->10s} {"":->10s}')

for p in report:
    price = p['price']
    p['price'] = f'${price:.2f}'
    print('{name:>10s} {shares:>10d} {price:>10s} {cost:>10.2f} {change:>10.2f}'.format_map(p))

print(f'\n')
print(f'{"":>10s} {"":>10s} {"Total.Cost":>10s} {cost:>10.2f}')
print(f'{"":>10s} {"":>10s} {"Curr.Val":>10s} {cost-actuals:>10.2f}')

