[Contents](../Contents.md) \| [Previous (5.2 Encapsulation)](../05_Object_model/02_Classes_encapsulation.md) \| [Next (6.2 Customizing Iteration)](02_Customizing_iteration.md)

# 6.1 Iteration Protocol

This section looks at the underlying process of iteration.

### Iteration Everywhere

Many different objects support iteration.

```python
a = 'hello'
for c in a: # Loop over characters in a
    ...

b = { 'name': 'Dave', 'password':'foo'}
for k in b: # Loop over keys in dictionary
    ...

c = [1,2,3,4]
for i in c: # Loop over items in a list/tuple
    ...

f = open('foo.txt')
for x in f: # Loop over lines in a file
    ...
```

### Iteration: Protocol

Consider the `for`-statement.

```python
for x in obj:
    # statements
```

What happens under the hood?

```python
_iter = obj.__iter__()        # Get iterator object
while True:
    try:
        x = _iter.__next__()  # Get next item
        # statements ...
    except StopIteration:     # No more items
        break
```

All the objects that work with the `for-loop` implement this low-level
iteration protocol.

Example: Manual iteration over a list.

```python
>>> x = [1,2,3]
>>> it = x.__iter__()
>>> it
<listiterator object at 0x590b0>
>>> it.__next__()
1
>>> it.__next__()
2
>>> it.__next__()
3
>>> it.__next__()
Traceback (most recent call last):
File "<stdin>", line 1, in ? StopIteration
>>>
```

### Supporting Iteration

Knowing about iteration is useful if you want to add it to your own objects.
For example, making a custom container.

```python
class Portfolio:
    def __init__(self):
        self.holdings = []

    def __iter__(self):
        return self.holdings.__iter__()
    ...

port = Portfolio()
for s in port:
    ...
```

## Exercises

### Exercise 6.1: Iteration Illustrated

Create the following list:

```python
a = [1,9,4,25,16]
```

Manually iterate over this list.  Call `__iter__()` to get an iterator and
call the `__next__()` method to obtain successive elements.

```python
>>> i = a.__iter__()
>>> i
<listiterator object at 0x64c10>
>>> i.__next__()
1
>>> i.__next__()
9
>>> i.__next__()
4
>>> i.__next__()
25
>>> i.__next__()
16
>>> i.__next__()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
>>>
```

The `next()` built-in function is a shortcut for calling
the `__next__()` method of an iterator. Try using it on a file:

```python
>>> f = open('Data/portfolio.csv')
>>> f.__iter__()    # Note: This returns the file itself
<_io.TextIOWrapper name='Data/portfolio.csv' mode='r' encoding='UTF-8'>
>>> next(f)
'name,shares,price\n'
>>> next(f)
'"AA",100,32.20\n'
>>> next(f)
'"IBM",50,91.10\n'
>>>
```

Keep calling `next(f)` until you reach the end of the
file. Watch what happens.

### Exercise 6.2: Supporting Iteration

On occasion, you might want to make one of your own objects support
iteration--especially if your object wraps around an existing
list or other iterable.  In a new file `portfolio.py`, define the
following class:

```python
# portfolio.py

class Portfolio:

    def __init__(self, holdings):
        self._holdings = holdings

    @property
    def total_cost(self):
        return sum([s.cost for s in self._holdings])

    def tabulate_shares(self):
        from collections import Counter
        total_shares = Counter()
        for s in self._holdings:
            total_shares[s.name] += s.shares
        return total_shares
```

This class is meant to be a layer around a list, but with some
extra methods such as the `total_cost` property.  Modify the `read_portfolio()`
function in `report.py` so that it creates a `Portfolio` instance like this:

```
# report.py
...

import fileparse
from stock import Stock
from portfolio import Portfolio

def read_portfolio(filename):
    '''
    Read a stock portfolio file into a list of dictionaries with keys
    name, shares, and price.
    '''
    with open(filename) as file:
        portdicts = fileparse.parse_csv(file,
                                        select=['name','shares','price'],
                                        types=[str,int,float])

    portfolio = [ Stock(d['name'], d['shares'], d['price']) for d in portdicts ]
    return Portfolio(portfolio)
...
```

Try running the `report.py` program. You will find that it fails spectacularly due to the fact
that `Portfolio` instances aren't iterable.

```python
>>> import report
>>> report.portfolio_report('Data/portfolio.csv', 'Data/prices.csv')
... crashes ...
```

Fix this by modifying the `Portfolio` class to support iteration:

```python
class Portfolio:

    def __init__(self, holdings):
        self._holdings = holdings

    def __iter__(self):
        return self._holdings.__iter__()

    @property
    def total_cost(self):
        return sum([s.shares*s.price for s in self._holdings])

    def tabulate_shares(self):
        from collections import Counter
        total_shares = Counter()
        for s in self._holdings:
            total_shares[s.name] += s.shares
        return total_shares
```

After you've made this change, your `report.py` program should work again.   While you're
at it, fix up your `pcost.py` program to use the new `Portfolio` object. Like this:

```python
# pcost.py

import report

def portfolio_cost(filename):
    '''
    Computes the total cost (shares*price) of a portfolio file
    '''
    portfolio = report.read_portfolio(filename)
    return portfolio.total_cost
...
```

Test it to make sure it works:

```python
>>> import pcost
>>> pcost.portfolio_cost('Data/portfolio.csv')
44671.15
>>>
```

### Exercise 6.3: Making a more proper container

If making a container class, you often want to do more than just
iteration. Modify the `Portfolio` class so that it has some other
special methods like this:

```python
class Portfolio:
    def __init__(self, holdings):
        self._holdings = holdings

    def __iter__(self):
        return self._holdings.__iter__()

    def __len__(self):
        return len(self._holdings)

    def __getitem__(self, index):
        return self._holdings[index]

    def __contains__(self, name):
        return any([s.name == name for s in self._holdings])

    @property
    def total_cost(self):
        return sum([s.shares*s.price for s in self._holdings])

    def tabulate_shares(self):
        from collections import Counter
        total_shares = Counter()
        for s in self._holdings:
            total_shares[s.name] += s.shares
        return total_shares
```

Now, try some experiments using this new class:

```
>>> import report
>>> portfolio = report.read_portfolio('Data/portfolio.csv')
>>> len(portfolio)
7
>>> portfolio[0]
Stock('AA', 100, 32.2)
>>> portfolio[1]
Stock('IBM', 50, 91.1)
>>> portfolio[0:3]
[Stock('AA', 100, 32.2), Stock('IBM', 50, 91.1), Stock('CAT', 150, 83.44)]
>>> 'IBM' in portfolio
True
>>> 'AAPL' in portfolio
False
>>>
```

One important observation about this--generally code is considered
"Pythonic" if it speaks the common vocabulary of how other parts of
Python normally work.  For container objects, supporting iteration,
indexing, containment, and other kinds of operators is an important
part of this.

[Contents](../Contents.md) \| [Previous (5.2 Encapsulation)](../05_Object_model/02_Classes_encapsulation.md) \| [Next (6.2 Customizing Iteration)](02_Customizing_iteration.md)