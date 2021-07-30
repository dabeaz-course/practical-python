from collections import Counter
from typing import Iterator, List

from stock import Stock


class Portfolio:
    def __init__(self, holdings: List[Stock]) -> None:
        self._holdings = holdings

    def __iter__(self) -> Iterator[Stock]:
        return self._holdings.__iter__()

    @property
    def total_cost(self) -> float:
        return sum([s.cost for s in self._holdings])

    def tabulate_shares(self) -> Counter:
        total_shares = Counter()
        for s in self._holdings:
            total_shares[s.name] += s.shares
        return total_shares
