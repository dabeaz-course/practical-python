import os
import time
from typing import Iterator, List

from . import report


def follow(filename: str) -> Iterator[str]:
    """
    Generate lines being written at the end of a file `filename`.
    """
    with open(filename) as f:
        f.seek(0, os.SEEK_END)  # Move file pointer 0 bytes from end of file
        while True:
            line = f.readline()
            if line == '':
                time.sleep(0.1)  # Sleep briefly and retry
                continue
            yield line


def main(args: List[str]) -> None:
    """
    Watch the stream of stock data and prints a ticker showing information
    for only those stocks in a portfolio.
    """

    if len(args) != 3:
        raise SystemExit(f'Usage: {args[0]} PORTFOLIO_FILE STOCK_LOG_FILE')

    portfolio = report.read_portfolio(args[1])

    for line in follow(args[2]):
        fields = line.split(',')
        name = fields[0].strip('"')
        price = float(fields[1])
        change = float(fields[4])
        if name in portfolio:
            print(f'{name:>10s} {price:>10.2f} {change:>10.2f}')


if __name__ == '__main__':
    import sys

    main(sys.argv)
