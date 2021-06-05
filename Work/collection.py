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
