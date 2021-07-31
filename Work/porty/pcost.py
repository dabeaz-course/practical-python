from typing import List

from .report import read_portfolio


def portfolio_cost(filename: str) -> float:
    portfolio = read_portfolio(filename)
    return portfolio.total_cost


def main(args: List[str]) -> None:
    if len(args) != 2:
        raise SystemExit(f'Usage: {args[0]} PORTFOLIO_FILE')
    print(f'Total cost: {portfolio_cost(args[1])}')


if __name__ == '__main__':
    import sys

    main(sys.argv)
