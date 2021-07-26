# prices.py
#
# Exercise 2.6

def read_prices(filename):
    '''Read prices form a file and store as dictionary.'''

    import csv

    prices = {}

    with open(filename,'rt') as f:
        rows = csv.reader(f)
        try:
            for key,value in rows:
                prices[key] = float(value)
        except ValueError:
            pass

    return prices


prices = read_prices('Data/prices.csv')

from pprint import pprint

print(prices['IBM'])
print(prices['MSFT'])

pprint(prices)


