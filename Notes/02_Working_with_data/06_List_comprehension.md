[Contents](../Contents.md) \| [Previous (2.5 Collections)](05_Collections.md) \| [Next (2.7 Object Model)](07_Objects.md)

# 2.6 List Comprehensions

A common task is processing items in a list.  This section introduces list comprehensions,
a powerful tool for doing just that.

### Creating new lists

A list comprehension creates a new list by applying an operation to
each element of a sequence.

```python
>>> a = [1, 2, 3, 4, 5]
>>> b = [2*x for x in a ]
>>> b
[2, 4, 6, 8, 10]
>>>
```

Another example:

```python
>>> names = ['Elwood', 'Jake']
>>> a = [name.lower() for name in names]
>>> a
['elwood', 'jake']
>>>
```

The general syntax is: `[ <expression> for <variable_name> in <sequence> ]`.

### Filtering

You can also filter during the list comprehension.

```python
>>> a = [1, -5, 4, 2, -2, 10]
>>> b = [2*x for x in a if x > 0 ]
>>> b
[2, 8, 4, 20]
>>>
```

### Use cases

List comprehensions are hugely useful.  For example, you can collect values of a specific
dictionary fields:

```python
stocknames = [s['name'] for s in stocks]
```

You can perform database-like queries on sequences.

```python
a = [s for s in stocks if s['price'] > 100 and s['shares'] > 50 ]
```

You can also combine a list comprehension with a sequence reduction:

```python
cost = sum([s['shares']*s['price'] for s in stocks])
```

### General Syntax

```code
[ <expression> for <variable_name> in <sequence> if <condition>]
```

What it means:

```python
result = []
for variable_name in sequence:
    if condition:
        result.append(expression)
```

### Historical Digression

List comprehensions come from math (set-builder notation).

```code
a = [ x * x for x in s if x > 0 ] # Python

a = { x^2 | x ∈ s, x > 0 }         # Math
```

It is also implemented in several other languages. Most
coders probably aren't thinking about their math class though. So,
it's fine to view it as a cool list shortcut.

## Exercises

Start by running your `report.py` program so that you have the
portfolio of stocks loaded in the interactive mode.

```bash
bash % python3 -i report.py
```

Now, at the Python interactive prompt, type statements to perform the
operations described below.  These operations perform various kinds of
data reductions, transforms, and queries on the portfolio data.

### Exercise 2.19: List comprehensions

Try a few simple list comprehensions just to become familiar with the syntax.

```python
>>> nums = [1,2,3,4]
>>> squares = [ x * x for x in nums ]
>>> squares
[1, 4, 9, 16]
>>> twice = [ 2 * x for x in nums if x > 2 ]
>>> twice
[6, 8]
>>>
```

Notice how the list comprehensions are creating a new list with the
data suitably transformed or filtered.

### Exercise 2.20: Sequence Reductions

Compute the total cost of the portfolio using a single Python statement.

```python
>>> portfolio = read_portfolio('Data/portfolio.csv')
>>> cost = sum([ s['shares'] * s['price'] for s in portfolio ])
>>> cost
44671.15
>>>
```

After you have done that, show how you can compute the current value
of the portfolio using a single statement.

```python
>>> value = sum([ s['shares'] * prices[s['name']] for s in portfolio ])
>>> value
28686.1
>>>
```

Both of the above operations are an example of a map-reduction. The
list comprehension is mapping an operation across the list.

```python
>>> [ s['shares'] * s['price'] for s in portfolio ]
[3220.0000000000005, 4555.0, 12516.0, 10246.0, 3835.1499999999996, 3254.9999999999995, 7044.0]
>>>
```

The `sum()` function is then performing a reduction across the result:

```python
>>> sum(_)
44671.15
>>>
```

With this knowledge, you are now ready to go launch a big-data startup company.

### Exercise 2.21: Data Queries

Try the following examples of various data queries.

First, a list of all portfolio holdings with more than 100 shares.

```python
>>> more100 = [ s for s in portfolio if s['shares'] > 100 ]
>>> more100
[{'price': 83.44, 'name': 'CAT', 'shares': 150}, {'price': 51.23, 'name': 'MSFT', 'shares': 200}]
>>>
```

All portfolio holdings for MSFT and IBM stocks.

```python
>>> msftibm = [ s for s in portfolio if s['name'] in {'MSFT','IBM'} ]
>>> msftibm
[{'price': 91.1, 'name': 'IBM', 'shares': 50}, {'price': 51.23, 'name': 'MSFT', 'shares': 200},
  {'price': 65.1, 'name': 'MSFT', 'shares': 50}, {'price': 70.44, 'name': 'IBM', 'shares': 100}]
>>>
```

A list of all portfolio holdings that cost more than $10000.

```python
>>> cost10k = [ s for s in portfolio if s['shares'] * s['price'] > 10000 ]
>>> cost10k
[{'price': 83.44, 'name': 'CAT', 'shares': 150}, {'price': 51.23, 'name': 'MSFT', 'shares': 200}]
>>>
```

### Exercise 2.22: Data Extraction

Show how you could build a list of tuples `(name, shares)` where `name` and `shares` are taken from `portfolio`.

```python
>>> name_shares =[ (s['name'], s['shares']) for s in portfolio ]
>>> name_shares
[('AA', 100), ('IBM', 50), ('CAT', 150), ('MSFT', 200), ('GE', 95), ('MSFT', 50), ('IBM', 100)]
>>>
```

If you change the square brackets (`[`,`]`) to curly braces (`{`, `}`), you get something known as a set comprehension.
This gives you unique or distinct values.

For example, this determines the set of unique stock names that appear in `portfolio`:

```python
>>> names = { s['name'] for s in portfolio }
>>> names
{ 'AA', 'GE', 'IBM', 'MSFT', 'CAT' }
>>>
```

If you specify `key:value` pairs, you can build a dictionary.
For example, make a dictionary that maps the name of a stock to the total number of shares held.

```python
>>> holdings = { name: 0 for name in names }
>>> holdings
{'AA': 0, 'GE': 0, 'IBM': 0, 'MSFT': 0, 'CAT': 0}
>>>
```

This latter feature is known as a **dictionary comprehension**. Let’s tabulate:

```python
>>> for s in portfolio:
        holdings[s['name']] += s['shares']

>>> holdings
{ 'AA': 100, 'GE': 95, 'IBM': 150, 'MSFT':250, 'CAT': 150 }
>>>
```

Try this example that filters the `prices` dictionary down to only
those names that appear in the portfolio:

```python
>>> portfolio_prices = { name: prices[name] for name in names }
>>> portfolio_prices
{'AA': 9.22, 'GE': 13.48, 'IBM': 106.28, 'MSFT': 20.89, 'CAT': 35.46}
>>>
```

### Exercise 2.23: Extracting Data From CSV Files

Knowing how to use various combinations of list, set, and dictionary
comprehensions can be useful in various forms of data processing.
Here’s an example that shows how to extract selected columns from a
CSV file.

First, read a row of header information from a CSV file:

```python
>>> import csv
>>> f = open('Data/portfoliodate.csv')
>>> rows = csv.reader(f)
>>> headers = next(rows)
>>> headers
['name', 'date', 'time', 'shares', 'price']
>>>
```

Next, define a variable that lists the columns that you actually care about:

```python
>>> select = ['name', 'shares', 'price']
>>>
```

Now, locate the indices of the above columns in the source CSV file:

```python
>>> indices = [ headers.index(colname) for colname in select ]
>>> indices
[0, 3, 4]
>>>
```

Finally, read a row of data and turn it into a dictionary using a
dictionary comprehension:

```python
>>> row = next(rows)
>>> record = { colname: row[index] for colname, index in zip(select, indices) }   # dict-comprehension
>>> record
{'price': '32.20', 'name': 'AA', 'shares': '100'}
>>>
```

If you’re feeling comfortable with what just happened, read the rest
of the file:

```python
>>> portfolio = [ { colname: row[index] for colname, index in zip(select, indices) } for row in rows ]
>>> portfolio
[{'price': '91.10', 'name': 'IBM', 'shares': '50'}, {'price': '83.44', 'name': 'CAT', 'shares': '150'},
  {'price': '51.23', 'name': 'MSFT', 'shares': '200'}, {'price': '40.37', 'name': 'GE', 'shares': '95'},
  {'price': '65.10', 'name': 'MSFT', 'shares': '50'}, {'price': '70.44', 'name': 'IBM', 'shares': '100'}]
>>>
```

Oh my, you just reduced much of the `read_portfolio()` function to a single statement.

### Commentary

List comprehensions are commonly used in Python as an efficient means
for transforming, filtering, or collecting data.  Due to the syntax,
you don’t want to go overboard—try to keep each list comprehension as
simple as possible.  It’s okay to break things into multiple
steps. For example, it’s not clear that you would want to spring that
last example on your unsuspecting co-workers.

That said, knowing how to quickly manipulate data is a skill that’s
incredibly useful.  There are numerous situations where you might have
to solve some kind of one-off problem involving data imports, exports,
extraction, and so forth.  Becoming a guru master of list
comprehensions can substantially reduce the time spent devising a
solution.  Also, don't forget about the `collections` module.

[Contents](../Contents.md) \| [Previous (2.5 Collections)](05_Collections.md) \| [Next (2.7 Object Model)](07_Objects.md)
