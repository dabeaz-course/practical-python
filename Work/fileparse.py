# fileparse.py
#
# Exercise 3.3
import csv


def parse_csv(
    filename: str,
    select: list = [],
    types: list = [],
    has_headers: bool = True,
    delimiter: str = ",",
) -> list:
    """
    Parse a CSV file into a list of records
    """
    with open(filename) as f:
        rows = csv.reader(f, delimiter=delimiter)
        if has_headers:
            orig_headers = next(rows)
            headers = select if select else orig_headers
            indices = [headers.index(name) for name in headers]
        records = []
        for orig_row in rows:
            if not orig_row:
                continue
            row = [orig_row[i] for i in indices] if has_headers else orig_row
            if types:
                row = [func(field) for func, field in zip(types, row)]
            record = dict(zip(headers, row)) if has_headers else tuple(row)
            records.append(record)
    return records
