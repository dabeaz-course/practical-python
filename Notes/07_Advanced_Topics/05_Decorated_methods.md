[Contents](../Contents.md) \| [Previous (7.4 Decorators)](04_Function_decorators.md) \| [Next (8 Testing and Debugging)](../08_Testing_debugging/00_Overview.md)

# 7.5 Decorated Methods

This section discusses a few built-in decorators that are used in
combination with method definitions.

### Predefined Decorators

There are predefined decorators used to specify special kinds of methods in class definitions.

```python
class Foo:
    def bar(self,a):
        ...

    @staticmethod
    def spam(a):
        ...

    @classmethod
    def grok(cls,a):
        ...

    @property
    def name(self):
        ...
```

Let's go one by one.

### Static Methods

`@staticmethod` is used to define a so-called *static* class methods
(from C++/Java).  A static method is a function that is part of the
class, but which does *not* operate on instances.

```python
class Foo(object):
    @staticmethod
    def bar(x):
        print('x =', x)

>>> Foo.bar(2) x=2
>>>
```

Static methods are sometimes used to implement internal supporting
code for a class.  For example, code to help manage created instances
(memory management, system resources, persistence, locking, etc).
They're also used by certain design patterns (not discussed here).

### Class Methods

`@classmethod` is used to define class methods.  A class method is a
method that receives the *class* object as the first parameter instead
of the instance.

```python
class Foo:
    def bar(self):
        print(self)

    @classmethod
    def spam(cls):
        print(cls)

>>> f = Foo()
>>> f.bar()
<__main__.Foo object at 0x971690>   # The instance `f`
>>> Foo.spam()
<class '__main__.Foo'>              # The class `Foo`
>>>
```

Class methods are most often used as a tool for defining alternate constructors.

```python
class Date:
    def __init__(self,year,month,day):
        self.year = year
        self.month = month
        self.day = day

    @classmethod
    def today(cls):
        # Notice how the class is passed as an argument
        tm = time.localtime()
        # And used to create a new instance
        return cls(tm.tm_year, tm.tm_mon, tm.tm_mday)

d = Date.today()
```

Class methods solve some tricky problems with features like inheritance.

```python
class Date:
    ...
    @classmethod
    def today(cls):
        # Gets the correct class (e.g. `NewDate`)
        tm = time.localtime()
        return cls(tm.tm_year, tm.tm_mon, tm.tm_mday)

class NewDate(Date):
    ...

d = NewDate.today()
```

## Exercises

### Exercise 7.11: Class Methods in Practice

In your `report.py` and `portfolio.py` files, the creation of a `Portfolio`
object is a bit muddled.  For example, the `report.py` program has code like this:

```python
def read_portfolio(filename, **opts):
    '''
    Read a stock portfolio file into a list of dictionaries with keys
    name, shares, and price.
    '''
    with open(filename) as lines:
        portdicts = fileparse.parse_csv(lines,
                                        select=['name','shares','price'],
                                        types=[str,int,float],
                                        **opts)

    portfolio = [ Stock(**d) for d in portdicts ]
    return Portfolio(portfolio)
```

and the `portfolio.py` file defines `Portfolio()` with an odd initializer
like this:

```python
class Portfolio:
    def __init__(self, holdings):
        self.holdings = holdings
    ...
```

Frankly, the chain of responsibility is all a bit confusing because the
code is scattered.    If a `Portfolio` class is supposed to contain
a list of `Stock` instances, maybe you should change the class to be a bit more clear.
Like this:

```python
# portfolio.py

import stock

class Portfolio:
    def __init__(self):
        self.holdings = []

    def append(self, holding):
        if not isinstance(holding, stock.Stock):
            raise TypeError('Expected a Stock instance')
        self.holdings.append(holding)
    ...
```

If you want to read a portfolio from a CSV file, maybe you should make a
class method for it:

```python
# portfolio.py

import fileparse
import stock

class Portfolio:
    def __init__(self):
        self.holdings = []

    def append(self, holding):
        if not isinstance(holding, stock.Stock):
            raise TypeError('Expected a Stock instance')
        self.holdings.append(holding)

    @classmethod
    def from_csv(cls, lines, **opts):
        self = cls()
        portdicts = fileparse.parse_csv(lines,
                                        select=['name','shares','price'],
                                        types=[str,int,float],
                                        **opts)

        for d in portdicts:
            self.append(stock.Stock(**d))

        return self
```

To use this new Portfolio class, you can now write code like this:

```
>>> from portfolio import Portfolio
>>> with open('Data/portfolio.csv') as lines:
...     port = Portfolio.from_csv(lines)
...
>>>
```

Make these changes to the `Portfolio` class and modify the `report.py`
code to use the class method.

[Contents](../Contents.md) \| [Previous (7.4 Decorators)](04_Function_decorators.md) \| [Next (8 Testing and Debugging)](../08_Testing_debugging/00_Overview.md)
