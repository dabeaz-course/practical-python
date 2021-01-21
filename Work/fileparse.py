# fileparse.py
#
# Exercise 3.3
import csv

from rich.console import Console
from rich.pretty import install

print = Console(width=100).print
install(Console(width=100))


def parse_csv(filename: str, *, select=None, types=None,
              has_headers=True, delimiter=',') -> list[dict]:

    ''' Parse a CSV file into a list of records '''
    with open(filename) as f:
        rows = csv.reader(f, delimiter=delimiter)
        headers = next(rows) if has_headers else []

        if select:
            indices = [headers.index(field) for field in select]
            headers = select

        records = []
        for row in rows:
            if not row:
                continue

            if select:
                row = [row[idx] for idx in indices]

            if types:
                row = [func(val) for func, val in zip(types, row)]

            if headers:
                record = dict(zip(headers, row))
            else:
                record = tuple(row)

            records.append(record)

    return records

# parsed_csv = parse_csv('Work/Data/prices.csv', has_headers=False, types=[str, float])
# parsed_csv = parse_csv('Work/Data/portfolio.dat', types=[str, int, float], delimiter=' ')
parsed_csv = parse_csv('Work/Data/portfolio.csv', select=['name', 'price', 'shares'], types=[str, float, int])
print(parsed_csv)
