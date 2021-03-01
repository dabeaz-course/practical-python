# fileparse.py
#
# Exercise 3.3

import csv

def parse_csv(filename, select=None, types=None, has_headers=True, delimiter=","):
    """Parse a csv file into a list of records

    select (list): Accepts a list of column names to select when opening the file
    types (list): Accepts a list of column types. Types for all columns,
        or selected columns must, be specified.
    """
    with open(filename) as f:
        rows = csv.reader(f, delimiter=delimiter)

        # Read the file headers
        if has_headers:
            header = next(rows)

        if select:
            indices = [header.index(colname) for colname in select]
            header = select
        else:
            indices = []

        records = []
        for row in rows:
            if not row:  # Skip rows with no data
                continue
            # Filter the row is specific columns were selected
            if indices:
                row = [row[index] for index in indices]
            # Convert data types
            if types:
                row = [func(val) for func, val in zip(types, row)]
            # Make dictionary
            record = dict(zip(header, row))
            records.append(record)

    return records
