cost_to_buy_all = 0.0

with open('Data/portfolio.csv', 'rt') as f:
	category = next(f)
	for line in f:
		Line = line.split(',')
		number_of_shares = float(Line[1])
		stock_cost = float(Line[2])
		cost_to_buy_all += number_of_shares * stock_cost

print('Total amount spent $', cost_to_buy_all)
#	data = f.read()

#print(data)

#with open('Data/portfolio.csv', 'rt') as f:
#	for line in f:
#		print(line, end='')

#f = open('Data/portfolio.csv', 'rt')
#headers = next(f)
#print(headers)

#for line in f:
#	print(line, end='')


