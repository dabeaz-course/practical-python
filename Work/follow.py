import os
import time
from typing import Iterator, List


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
    if len(args) != 2:
        raise SystemExit(f'Usage: {args[0]} STOCK_LOG_FILE')

    for line in follow(args[1]):
        fields = line.split(',')
        name = fields[0].strip('"')
        price = float(fields[1])
        change = float(fields[4])
        if change < 0:
            print(f'{name:>10s} {price:>10.2f} {change:>10.2f}')


if __name__ == '__main__':
    import sys

    main(sys.argv)
