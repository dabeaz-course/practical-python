# 2.7 Objects

import sys
import csv

def parse_date_slashes(string_data):
    return tuple(string_data.split('/'))
    
def read_portfolio(filename):

    portfolio = []
    with open(filename,'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        types = [str, float, parse_date_slashes, str, float, float, float, float, int]


        for rowno,row in enumerate(rows):
            try:
                portfolio.append({headers:func(val) for headers,func,val in zip(headers,types,row)})
            except ValueError:
                print(f'Rowno:{rowno} had an error: {row}')

        return portfolio

if len(sys.argv) < 2:
    portfolio = read_portfolio('Data/dowstocks.csv')
else:
    portfolio = read_portfolio(sys.argv[1])

