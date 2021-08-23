#!/usr/bin/env python3
# report.py
#
# Exercise 2.4 - example with tuple unpacking and list of tuples

import csv
import fileparse
import stock
import tableformat

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
        except TypeError as err:
            print(err)

    return adj_portfolio

def print_report(report:object, formatter:object) -> None:
    """
    Print results of the report.
    Calculates cost and actuals and displays at bottom for profit/loss.
    """

    cost = sum([stock.cost() for stock in report])
    
    formatter.headings(['Name', 'Shares', 'Price', 'Change'])

    for stock in report:
        rowdata = [ stock.name, str(stock.shares), f'{stock.price:0.2f}', f'{stock.change:0.2f}' ]
        formatter.row(rowdata)

    print(f'\n')
    print(f'{"":>10s} {"":>10s} {"Total.Cost":>10s} {cost:>10.2f}')


    return None

def portfolio_report(portfolio_fname: str, prices_fname: str, fmt='txt') -> None:
    """
    Executes program to show portfolio_report.
    """

    # Read data files
    portfolio = read_portfolio(portfolio_fname)
    prices = read_prices(prices_fname)

    # Create report data    
    report = make_report(portfolio, prices)

    # Print it out
    formatter = tableformat.create_formatter(fmt)
    print_report(report,formatter)

    return None


# Main function
def main(argv):
    # Parse command line args, environment, etc.
    if len(argv) != 4:
        raise SystemExit(f'Usage: {argv[0]} ' 'portfile pricefile [txt|csv|html]')
    
    portfile = argv[1]
    pricefile = argv[2]
    print_fmt = argv[3]

    portfolio_report(portfolio_fname=portfile, prices_fname=pricefile, fmt=print_fmt)


if __name__ == '__main__':
    import sys
    main(sys.argv)
