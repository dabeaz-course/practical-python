import csv

def portfolio_cost(filename):
	cost_to_buy_all = 0.0

	with open('Data/portfolio.csv', 'rt') as f:
		category = next(f)
		for line in f:
			Line = line.split(',')
			number_of_shares = float(Line[1])
			stock_cost = float(Line[2])
			cost_to_buy_all += number_of_shares * stock_cost
			print('Total amount spent $', cost_to_buy_all)
	return cost_to_buy_all

filename = 'Data/portfolio.csv'

cost = portfolio_cost(filename)
print('Total cost: $', cost)
