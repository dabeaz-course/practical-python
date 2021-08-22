# report.py
#
# Exercise 2.4
#import csv
#def read_portfolio(filename):
#	list = []
#	with open(filename, 'rt') as f:
#		rows = csv.reader(f)
#		header = next(rows)
#		for row in rows:
#			holding = {
#				'Name' : row[0],
#				'Shares' : int(row[1]),
#				'Price' : float(row[2])
#			}
#			list.append(holding)
#	return list
#portfolio = read_portfolio('Data/portfolio.csv')
#total = 0.0
#for s in portfolio:
#	total+= s[1] * s[2]
#print(portfolio)
#from pprint import pprint
#pprint(portfolio)

#prices = { }
#prices['IBM'] = 92.45
#prices['MSFT'] = 45.12
#print(prices)
#print(prices['MSFT'])

#def read_prices(filename):
#	dict = { }
#	with open(filename) as f:
#		rows = csv.reader(f)
#		for row in rows:
#			try:
#				dict[row[0]] = float(row[1])
#			except IndexError:
#				pass
#	return dict

#def make_report(list, dict):
#	A = []
#	for holding in list:
#		new_price = dict[holding['Name']]
#		change = new_price - holding['Price']
#		Conclusion = (holding['Name'], holding['Shares'], new_price, change)
#		A.append(Conclusion)
#	return A

#dict = read_prices('Data/prices.csv')
#list = read_portfolio('Data/portfolio.csv')
#report = make_report(list, dict)

#Title = ('Name', 'Shares', 'Price', 'Change')
#print(Title)
#print('-------------------------------------')
#for row in report:
#	print('%7s %7d $%7.3f %7.3f' % row)


import csv

def read_portfolio(filename):
    '''
    Read a stock portfolio file into a list of dictionaries with keys
    name, shares, and price.
    '''
    portfolio = []
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)

        for row in rows:
            record = row
            stock = {
                 'name'   : row[0],
                 'shares' : int(row[1]),
                 'price'   : float(row[2])
            }
            portfolio.append(stock)

    return portfolio

def read_prices(filename):
    '''
    Read a CSV file of price data into a dict mapping names to prices.
    '''
    prices = {}
    with open(filename) as f:
        rows = csv.reader(f)
        for row in rows:
            try:
                prices[row[0]] = float(row[1])
            except IndexError:
                pass

    return prices

def make_report_data(portfolio, prices):
    '''
    Make a list of (name, shares, price, change) tuples given a portfolio list
    and prices dictionary.
    '''
    rows = []
    for stock in portfolio:
        current_price = prices[stock['name']]
        change        = current_price - stock['price']
        summary       = (stock['name'], stock['shares'], current_price, change)
        rows.append(summary)
    return rows

# Read data files and create the report data

portfolio = read_portfolio('Data/portfolio.csv')
prices    = read_prices('Data/prices.csv')

# Generate the report data

report    = make_report_data(portfolio, prices)

# Output the report
headers = ('Name', 'Shares', 'Price', 'Change')
print('%10s %10s %10s %10s' % headers)
print(('-' * 10 + ' ') * len(headers))
for row in report:
    print('%10s %10d %10.2f %10.2f' % row)
