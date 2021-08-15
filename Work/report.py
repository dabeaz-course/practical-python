#!/usr/bin/env python3
# report.py
#
# Exercise 2.4 - example with tuple unpacking and list of tuples

import csv
import fileparse
from collections import defaultdict

def read_portfolio(filename: str) -> list:
    '''Reads in portfolio and stores into a list of dictionaries.
       Args: (string) filename ex: 'Data/portfolio.csv' 
       Return: (dictonary) List of dictonaries.
    '''

    with open(filename, 'rt') as f:
        portfolio = fileparse.parse_csv(lines=f,types=[str, int, float],has_headers=True)

    return portfolio


def read_prices(filename: str) -> list:
    '''Read prices form a file and store as dictionary.'''

    prices = {}
    with open(filename, 'rt') as f:
        prices = dict(fileparse.parse_csv(lines=f, select=None, types=[str,float],has_headers=False,delimiter=','))

    return prices

def make_report(portfolio: list, prices: list) -> list:
    '''Adjust Portfolio to include change in price and current price.

       Args: portfolio list of dictionaries. Expecting name, shares, price as keys.
       Return: adj_portolio list of dictionaries, with additional key 'change'
    '''

    adj_portfolio = []
    for row in portfolio:
        try:
            adj_portfolio.append(({
                'name':row['name'],
                'price':row['price'],
                'shares':row['shares'],
                'cost': (row['price'] * row['shares']),
                'change':prices[row['name']]-row['price']            
                }))
        except TypeError as e:
            print(e)

    return adj_portfolio

def print_report(report:list,portfolio:list,prices:list) -> None:
    """
    Print results of the report.
    Calculates cost and actuals and displays at bottom for profit/loss.
    """

    cost = sum([row['shares'] * float(row['price']) for row in portfolio])
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

    return None

def portfolio_report(portfolio_fname: str, prices_fname: str) -> None:
    """
    Executes program to show portfolio_report.
    """
    portfolio = read_portfolio(portfolio_fname)
    prices = read_prices(prices_fname)
    
    report = make_report(portfolio, prices)
    print_report(report,portfolio,prices)

    return None


# Main function
def main(argv):
    # Parse command line args, environment, etc.
    if len(argv) != 3:
        raise SystemExit(f'Usage: {argv[0]} ' 'portfile pricefile')
    portfile = argv[1]
    pricefile = argv[2]

    portfolio_report(portfolio_fname=portfile, prices_fname=pricefile)


if __name__ == '__main__':
    import sys
    main(sys.argv)
