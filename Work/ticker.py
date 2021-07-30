import csv
from typing import Any, Dict, Iterator, List, Type

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


def filter_symbols(rows: Iterator[Dict[str, Any]], names) -> Iterator[Dict[str, Any]]:
    for row in rows:
        if row['name'] in names:
            yield row


def main():
    portfolio = read_portfolio('Data/portfolio.csv')
    lines = follow('Data/stocklog.csv')
    rows = parse_stock_data(lines)
    rows = filter_symbols(rows, portfolio)
    for row in rows:
        print(row)


if __name__ == '__main__':
    main()
