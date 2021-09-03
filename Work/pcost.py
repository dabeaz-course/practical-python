import report

def portfolio_cost(filename):

	portfolio = report.read_portfolio(filename)

	return sum([s['shares'] * s['price'] for s in portfolio])

def main(argv):
	if len(argv) != 2:
		raise SystemExit('Usage: %s pricefile' % argv[0])
	filename = argv[1]
	print('Total cost:', portfolio_cost(filename))

if __name__ == '__main__':
	import sys
	main(sys.argv)
