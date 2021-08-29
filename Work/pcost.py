# pcost.py
#
# Exercise 1.27%

#with open('Data/portfolio.csv', 'rt') as f:
#	for line in f:
#		print(line, end='')
import csv
#f = open('Data/portfolio.csv', 'rt')
#rows = csv.reader(f)
#headers = next(rows)
#print(headers)

#row = next(rows)
#print(row)

#record = dict(zip(headers, row))
#print(record)

def portfolio_cost(filename):
	total_cost = 0.0
	with open(filename) as f:
		rows = csv.reader(f)
		headers = next(rows)
		for rowno, row in enumerate(rows, start=1):
			record = dict(zip(headers, row))
			try:
				nshares = int(record['shares'])
				price = float(record['price'])
				total_cost += nshares * price
			except ValueError:
				print(f'Row {rowno}: Bad row: {row}')
	return total_cost

print(portfolio_cost('Data/portfoliodate.csv'))

#f = str(f)
#print(f)
#List = []
#for line in f:
#	stripped_line = line.strip
#	line_list = stripped_line.split()
#	List.append(line_list)
#print(List)

#line = str(line)
#line.remove('AA')
 #line.remove('IBM')
#line.remove('CAT')
#line.remove('MSFT')
#line.remove('GE')
#line.remove('MSFT')
#line.remove('IBM')

def portfolio_report(pricefile):

	cost = portfolio_cost(pricefile)

	report = make_report_data(cost)

	print_report(report)

def main(argv):
	if len(argv) != 2:
		raise SystemExit('Usage: %s pricefile' % argv[0])
	portfolio_report(argv[1], argv[2])

if __name__ == '__main__':
	import sys
	main(sys.argv)
