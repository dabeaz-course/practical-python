# pcost.py
#
# Exercise 1.27
import csv
#filename = 'Work/Data/portfolio.csv'
def portfolio_cost(filename):
    total_cost =0
    with open(filename,'rt') as file :
        rows = csv.reader(file)
        headers = next(rows)
        for row in rows:
            try:
                nshares = int(row[1])
                price = float(row[2])
                total_cost += nshares * price
            # This catches errors in int() and float() conversions above
            except ValueError:
                print('Bad row:', row)
    return total_cost

cost = portfolio_cost('Work/Data/missing.csv')    
#portfolio_cost('Data/missing.csv')
print('Total cost:', cost)

