# pcost.py
#
# Exercise 1.27

# opens data/portfolio.csv , reads all lines, and calculates how much it cost to purchase all of the shares in the portfolio. 
# Total cost 44671.15  <- output
import csv
import sys

def portfolioCost(filename):
    '''
    Computes the total cost (shares*price) of a portfolio file
    '''
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        header = next(rows) # skips header
        total = 0.0
        for rowNum, row in enumerate(rows, start=1):
            record = dict(zip(header, row))

            try: 
                # shares = int(row[1])
                # price = float(row[2])
                shares = int(record['shares'])
                price = float(record['price'])

                total += shares * price
            except ValueError:
                # print("Row", rowNum, ": Couldn't parse:", row)
                print(f'Row {rowNum}: Couldn\'t parse: {row}')
    return total

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    print("Missing file input.")

# cost = portfolioCost('Data/missing.csv')
# cost = portfolioCost('Data/portfolio.csv')
cost = portfolioCost(filename)
print('Total cost:', cost)