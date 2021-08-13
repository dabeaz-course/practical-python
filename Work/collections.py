# Collections
# Suppose you wanted to tabulate the total number of shares of each stock. 
# This is easy using #Counter objects. Try it:

portfolio = read_portfolio('Data/portfolio.csv')

from collections import Counter

holdings = Counter()

for value in portfolio:
	holdings[value['name']] += value['shares']


portfolio = read_portfolio('Data/portfolio.csv')

from collections import defaultdict

holdings = defaultdict(list)

for value in portfolio:
	holdings[value['name']].append((value['shares'], value['price']))