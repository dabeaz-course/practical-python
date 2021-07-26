# 2.2 Containers

portfolio = [('GOOG', 100, 490.1),('IBM', 50, 91.3), ('CAT', 150, 83.44)]

portfolio[0]
portfolio[2]



records = []  # Initial empty list

with open('Data/portfolio.csv', 'rt') as f:
    next(f) # Skip header
    for line in f:
        row = line.split(',')
        records.append((row[0], int(row[1]), float(row[2])))
			


# Dictionary as container

prices = {
   'GOOG': 513.25,
   'CAT': 87.22,
   'IBM': 93.37,
   'MSFT': 44.12
}

prices = {}

prices['GOOG'] = 513.25
prices['CAT'] = 87.22
prices['IBM'] = 93.37


# Populating dictionary from a file

prices = {}

with open('Data/prices.csv', 'rt') as f:
	for line in f:
		row = line.split(',')
		if len(row) == 2:
			prices[str(row[0])] = float(row[1])


import csv

prices = {}

with open('Data/prices.csv', 'rt') as f:
	data = csv.reader(f)
	for line in data:
		if len(line) == 2:
			prices[str(row[0])] = float(row[1])
		

