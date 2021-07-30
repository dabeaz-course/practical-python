from collections import Counter
from typing import Iterator, List

from stock import Stock


class Portfolio:
    def __init__(self, holdings: List[Stock]) -> None:
        self._holdings = holdings

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

    @property
    def total_cost(self) -> float:
        return sum([s.cost for s in self])

    def tabulate_shares(self) -> Counter:
        total_shares = Counter()
        for s in self._holdings:
            total_shares[s.name] += s.shares
        return total_shares
