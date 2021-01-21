# fileparse.py
#
# Exercise 3.3
import csv

from rich.console import Console
from rich.pretty import install

print = Console(width=100).print
install(Console(width=100))


def parse_csv(filename: str, select=None) -> list[dict]:
    '''
    Parse a CSV file into a list of records
    '''
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)
        indices = {headers.index(field) for field in select} if select else None
        print(indices)
        records = []

        for row in rows:
            if not row:
                continue

            if select:
                record = {field: row[idx] for field, idx in zip(select, indices)}
            else:
                record = dict(zip(headers, row))

            records.append(record)
    return records

parsed_csv = parse_csv('Work/Data/portfolio.csv', select=['name', 'name'])
print(parsed_csv)
