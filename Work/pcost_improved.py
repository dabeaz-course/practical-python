# pcost_csv.py

# Exercise 1.27
# Modified to use csv imported library.
# Handles csv files natively, gets rid of double quotes
# No need to split by delimitter.

# run with python3 -i pcost_csv.py
# inputs: portfolio_cost('Data/portfolio.csv') 
#		  portfolio_cost('Data/missing.csv')    <-- uses try, except catch.

import csv
import sys
import report

def portfolio_cost(filename):
	'Using csv library to parse csv.'
	portfolio = report.read_portfolio(filename)

	total_cost = 0
	for row in portfolio:
		total_cost += row['shares'] * row['price']	

	return total_cost



if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

cost = portfolio_cost(filename)
print('Total cost:', cost)