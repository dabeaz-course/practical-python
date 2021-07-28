from typing import Sequence


class TableFormatter:
    def headings(self, headers: Sequence[str]) -> None:
        """
        Output table headings.
        """
        raise NotImplementedError

    def row(self, row_data: Sequence[str]) -> None:
        """
        Output a single row of table data.
        """
        raise NotImplementedError


class TextTableFormatter(TableFormatter):
    """
    Output a table in plain-text format.
    """

    def headings(self, headers: Sequence[str]) -> None:
        print(*(f'{h:>10s}' for h in headers))
        print(*('-' * 10 for _ in range(len(headers))))

    def row(self, row_data: Sequence[str]) -> None:
        print(*(f'{d:>10s}' for d in row_data))


class CSVTableFormatter(TableFormatter):
    """
    Output a table in CSV format.
    """

    def headings(self, headers: Sequence[str]) -> None:
        print(','.join(headers))

    def row(self, row_data: Sequence[str]) -> None:
        print(','.join(row_data))


class HTMLTableFormatter(TableFormatter):
    """
    Output a table in HTML table format
    """

    def headings(self, headers: Sequence[str]) -> None:
        print(f'<tr>{"".join(f"<th>{h}</th>" for h in headers)}</tr>')

    def row(self, row_data: Sequence[str]) -> None:
        print(f'<tr>{"".join(f"<td>{d}</td>" for d in row_data)}</tr>')


def create_formatter(name: str) -> TableFormatter:
    if name == 'txt':
        return TextTableFormatter()
    elif name == 'csv':
        return CSVTableFormatter()
    elif name == 'html':
        return HTMLTableFormatter()
    else:
        raise RuntimeError(f'Unknown format {name}')
