import csv
from typing import Any, Callable, Dict, List, Optional, Sequence


def parse_csv(
        filename: str,
        *,
        select: Optional[Sequence[str]] = None,
        types: Optional[Sequence[Callable]] = None,
        has_header: bool = True,
        delimiter: str = ','
) -> List[Dict[str, Any]]:
    """
    Parse a csv-file `filename` into a list of records.
    Use `delimiter` as a delimiter for columns in the file.
    If `select` is provided, then only columns from `select` are added to result records.
    If `types` is provided, then values are converted according to it.
    If `has_header` is falsy, then return result is a list of tuples.
    If `has_header` is false and `select` is set RuntimeError is raised.
    """
    if not has_header and select is not None:
        raise RuntimeError('`select` argument requires column headers')

    with open(filename) as f:
        rows = csv.reader(f, delimiter=delimiter)

        indices: Optional[List[int]] = None
        if has_header:
            headers = next(rows)  # Read the file headers.

            # If a column selector was given, find indices of the specified columns.
            # Also narrow the set of headers used for resulting dictionaries.
            if select is not None:
                indices = [headers.index(column_name) for column_name in select]
                headers = list(select)

        records = []
        for row in rows:
            # Skip rows with no data.
            if not row:
                continue

            # Filter the row if specific columns were selected.
            if indices is not None:
                row = [row[index] for index in indices]

            # Convert the row values to corresponding types
            if types is not None:
                row = [func(value) for func, value in zip(types, row)]

            if has_header:
                record = dict(zip(headers, row))
            else:
                record = tuple(row)
            records.append(record)

    return records
