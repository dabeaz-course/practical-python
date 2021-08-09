[Contents](../Contents.md) \| [Previous (6.2 Customizing Iteration)](02_Customizing_iteration.md) \| [Next (6.4 Generator Expressions)](04_More_generators.md)

# 6.3 Producers, Consumers and Pipelines

Generators are a useful tool for setting various kinds of
producer/consumer problems and dataflow pipelines.  This section
discusses that.

### Producer-Consumer Problems

Generators are closely related to various forms of *producer-consumer* problems.

```python
# Producer
def follow(f):
    ...
    while True:
        ...
        yield line        # Produces value in `line` below
        ...

# Consumer
for line in follow(f):    # Consumes value from `yield` above
    ...
```

`yield` produces values that `for` consumes.

### Generator Pipelines

You can use this aspect of generators to set up processing pipelines (like Unix pipes).

*producer* &rarr; *processing* &rarr; *processing* &rarr; *consumer*

Processing pipes have an initial data producer, some set of intermediate processing stages and a final consumer.

**producer** &rarr; *processing* &rarr; *processing* &rarr; *consumer*

```python
def producer():
    ...
    yield item
    ...
```

The producer is typically a generator. Although it could also be a list of some other sequence.
`yield` feeds data into the pipeline.

*producer* &rarr; *processing* &rarr; *processing* &rarr; **consumer**

```python
def consumer(s):
    for item in s:
        ...
```

Consumer is a for-loop. It gets items and does something with them.

*producer* &rarr; **processing** &rarr; **processing** &rarr; *consumer*

```python
def processing(s):
    for item in s:
        ...
        yield newitem
        ...
```

Intermediate processing stages simultaneously consume and produce items.
They might modify the data stream.
They can also filter (discarding items).

*producer* &rarr; *processing* &rarr; *processing* &rarr; *consumer*

```python
def producer():
    ...
    yield item          # yields the item that is received by the `processing`
    ...

def processing(s):
    for item in s:      # Comes from the `producer`
        ...
        yield newitem   # yields a new item
        ...

def consumer(s):
    for item in s:      # Comes from the `processing`
        ...
```

Code to setup the pipeline

```python
a = producer()
b = processing(a)
c = consumer(b)
```

You will notice that data incrementally flows through the different functions.

## Exercises

For this exercise the `stocksim.py` program should still be running in the background.
You’re going to use the `follow()` function you wrote in the previous exercise.

### Exercise 6.8: Setting up a simple pipeline

Let's see the pipelining idea in action.  Write the following
function:

```python
>>> def filematch(lines, substr):
        for line in lines:
            if substr in line:
                yield line

>>>
```

This function is almost exactly the same as the first generator
example in the previous exercise except that it's no longer
opening a file--it merely operates on a sequence of lines given
to it as an argument.  Now, try this:

```
>>> from follow import follow
>>> lines = follow('Data/stocklog.csv')
>>> ibm = filematch(lines, 'IBM')
>>> for line in ibm:
        print(line)

... wait for output ...
```

It might take awhile for output to appear, but eventually you
should see some lines containing data for IBM.

### Exercise 6.9: Setting up a more complex pipeline

Take the pipelining idea a few steps further by performing
more actions.

```
>>> from follow import follow
>>> import csv
>>> lines = follow('Data/stocklog.csv')
>>> rows = csv.reader(lines)
>>> for row in rows:
        print(row)

['BA', '98.35', '6/11/2007', '09:41.07', '0.16', '98.25', '98.35', '98.31', '158148']
['AA', '39.63', '6/11/2007', '09:41.07', '-0.03', '39.67', '39.63', '39.31', '270224']
['XOM', '82.45', '6/11/2007', '09:41.07', '-0.23', '82.68', '82.64', '82.41', '748062']
['PG', '62.95', '6/11/2007', '09:41.08', '-0.12', '62.80', '62.97', '62.61', '454327']
...
```

Well, that's interesting.  What you're seeing here is that the output of the
`follow()` function has been piped into the `csv.reader()` function and we're
now getting a sequence of split rows.

### Exercise 6.10: Making more pipeline components

Let's extend the whole idea into a larger pipeline.  In a separate file `ticker.py`,
start by creating a function that reads a CSV file as you did above:

```python
# ticker.py

from follow import follow
import csv

def parse_stock_data(lines):
    rows = csv.reader(lines)
    return rows

if __name__ == '__main__':
    lines = follow('Data/stocklog.csv')
    rows = parse_stock_data(lines)
    for row in rows:
        print(row)
```

Write a new function that selects specific columns:

```
# ticker.py
...
def select_columns(rows, indices):
    for row in rows:
        yield [row[index] for index in indices]
...
def parse_stock_data(lines):
    rows = csv.reader(lines)
    rows = select_columns(rows, [0, 1, 4])
    return rows
```

Run your program again.  You should see output narrowed down like this:

```
['BA', '98.35', '0.16']
['AA', '39.63', '-0.03']
['XOM', '82.45','-0.23']
['PG', '62.95', '-0.12']
...
```

Write generator functions that convert data types and build dictionaries.
For example:

```python
# ticker.py
...

def convert_types(rows, types):
    for row in rows:
        yield [func(val) for func, val in zip(types, row)]

def make_dicts(rows, headers):
    for row in rows:
        yield dict(zip(headers, row))
...
def parse_stock_data(lines):
    rows = csv.reader(lines)
    rows = select_columns(rows, [0, 1, 4])
    rows = convert_types(rows, [str, float, float])
    rows = make_dicts(rows, ['name', 'price', 'change'])
    return rows
...
```

Run your program again.  You should now a stream of dictionaries like this:

```
{ 'name':'BA', 'price':98.35, 'change':0.16 }
{ 'name':'AA', 'price':39.63, 'change':-0.03 }
{ 'name':'XOM', 'price':82.45, 'change': -0.23 }
{ 'name':'PG', 'price':62.95, 'change':-0.12 }
...
```

### Exercise 6.11: Filtering data

Write a function that filters data.  For example:

```python
# ticker.py
...

def filter_symbols(rows, names):
    for row in rows:
        if row['name'] in names:
            yield row
```

Use this to filter stocks to just those in your portfolio:

```python
import report
portfolio = report.read_portfolio('Data/portfolio.csv')
rows = parse_stock_data(follow('Data/stocklog.csv'))
rows = filter_symbols(rows, portfolio)
for row in rows:
    print(row)
```

### Exercise 6.12: Putting it all together

In the `ticker.py` program, write a function `ticker(portfile, logfile, fmt)`
that creates a real-time stock ticker from a given portfolio, logfile,
and table format.  For example::

```python
>>> from ticker import ticker
>>> ticker('Data/portfolio.csv', 'Data/stocklog.csv', 'txt')
      Name      Price     Change
---------- ---------- ----------
        GE      37.14      -0.18
      MSFT      29.96      -0.09
       CAT      78.03      -0.49
        AA      39.34      -0.32
...

>>> ticker('Data/portfolio.csv', 'Data/stocklog.csv', 'csv')
Name,Price,Change
IBM,102.79,-0.28
CAT,78.04,-0.48
AA,39.35,-0.31
CAT,78.05,-0.47
...
```

### Discussion

Some lessons learned: You can create various generator functions and
chain them together to perform processing involving data-flow
pipelines.  In addition, you can create functions that package a
series of pipeline stages into a single function call (for example,
the `parse_stock_data()` function).

[Contents](../Contents.md) \| [Previous (6.2 Customizing Iteration)](02_Customizing_iteration.md) \| [Next (6.4 Generator Expressions)](04_More_generators.md)
