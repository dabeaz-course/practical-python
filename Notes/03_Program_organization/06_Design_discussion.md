[Contents](../Contents.md) \| [Previous (3.5 Main module)](05_Main_module.md) \| [Next (4 Classes)](../04_Classes_objects/00_Overview.md)

# 3.6 Design Discussion

In this section we reconsider a design decision made earlier.

### Filenames versus Iterables

Compare these two programs that return the same output.

```python
# Provide a filename
def read_data(filename):
    records = []
    with open(filename) as f:
        for line in f:
            ...
            records.append(r)
    return records

d = read_data('file.csv')
```

```python
# Provide lines
def read_data(lines):
    records = []
    for line in lines:
        ...
        records.append(r)
    return records

with open('file.csv') as f:
    d = read_data(f)
```

* Which of these functions do you prefer? Why?
* Which of these functions is more flexible?

### Deep Idea: "Duck Typing"

[Duck Typing](https://en.wikipedia.org/wiki/Duck_typing) is a computer
programming concept to determine whether an object can be used for a
particular purpose.  It is an application of the [duck
test](https://en.wikipedia.org/wiki/Duck_test).

> If it looks like a duck, swims like a duck, and quacks like a duck, then it probably is a duck.

In the second version of `read_data()` above, the function expects any
iterable object. Not just the lines of a file.

```python
def read_data(lines):
    records = []
    for line in lines:
        ...
        records.append(r)
    return records
```

This means that we can use it with other *lines*.

```python
# A CSV file
lines = open('data.csv')
data = read_data(lines)

# A zipped file
lines = gzip.open('data.csv.gz','rt')
data = read_data(lines)

# The Standard Input
lines = sys.stdin
data = read_data(lines)

# A list of strings
lines = ['ACME,50,91.1','IBM,75,123.45', ... ]
data = read_data(lines)
```

There is considerable flexibility with this design.

*Question: Should we embrace or fight this flexibility?*

### Library Design Best Practices

Code libraries are often better served by embracing flexibility.
Don't restrict your options.  With great flexibility comes great power.

## Exercise

### Exercise 3.17: From filenames to file-like objects

You've now created a file `fileparse.py` that contained a
function `parse_csv()`.  The function worked like this:

```python
>>> import fileparse
>>> portfolio = fileparse.parse_csv('Data/portfolio.csv', types=[str,int,float])
>>>
```

Right now, the function expects to be passed a filename.  However, you
can make the code more flexible.  Modify the function so that it works
with any file-like/iterable object.  For example:

```
>>> import fileparse
>>> import gzip
>>> with gzip.open('Data/portfolio.csv.gz', 'rt') as file:
...      port = fileparse.parse_csv(file, types=[str,int,float])
...
>>> lines = ['name,shares,price', 'AA,100,34.23', 'IBM,50,91.1', 'HPE,75,45.1']
>>> port = fileparse.parse_csv(lines, types=[str,int,float])
>>>
```

In this new code, what happens if you pass a filename as before?

```
>>> port = fileparse.parse_csv('Data/portfolio.csv', types=[str,int,float])
>>> port
... look at output (it should be crazy) ...
>>>
```

Yes, you'll need to be careful.   Could you add a safety check to avoid this?

### Exercise 3.18: Fixing existing functions

Fix the `read_portfolio()` and `read_prices()` functions in the
`report.py` file so that they work with the modified version of
`parse_csv()`.  This should only involve a minor modification.
Afterwards, your `report.py` and `pcost.py` programs should work
the same way they always did.

[Contents](../Contents.md) \| [Previous (3.5 Main module)](05_Main_module.md) \| [Next (4 Classes)](../04_Classes_objects/00_Overview.md)