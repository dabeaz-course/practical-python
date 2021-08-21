#!/usr/bin/env python3
# report.py
#
# Exercise 2.4 - example with tuple unpacking and list of tuples

import csv
import fileparse
import stock

def read_portfolio(filename: str) -> list:
    '''Reads in portfolio and stores into a list of dictionaries.
       Args: (string) filename ex: 'Data/portfolio.csv' 
       Return: (dictonary) List of dictonaries.
    '''

    with open(filename, 'rt') as f:
        portfolio = fileparse.parse_csv(lines=f,types=[str, int, float],has_headers=True)

    stock_portfolio = [stock.Stock(s['name'],s['shares'],s['price']) for s in portfolio]

    return stock_portfolio


def read_prices(filename: str) -> list:
    '''Read prices form a file and store as dictionary.'''

    prices = {}
    with open(filename, 'rt') as f:
        prices = dict(fileparse.parse_csv(lines=f, types=[str,float],has_headers=False))

    return prices

def make_report(portfolio: object, prices: list) -> list:
    '''Adjust Portfolio to include change in price and current price.

       Args: portfolio list of objects. Expecting Stock() with name, shares, price as attributes.
       Return: adj_portolio list of dictionaries, with additional key 'change'
    '''

    adj_portfolio = []
    for stock in portfolio:
        try:
            stock.change = prices[stock.name] - stock.price
            adj_portfolio.append(stock)
        except TypeError as e:
            print(e)

    return adj_portfolio

def print_report(report:object,portfolio:object,prices:list) -> None:
    """
    Print results of the report.
    Calculates cost and actuals and displays at bottom for profit/loss.
    """

    cost = sum([stock.shares * float(stock.price) for stock in portfolio])
    actuals = sum([prices[stock.name]* stock.shares for stock in portfolio])

    headers = ('Name', 'Shares', 'Price', 'Cost', 'Change')
    print(f'{headers[0]:>10s} {headers[1]:>10s} {headers[2]:>10s} {headers[3]:>10s} {headers[4]:>10s}')
    print(f'{"":->10s} {"":->10s} {"":->10s} {"":->10s} {"":->10s}')

    for p in report:
        price = p.price
        p.price = f'${price:.2f}'
        print(f'{p.name:>10s} {p.shares:>10d} {p.price:>10s} {p.cost:>10.2f} {p.change:>10.2f}')

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
