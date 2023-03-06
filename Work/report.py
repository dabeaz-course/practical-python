# report.py
#
# Exercise 2.4

import csv

def readPortfolio(filename):
    '''
    Read a stock portfolio file into a list of dictionaries
    with keys name, shares, price 
    '''
    portfolio = []
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)

        '''dictionary comprehension'''
        '''
        select = ['name', 'shares', 'price']
        indeces = [headers.index(colname) for colname in select]
        portfolio = [{colname:row[index] for colname, index in zip(select, indeces)} for row in rows]
        '''
        
        for row in rows:
            record = dict(zip(headers, row))
            # print(record)
            stock = {
                'name' : record['name'],
                'shares' : int(record['shares']),
                'price' : float(record['price'])
            }
            portfolio.append(stock)
        
    return portfolio

def readPrices(filename):
    '''
    make a dictionary of prices given prices csv file
    '''
    price = {}
    with open(filename, 'r') as f:
        rows = csv.reader(f)
        for row in rows:
            try:
                price[row[0]] = float(row[1])
            except IndexError:
                # print('Index out of range')
                # continue
                pass
    return price

# Compute gain/loss

# check for portfolio stock in stock prices
# compute shares * price when bought vs shares * stock prices
def makeReportData(portfolio, prices):
    '''
    make a list of (name, shares, price, change) given portfolio list 
    and prices dictionary
    '''

    report = []

    for stock in portfolio:
        stockPrice = stock['price']
        
        marketPrice = prices[stock['name']]
        change = marketPrice - stockPrice
        summary = (stock['name'], stock['shares'], marketPrice, change)
        report.append(summary)

    return report

def printReports(report):
    '''
    Prints a formatted table with the list of tuples (Name, Shares, Price, Change)
    '''
    headers = ('Name', 'Shares', 'Price', 'Change')
    print('%10%10%10%10' % headers)
    print(('-' * 10 + ' ') * len(headers))

    for row in report:
        print('%10 %10d %10.2f %10.2f' % row)

def portfolioReport(portfolioFile, priceFile):
    '''
    Given portfolio and price files, make a report
    '''

    portfolio = readPortfolio(portfolioFile)
    prices = readPrices(priceFile)

    # generate report data
    report = makeReportData(portfolio, prices)

    printReports(report)

portfolioReport('/../Work/Data/portfolio.csv', '/../Work/Data/prices')