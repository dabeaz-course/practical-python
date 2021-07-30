import csv
from typing import Any, Dict, Iterator, List, Type

import tableformat
from follow import follow
from report import read_portfolio


def parse_stock_data(lines: Iterator[str]) -> Iterator:
    rows = csv.reader(lines)
    rows = select_columns(rows, [0, 1, 4])
    rows = convert_types(rows, [str, float, float])
    rows = make_dicts(rows, ['name', 'price', 'change'])
    return rows


def select_columns(rows: Iterator[List[str]], indices: List[int]) -> Iterator[List[str]]:
    for row in rows:
        yield [row[index] for index in indices]


def convert_types(rows: Iterator[List[str]], types: List[Type]) -> Iterator[List[Any]]:
    for row in rows:
        yield [t(v) for t, v in zip(types, row)]


def make_dicts(rows: Iterator[List[Any]], headers: List[str]) -> Iterator[Dict[str, Any]]:
    for row in rows:
        yield dict(zip(headers, row))


def ticker(portfolio_file: str, stock_log_file: str, fmt: str) -> None:
    portfolio = read_portfolio(portfolio_file)
    lines = follow(stock_log_file)
    rows = parse_stock_data(lines)
    rows = (row for row in rows if row['name'] in portfolio)
    formatter = tableformat.create_formatter(fmt)
    formatter.headings(['Name', 'Price', 'Change'])
    for row in rows:
        formatter.row([row['name'], f'{row["price"]:.2f}', f'{row["change"]:.2f}'])


def main(args: List[str]) -> None:
    if len(args) != 4:
        raise SystemExit(f'Usage: {args[0]} PORTFOLIO_FILE STOCK_LOG_FILE REPORT_FORMAT')
    ticker(args[1], args[2], args[3])


if __name__ == '__main__':
    import sys

    main(sys.argv)
