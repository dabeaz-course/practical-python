from __future__ import annotations

from collections import Counter
from typing import Iterable, Iterator

from .fileparse import parse_csv
from .stock import Stock


class Portfolio:
    def __init__(self) -> None:
        self._holdings = []

    @classmethod
    def from_csv(cls, lines: Iterable[str], **kwargs) -> Portfolio:
        self = cls()
        portfolio_as_dicts = parse_csv(
            lines=lines,
            select=('name', 'shares', 'price'),
            types=(str, int, float),
            **kwargs
        )
        for d in portfolio_as_dicts:
            self.append(Stock(**d))
        return self

    def __iter__(self) -> Iterator[Stock]:
        return iter(self._holdings)

    def __len__(self) -> int:
        return len(self._holdings)

    def __getitem__(self, index: int) -> Stock:
        return self._holdings[index]

    def __contains__(self, name: str) -> bool:
        return any(s.name == name for s in self)

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}({self._holdings!r})'

    def append(self, holding: Stock) -> None:
        if not isinstance(holding, Stock):
            raise TypeError(f'Expected a {Stock.__name__} instance')
        self._holdings.append(holding)

    @property
    def total_cost(self) -> float:
        return sum([s.cost for s in self])

    def tabulate_shares(self) -> Counter:
        total_shares = Counter()
        for s in self._holdings:
            total_shares[s.name] += s.shares
        return total_shares
