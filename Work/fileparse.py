import csv


def parse_csv(filename):
    """
    Parse a csv-file into a list of records.
    """
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)  # Read the file headers.
        records = []
        for row in rows:
            if not row:  # Skip rows with no data.
                continue
            record = dict(zip(headers, row))
            records.append(record)

    return records
