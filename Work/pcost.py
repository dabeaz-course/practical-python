# pcost.py
#
# Exercise 1.27
"""
The columns in portfolio.csv correspond to the stock name, number of shares, and purchase price of a single stock holding. Write a program called pcost.py that opens this file, reads all lines, and calculates how much it cost to purchase all of the shares in the portfolio.

Hint: to convert a string to an integer, use int(s). To convert a string to a floating point, use float(s).

Your program should print output such as the following:

Total cost 44671.15

"""
import csv

def portfolio_cost(file_name):
    total_cost = 0.0
    try:
        file = open(file_name)
        rows = csv.reader(file)
        header = next(rows)
        for rowno, row in enumerate(rows):
            record = dict(zip(header,row))
            try:
                nshares = int(record['shares'])
                price = float(record['price'])
                total_cost += nshares * price
            except ValueError:
                print(f'{rowno:>10d}: Could not parse {row:}')
        file.close()
    except FileNotFoundError:
        print(f"Invalid: Couldn't find {file_name}")
    return total_cost


def portfolio_cost_py(file_name):
    with open('../Work/Data/' + file_name, 'rt') as file:
        headers = next(file).split(',')
        total_cost = 0.0
        for line in file:
            row = line.split(',')
            try:
                total_cost += int(row[1]) * float(row[2])
            except ValueError:
                print("Couldn't parse", line)
    return total_cost



