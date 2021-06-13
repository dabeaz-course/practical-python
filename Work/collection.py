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



portfolio = read_portfolio('Data/portfolio.csv')
from collections import Counter
holding = Counter()
for s in portfolio:
	holding[s['Name']] += s['Shares']

print(holding)


portfolio2 = read_portfolio('Data/portfolio2.csv')
holding = Counter()
for s in portfolio2:
	holding[s['Name']] += s['Shares']
print(holding)

#nums = [1, 2, 3, 4]
#squares = [x * x for x in nums]
#print(squares)
#double = [2 * x for x in nums if x > 2]
#print(double)

cost = sum([ s['Shares'] * s['Price'] for s in portfolio ])
print(cost)

more100 = [s for s in portfolio if s['Shares'] > 100]
print(more100)
msftibm = [s for s in portfolio if s['Name'] in {'MSFT', 'IBM'}]
print(msftibm)

cost10k = [s for s in portfolio if s['Shares'] * s['Price'] > 10000]
print(cost10k)

name_and_shares = [(s['Name'], s['Shares']) for s in portfolio]
print(name_and_shares)

