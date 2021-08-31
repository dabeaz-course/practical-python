#!/usr/bin/env python3
#pcost.py

# Exercise 1.27
# Modified to use csv imported library.
# Handles csv files natively, gets rid of double quotes
# No need to split by delimitter.

# run with python3 -i pcost_csv.py
# inputs: portfolio_cost('Data/portfolio.csv') 
#         portfolio_cost('Data/missing.csv')    <-- uses try, except catch.

import csv
import report
from portfolio import Portfolio

def portfolio_cost(filename):
    'Using csv library to parse csv.'
    portfolio = report.read_portfolio(filename)
    
    return portfolio.total_cost


def main(argv):
    # Main function

    if len(argv) != 2:
        raise SystemExit(f'Usage: {argv[0]} ','filename')

    filename = argv[1]
    cost = portfolio_cost(filename=filename)
    print('Total Cost:', cost)


if __name__ == '__main__':
    import sys
    main(sys.argv)