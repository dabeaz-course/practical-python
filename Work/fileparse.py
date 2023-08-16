# fileparse.py
#
# Exercise 3.3

import csv

def parse_csv(filename, select: list):
    '''
    Parse a CSV file into a list of records
    '''
    with open(filename) as f:
        rows = csv.reader(f)

        # Read the file headers
        headers = next(rows)
        select_indices = [headers.index(name) for name in select] \
            if select \
            else [i for i in range(len(headers))]
        if select:
            headers = select
        records = []
        for row in rows:
            if not row:    # Skip rows with no data
                continue
            record = dict(zip(
                headers,
                [row[i] for i in select_indices]))
            records.append(record)

    return records