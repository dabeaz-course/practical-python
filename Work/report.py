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
import fileparse

def read_portfolio(filename):
    '''
    Read a stock portfolio file into a list of dictionaries with keys
    name, shares, and price.
    '''
    with open(filename) as lines:
        return fileparse.parse_csv(lines, select = ['name', 'shares', 'price'], types = [str,int,float])

def read_prices(filename):
    '''
    Read a CSV file of price data into a dict mapping names to prices.
    '''
    prices = {}
    with open(filename) as lines:
        return dict(fileparse.parse_csv(lines, types = [str,float], has_headers = False))


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

def portfolio_report(portfoliofile, pricefile):

	portfolio = read_portfolio(portfoliofile)
	prices = read_prices(pricefile)

	report = make_report_data(portfolio, prices)

	print_report(report)

def main(args):
	if len(args) != 3:
		raise SystemExit('Usage: %s portfile pricefile' % args[0])
	portfolio_report(args[1], args[2])

if __name__ == '__main__':
	import sys
	main(sys.argv)
