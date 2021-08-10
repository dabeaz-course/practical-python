# fileparse.py
#
# Exercise 3.3

import csv


def parse_csv(filename: str, select=None, types=list, has_headers=True, delimiter=',', silence_errors=True) -> list:
    """
    Parses a CSV file with optional types, headers and select vector
    @filename: 
    """

    with open(filename, 'rt') as f:

        rows = csv.reader(f, delimiter=delimiter)
        if has_headers:
            headers = next(rows)

        records = []
        
        if select and has_headers:
            indices = [headers.index(colname) for colname in select]
            headers = select
        elif (select and not has_headers):
        	raise RuntimeError("select argument requires column headers")
        else:
            indices = []

        for rowno,row in enumerate(rows):
            try:
                if not row:  # Skip empty rows.
                    continue
                if indices:
                    row = [row[index] for index in indices]
                if types and has_headers:
                    record = {colname: fun(value) for colname,
                              fun, value in zip(headers, types, row)}
                if types and not has_headers:
                    record = tuple([(fun(value))
                                   for fun, value in zip(types, row)])
                else:
                    record = {colname: value for colname,
                              value in zip(headers, row)}
            except ValueError as e:
                if not silence_errors:
                    print(f"Row {rowno}: Couldn't convert {row}")
                    print(f"Row {rowno}: Reason {e}")

            records.append(record)

        return records


"""print(parse_csv('Data/portfolio.csv',
      select=['name', 'shares', 'price'], types=[str, int, float], has_headers=True))
"""
#print(parse_csv('Data/prices.csv', select=None, types=[str,float],has_headers=False,delimiter=','))
#print(parse_csv('Data/portfolio.dat', select=None, types=[str,int,float],has_headers=True,delimiter=' '))
#print(parse_csv('Data/prices.csv', select=None, types=[str,float],has_headers=False,delimiter=','))
#portfolio = parse_csv('Data/missing.csv', types=[str,int, float], silence_errors=False)