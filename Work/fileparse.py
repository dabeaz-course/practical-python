# fileparse.py
#
# Exercise 3.3
# fileparse.py
import csv

def parse_csv(filename, select=None,types=[str, int, float]):
    '''
    Parse a CSV file
    '''
    with open(filename) as f:
        rows = csv.reader(f)

        # Read the file headers
        headers = next(rows)

        # If a column selector was given, find indices of the specified columns.
        # Also narrow the set of headers used for resulting dictionaries
        if select:
            indices = [headers.index(colname) for colname in select]
            headers = select
        else:
            indices = []

        records = []
        for row in rows:
            if not row:    # Skip rows with no data
                continue
            # Filter the row if specific columns were selected
            if indices:
                row = [ row[index] for index in indices ]

            # Make a dictionary
            record = dict(zip(headers, row))
            records.append(record)

    print(record)

    return records

parse_csv('Work/Data/portfolio.csv')
