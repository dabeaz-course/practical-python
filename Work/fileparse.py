# fileparse.py
#
# Exercise 3.3

import csv


def parse_csv(filename, select: list = [], types: list = []):
    """
    Parse a CSV file into a list of records
    """
    with open(filename) as f:
        rows = csv.reader(f)

        # Read the file headers
        file_headers = next(rows)
        headers = select if select else file_headers
        indices = (
            [headers.index(name) for name in select]
            if select
            else [i for i in range(len(headers))]
        )
        records = []
        for row in rows:
            if not row:  # Skip rows with no data
                continue
            select_row = [row[col] for col in indices]
            if types:
                select_row = [func(col) for func, col in zip(types, select_row)]
            record = dict(zip(headers, select_row))
            records.append(record)

    return records
