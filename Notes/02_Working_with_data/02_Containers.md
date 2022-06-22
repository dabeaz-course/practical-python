[Contents](../Contents.md) \| [Previous (2.1 Datatypes)](01_Datatypes.md) \| [Next (2.3 Formatting)](03_Formatting.md)

# 2.2 Containers

This section discusses lists, dictionaries, and sets.

### Overview

Programs often have to work with many objects.

* A portfolio of stocks
* A table of stock prices

There are three main choices to use.

* Lists. Ordered data.
* Dictionaries. Unordered data.
* Sets. Unordered collection of unique items.

### Lists as a Container

Use a list when the order of the data matters. Remember that lists can hold any kind of object.
For example, a list of tuples.

```python
portfolio = [
    ('GOOG', 100, 490.1),
    ('IBM', 50, 91.3),
    ('CAT', 150, 83.44)
]

portfolio[0]            # ('GOOG', 100, 490.1)
portfolio[2]            # ('CAT', 150, 83.44)
```

### List construction

Building a list from scratch.

```python
records = []  # Initial empty list

# Use .append() to add more items
records.append(('GOOG', 100, 490.10))
records.append(('IBM', 50, 91.3))
...
```

An example when reading records from a file.

```python
records = []  # Initial empty list

with open('Data/portfolio.csv', 'rt') as f:
    next(f) # Skip header
    for line in f:
        row = line.split(',')
        records.append((row[0], int(row[1]), float(row[2])))
```

### Dicts as a Container

Dictionaries are useful if you want fast random lookups (by key name).  For
example, a dictionary of stock prices:

```python
prices = {
   'GOOG': 513.25,
   'CAT': 87.22,
   'IBM': 93.37,
   'MSFT': 44.12
}
```

Here are some simple lookups:

```python
>>> prices['IBM']
93.37
>>> prices['GOOG']
513.25
>>>
```

### Dict Construction

Example of building a dict from scratch.

```python
prices = {} # Initial empty dict

# Insert new items
prices['GOOG'] = 513.25
prices['CAT'] = 87.22
prices['IBM'] = 93.37
```

An example populating the dict from the contents of a file.

```python
prices = {} # Initial empty dict

with open('Data/prices.csv', 'rt') as f:
    for line in f:
        row = line.split(',')
        prices[row[0]] = float(row[1])
```

Note: If you try this on the `Data/prices.csv` file, you'll find that
it almost works--there's a blank line at the end that causes it to
crash.  You'll need to figure out some way to modify the code to
account for that (see Exercise 2.6).

### Dictionary Lookups

You can test the existence of a key.

```python
if key in d:
    # YES
else:
    # NO
```

You can look up a value that might not exist and provide a default value in case it doesn't.

```python
name = d.get(key, default)
```

An example:

```python
>>> prices.get('IBM', 0.0)
93.37
>>> prices.get('SCOX', 0.0)
0.0
>>>
```

### Composite keys

Almost any type of value can be used as a dictionary key in Python. A dictionary key must be of a type that is immutable.
For example, tuples:

```python
holidays = {
  (1, 1) : 'New Years',
  (3, 14) : 'Pi day',
  (9, 13) : "Programmer's day",
}
```

Then to access:

```python
>>> holidays[3, 14]
'Pi day'
>>>
```

*Neither a list, a set, nor another dictionary can serve as a dictionary key, because lists and dictionaries are mutable.*

### Sets

Sets are collection of unordered unique items.

```python
tech_stocks = { 'IBM','AAPL','MSFT' }
# Alternative syntax
tech_stocks = set(['IBM', 'AAPL', 'MSFT'])
```

Sets are useful for membership tests.

```python
>>> tech_stocks
set(['AAPL', 'IBM', 'MSFT'])
>>> 'IBM' in tech_stocks
True
>>> 'FB' in tech_stocks
False
>>>
```

Sets are also useful for duplicate elimination.

```python
names = ['IBM', 'AAPL', 'GOOG', 'IBM', 'GOOG', 'YHOO']

unique = set(names)
# unique = set(['IBM', 'AAPL','GOOG','YHOO'])
```

Additional set operations:

```python
unique.add('CAT')        # Add an item
unique.remove('YHOO')    # Remove an item

s1 = { 'a', 'b', 'c'}
s2 = { 'c', 'd' }
s1 | s2                 # Set union { 'a', 'b', 'c', 'd' }
s1 & s2                 # Set intersection { 'c' }
s1 - s2                 # Set difference { 'a', 'b' }
```

## Exercises

In these exercises, you start building one of the major programs used
for the rest of this course.  Do your work in the file `Work/report.py`.

### Exercise 2.4: A list of tuples

The file `Data/portfolio.csv` contains a list of stocks in a
portfolio.  In [Exercise 1.30](../01_Introduction/07_Functions.md), you
wrote a function `portfolio_cost(filename)` that read this file and
performed a simple calculation.

Your code should have looked something like this:

```python
# pcost.py

import csv

def portfolio_cost(filename):
    '''Computes the total cost (shares*price) of a portfolio file'''
    total_cost = 0.0

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            nshares = int(row[1])
            price = float(row[2])
            total_cost += nshares * price
    return total_cost
```

Using this code as a rough guide, create a new file `report.py`.  In
that file, define a function `read_portfolio(filename)` that opens a
given portfolio file and reads it into a list of tuples.  To do this,
you’re going to make a few minor modifications to the above code.

First, instead of defining `total_cost = 0`, you’ll make a variable
that’s initially set to an empty list. For example:

```python
portfolio = []
```

Next, instead of totaling up the cost, you’ll turn each row into a
tuple exactly as you just did in the last exercise and append it to
this list. For example:

```python
for row in rows:
    holding = (row[0], int(row[1]), float(row[2]))
    portfolio.append(holding)
```

Finally, you’ll return the resulting `portfolio` list.

Experiment with your function interactively (just a reminder that in
order to do this, you first have to run the `report.py` program in the
interpreter):

*Hint: Use `-i` when executing the file in the terminal*

```python
>>> portfolio = read_portfolio('Data/portfolio.csv')
>>> portfolio
[('AA', 100, 32.2), ('IBM', 50, 91.1), ('CAT', 150, 83.44), ('MSFT', 200, 51.23),
    ('GE', 95, 40.37), ('MSFT', 50, 65.1), ('IBM', 100, 70.44)]
>>>
>>> portfolio[0]
('AA', 100, 32.2)
>>> portfolio[1]
('IBM', 50, 91.1)
>>> portfolio[1][1]
50
>>> total = 0.0
>>> for s in portfolio:
        total += s[1] * s[2]

>>> print(total)
44671.15
>>>
```

This list of tuples that you have created is very similar to a 2-D
array.  For example, you can access a specific column and row using a
lookup such as `portfolio[row][column]` where `row` and `column` are
integers.

That said, you can also rewrite the last for-loop using a statement like this:

```python
>>> total = 0.0
>>> for name, shares, price in portfolio:
            total += shares*price

>>> print(total)
44671.15
>>>
```

### Exercise 2.5: List of Dictionaries

Take the function you wrote in Exercise 2.4 and modify to represent each
stock in the portfolio with a dictionary instead of a tuple.  In this
dictionary use the field names of "name", "shares", and "price" to
represent the different columns in the input file.

Experiment with this new function in the same manner as you did in
Exercise 2.4.

```python
>>> portfolio = read_portfolio('Data/portfolio.csv')
>>> portfolio
[{'name': 'AA', 'shares': 100, 'price': 32.2}, {'name': 'IBM', 'shares': 50, 'price': 91.1},
    {'name': 'CAT', 'shares': 150, 'price': 83.44}, {'name': 'MSFT', 'shares': 200, 'price': 51.23},
    {'name': 'GE', 'shares': 95, 'price': 40.37}, {'name': 'MSFT', 'shares': 50, 'price': 65.1},
    {'name': 'IBM', 'shares': 100, 'price': 70.44}]
>>> portfolio[0]
{'name': 'AA', 'shares': 100, 'price': 32.2}
>>> portfolio[1]
{'name': 'IBM', 'shares': 50, 'price': 91.1}
>>> portfolio[1]['shares']
50
>>> total = 0.0
>>> for s in portfolio:
        total += s['shares']*s['price']

>>> print(total)
44671.15
>>>
```

Here, you will notice that the different fields for each entry are
accessed by key names instead of numeric column numbers.  This is
often preferred because the resulting code is easier to read later.

Viewing large dictionaries and lists can be messy. To clean up the
output for debugging, consider using the `pprint` function.

```python
>>> from pprint import pprint
>>> pprint(portfolio)
[{'name': 'AA', 'price': 32.2, 'shares': 100},
    {'name': 'IBM', 'price': 91.1, 'shares': 50},
    {'name': 'CAT', 'price': 83.44, 'shares': 150},
    {'name': 'MSFT', 'price': 51.23, 'shares': 200},
    {'name': 'GE', 'price': 40.37, 'shares': 95},
    {'name': 'MSFT', 'price': 65.1, 'shares': 50},
    {'name': 'IBM', 'price': 70.44, 'shares': 100}]
>>>
```

### Exercise 2.6: Dictionaries as a container

A dictionary is a useful way to keep track of items where you want to
look up items using an index other than an integer.  In the Python
shell, try playing with a dictionary:

```python
>>> prices = { }
>>> prices['IBM'] = 92.45
>>> prices['MSFT'] = 45.12
>>> prices
... look at the result ...
>>> prices['IBM']
92.45
>>> prices['AAPL']
... look at the result ...
>>> 'AAPL' in prices
False
>>>
```

The file `Data/prices.csv` contains a series of lines with stock prices.
The file looks something like this:

```csv
"AA",9.22
"AXP",24.85
"BA",44.85
"BAC",11.27
"C",3.72
...
```

Write a function `read_prices(filename)` that reads a set of prices
such as this into a dictionary where the keys of the dictionary are
the stock names and the values in the dictionary are the stock prices.

To do this, start with an empty dictionary and start inserting values
into it just as you did above. However, you are reading the values
from a file now.

We’ll use this data structure to quickly lookup the price of a given
stock name.

A few little tips that you’ll need for this part. First, make sure you
use the `csv` module just as you did before—there’s no need to
reinvent the wheel here.

```python
>>> import csv
>>> f = open('Data/prices.csv', 'r')
>>> rows = csv.reader(f)
>>> for row in rows:
        print(row)


['AA', '9.22']
['AXP', '24.85']
...
[]
>>>
```

The other little complication is that the `Data/prices.csv` file may
have some blank lines in it. Notice how the last row of data above is
an empty list—meaning no data was present on that line.

There’s a possibility that this could cause your program to die with
an exception.  Use the `try` and `except` statements to catch this as
appropriate.  Thought: would it be better to guard against bad data with
an `if`-statement instead?

Once you have written your `read_prices()` function, test it
interactively to make sure it works:

```python
>>> prices = read_prices('Data/prices.csv')
>>> prices['IBM']
106.28
>>> prices['MSFT']
20.89
>>>
```

### Exercise 2.7: Finding out if you can retire

Tie all of this work together by adding a few additional statements to
your `report.py` program that computes gain/loss. These statements
should take the list of stocks in Exercise 2.5 and the dictionary of
prices in Exercise 2.6 and compute the current value of the portfolio
along with the gain/loss.

[Contents](../Contents.md) \| [Previous (2.1 Datatypes)](01_Datatypes.md) \| [Next (2.3 Formatting)](03_Formatting.md)
