# report.py
#
# Exercise 2.4
import csv
import sys


def read_portfolio(filename):
    """
    Read a stock portfolio from a csv file into a list of dictionary entries
    including name, # of shares, and current price
    """
    portfolio = []
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            stock = {
                'name': row[0],
                'shares': int(row[1]),
                'price': float(row[2])
            }
            portfolio.append(stock)
    return portfolio


def read_prices(filename):
    """
    Read a csv file of price data into a dictionary mapping of names to prices
    """
    prices = {}
    with open(filename) as f:
        rows = csv.reader(f)
        for row in rows:
            try:
                prices[row[0]] = float(row[1])
            except IndexError:
                pass
    return prices


def make_report(portfolio, prices):
    returnVal = []
    for i in range(len(portfolio)):
        Record = []
        Record.append(portfolio[i]['name'])
        Record.append(portfolio[i]['shares'])
        Record.append(portfolio[i]['price'])
        Record.append(prices[portfolio[i]['name']] - portfolio[i]['price'])
        myTRecord = *Record,
        returnVal.append(myTRecord)
    return returnVal

# check if the files with price data are cli parameters
# set default test data if not passed to script


if len(sys.argv) == 3:
    porfolio_file = sys.argv[1]
    price_file = sys.argv[2]
else:
    porfolio_file = 'Data/portfolio.csv'
    price_file = 'Data/prices.csv'

portfolio = read_portfolio(porfolio_file)
prices = read_prices(price_file)

# print value of portfolio followed by value of price list
# totalCost = 0.0
# for s in portfolio:
#     totalCost += s['shares'] * s['price']
# print(f"Total cost of Portfolio: {totalCost:.2f}")
# totalValue = 0.0
# for s in portfolio:
#     totalValue += s['shares'] * prices[s['name']]
# print(f"Current Value of Portfolio: {totalValue:.2f}")
# print(f"Gain/Loss: {totalValue - totalCost:.2f}")
portfolio = read_portfolio('Data/portfolio.csv')
prices = read_prices('Data/prices.csv')
report = make_report(portfolio, prices)
# Format our report output with f-strings
for name, shares, price, change in report:
    print(f"{name:>10s} {shares:>10d} {price:10.2f} {change:>10.2f}")

