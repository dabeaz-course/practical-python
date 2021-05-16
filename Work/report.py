 # report.py
#
# Exercise 2.4
import csv
def read_portfolio(filename):
	list = []
	with open(filename, 'rt') as f:
		rows = csv.reader(f)
		header = next(rows)
		for row in rows:
			holding = {
				'Name' : row[0],
				'Shares' : int(row[1]),
				'Price' : float(row[2])
			}
			list.append(holding)
	return list
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

def read_prices(filename):
	dict = { }
	with open(filename) as f:
		rows = csv.reader(f)
		for row in rows:
			try:
				dict[row[0]] = float(row[1])
			except IndexError:
				pass
	return dict

def make_report(list, dict):
	A = []
	for holding in list:
		new_price = dict[holding['Name']]
		change = new_price - holding['Price']
		Conclusion = (holding['Name'], holding['Shares'], new_price, change)
		A.append(Conclusion)
	return A

dict = read_prices('Data/prices.csv')
list = read_portfolio('Data/portfolio.csv')
report = make_report(list, dict)

Title = ('Name', 'Shares', 'Price', 'Change')
print(Title)
print('-------------------------------------')
for row in report:
	print('%7s %7d $%7.3f %7.3f' % row)
