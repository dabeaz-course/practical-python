"""This class is a container. Some wrapper around a list or another iterable
object. Therefore, such class should keep all the properties of the original
object e.g.: It has to be iterable, It has to be possible to calculate the
length, elements indexing should be possible, checking for element presence
sould be possible.
"""

class Portfolio:

    def __init__(self, holdings):
        self._holdings = holdings

    # Use this if you want to make an object iterable
    def __iter__(self):
        return self._holdings.__iter__()

    # With this you can use len()
    def __len__(self):
        return len(self._holdings)

    # enables indexing (portfolio[0])
    def __getitem__(self, index):
        return self._holdings[index]

    # you can check whether element is in the container
    # In this case you can check for the name
    def __contains__(self, name):
        return any([s.name == name for s in self._holdings])

    @property
    def total_cost(self):
        return sum(s.cost for s in self._holdings)

    def tabulate_shares(self):
        from collections import Counter
        total_shares = Counter()
        for s in self._holdings:
            total_shares[s.name] += s.shares
        return total_shares
