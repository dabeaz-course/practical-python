# pcost.py
#
# Exercise 1.27
import csv
import sys
#filename = 'Work/Data/portfolio.csv'
def portfolio_cost(filename):
    total_cost =0
    with open(filename,'rt') as file :
        rows = csv.reader(file)
        headers = next(rows)
        for rowno, row in enumerate(rows, start=1):
            record = dict(zip(headers, row))
            try:
                nshares = int(row[1])
                price = float(row[2])
                total_cost += nshares * price
            except ValueError:
                print(f'Row {rowno}: Bad row: {row}')
    return total_cost

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Work/Data/portfoliodate.csv'

cost = portfolio_cost(filename)    
#portfolio_cost('Data/missing.csv')
print('Total cost:', cost)

