import csv
from typing import Any, Callable, Dict, List, Optional, Sequence, Tuple, Union


def parse_csv(
        lines: Sequence[str],
        *,
        select: Optional[Sequence[str]] = None,
        types: Optional[Sequence[Callable]] = None,
        has_header: bool = True,
        delimiter: str = ',',
        silence_errors: bool = False
) -> List[Union[Dict[str, Any], Tuple]]:
    """
    Parse `lines` (supposedly list of strings in CSV format) into a list of records.
    Use `delimiter` as a delimiter for columns in lines.
    If `select` is provided, then only columns from `select` are added to result records.
    If `types` is provided, then values are converted according to it.
    If `has_header` is falsy, then return result is a list of tuples.
    If `has_header` is falsy and `select` is set, then RuntimeError is raised.
    If `silence_errors` is truthy, then conversion errors are silenced.
    """
    if isinstance(lines, str):
        raise ValueError('`lines` must be list of str (not str)')

    if not has_header and select is not None:
        raise RuntimeError('`select` argument requires column headers')

    rows = csv.reader(lines, delimiter=delimiter)

    indices: Optional[List[int]] = None
    headers: Optional[List[str]] = None
    if has_header:
        headers = next(rows)  # Read the file headers.

        # If a column selector was given, find indices of the specified columns.
        # Also narrow the set of headers used for resulting dictionaries.
        if select is not None:
            indices = [headers.index(column_name) for column_name in select]
            headers = list(select)

    records = []
    for row_number, row in enumerate(rows, start=1):
        # Skip rows with no data.
        if not row:
            continue

        # Filter the row if specific columns were selected.
        if indices is not None:
            row = [row[index] for index in indices]

        # Convert the row values to corresponding types.
        # Skip inconvertible rows.
        if types is not None:
            try:
                row = [func(value) for func, value in zip(types, row)]
            except ValueError as e:
                if not silence_errors:
                    print(f"Row {row_number}: Couldn't convert {row!r}")
                    print(f'Row {row_number}: Reason - {e}')
                continue

        if has_header:
            record = dict(zip(headers, row))
        else:
            record = tuple(row)
        records.append(record)

    return records
