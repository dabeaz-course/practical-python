# 3.2 More on Functions

This section fills in a few more details about how functions work and are defined.

### Calling a Function

Consider this function:

```python
def read_prices(filename, debug):
    ...
```

You can call the function with positional arguments:

```
prices = read_prices('prices.csv', True)
```

Or you can call the function with keyword arguments:

```python
prices = read_prices(filename='prices.csv', debug=True)
```

### Default Arguments

Sometimes you want an optional argument.

```python
def read_prices(filename, debug=False):
    ...
```

If a default value is assigned, the argument is optional in function calls.

```python
d = read_prices('prices.csv')
e = read_prices('prices.dat', True)
```

*Note: Arguments with defaults must appear at the end of the arguments list (all non-optional arguments go first).*

### Prefer keyword arguments for optional arguments

Compare and contrast these two different calling styles:

```python
parse_data(data, False, True) # ?????

parse_data(data, ignore_errors=True)
parse_data(data, debug=True)
parse_data(data, debug=True, ignore_errors=True)
```

Keyword arguments improve code clarity.

### Design Best Practices

Always give short, but meaningful names to functions arguments.

Someone using a function may want to use the keyword calling style.

```python
d = read_prices('prices.csv', debug=True)
```

Python development tools will show the names in help features and documentation.

### Return Values

The `return` statement returns a value

```python
def square(x):
    return x * x
```

If no return value or `return` not specified, `None` is returned.

```python
def bar(x):
    statements
    return

a = bar(4)      # a = None

# OR
def foo(x):
    statements  # No `return`

b = foo(4)      # b = None
```

### Multiple Return Values

Functions can only return one value.
However, a function may return multiple values by returning a tuple.

```python
def divide(a,b):
    q = a // b      # Quotient
    r = a % b       # Remainder
    return q, r     # Return a tuple
```

Usage example:

```python
x, y = divide(37,5) # x = 7, y = 2

x = divide(37, 5)   # x = (7, 2)
```

### Variable Scope

Programs assign values to variables.

```python
x = value # Global variable

def foo():
    y = value # Local variable
```

Variables assignments occur outside and inside function definitions.
Variables defined outside are "global". Variables inside a function are "local".

### Local Variables

Variables inside functions are private.

```python
def read_portfolio(filename):
    portfolio = []
    for line in open(filename):
        fields = line.split()
        s = (fields[0],int(fields[1]),float(fields[2]))
        portfolio.append(s)
    return portfolio
```

In this example, `filename`, `portfolio`, `line`, `fields` and `s` are local variables.
Those variables are not retained or accessible after the function call.

```pycon
>>> stocks = read_portfolio('stocks.dat')
>>> fields
Traceback (most recent call last):
File "<stdin>", line 1, in ?
NameError: name 'fields' is not defined
>>>
```

They also can't conflict with variables found elsewhere.

### Global Variables

Functions can freely access the values of globals.

```python
name = 'Dave'

def greeting():
    print('Hello', name)  # Using `name` global variable
```

However, functions can't modify globals:

```python
name = 'Dave'

def spam():
  name = 'Guido'

spam()
print(name) # prints 'Dave'
```

**Remember: All assignments in functions are local.**

### Modifying Globals

If you must modify a global variable you must declare it as such.

```python
name = 'Dave'
def spam():
    global name
    name = 'Guido' # Changes the global name above
```

The global declaration must appear before its use.   Having seen this,
know that it is considered poor form.  In fact, try to avoid entirely
if you can.  If you need a function to modify some kind of state outside
of the function, it's better to use a class instead (more on this later).

### Argument Passing

When you call a function, the argument variables are names for passed values.
If mutable data types are passed (e.g. lists, dicts), they can be modified *in-place*.

```python
def foo(items):
    items.append(42)    # Modifies the input object

a = [1, 2, 3]
foo(a)
print(a)                # [1, 2, 3, 42]
```

**Key point: Functions don't receive a copy of the input arguments.**

### Reassignment vs Modifying

Make sure you understand the subtle difference between modifying a value and reassigning a variable name.

```python
def foo(items):
    items.append(42)    # Modifies the input object

a = [1, 2, 3]
foo(a)
print(a)                # [1, 2, 3, 42]

# VS
def bar(items):
    items = [4,5,6]    # Reassigns `items` variable

b = [1, 2, 3]
bar(b)
print(b)                # [1, 2, 3]
```

*Reminder: Variable assignment never overwrites memory. The name is simply bound to a new value.*

## Exercises

This exercise involves a lot of steps and putting concepts together from past exercises. 
The final solution is only about 25 lines of code, but take your time and make sure you understand each part.

A central part of your `report.py` program focuses on the reading of
CSV files.  For example, the function `read_portfolio()` reads a file
containing rows of portfolio data and the function `read_prices()`
reads a file containing rows of price data. In both of those
functions, there are a lot of low-level "fiddly" bits and similar
features.  For example, they both open a file and wrap it with the
`csv` module and they both convert various fields into new types.

If you were doing a lot of file parsing for real, you’d probably want
to clean some of this up and make it more general purpose.  That's
our goal.

Start this exercise by creating a new file called `fileparse.py`. This is where we will be doing our work.

### (a) Reading CSV Files

To start, let’s just focus on the problem of reading a CSV file into a
list of dictionaries.  In the file `fileparse.py`, define a simple
function that looks like this:

```python
# fileparse.py
import csv

def parse_csv(filename):
    '''
    Parse a CSV file into a list of records
    '''
    with open(filename) as f:
        rows = csv.reader(f)

        # Read the file headers
        headers = next(rows)
        records = []
        for row in rows:
            if not row:    # Skip rows with no data
                continue
            record = dict(zip(headers, row))
            records.append(record)

    return records
```

This function reads a CSV file into a list of dictionaries while
hiding the details of opening the file, wrapping it with the `csv`
module, ignoring blank lines, and so forth.

Try it out:

Hint: `python3 -i fileparse.py`.

```pycon
>>> portfolio = parse_csv('Data/portfolio.csv')
>>> portfolio
[{'price': '32.20', 'name': 'AA', 'shares': '100'}, {'price': '91.10', 'name': 'IBM', 'shares': '50'}, {'price': '83.44', 'name': 'CAT', 'shares': '150'}, {'price': '51.23', 'name': 'MSFT', 'shares': '200'}, {'price': '40.37', 'name': 'GE', 'shares': '95'}, {'price': '65.10', 'name': 'MSFT', 'shares': '50'}, {'price': '70.44', 'name': 'IBM', 'shares': '100'}]
>>>
```

This is great except that you can’t do any kind of useful calculation with the data because everything is represented as a string.
We’ll fix this shortly, but let’s keep building on it.

### (b) Building a Column Selector

In many cases, you’re only interested in selected columns from a CSV file, not all of the data.
Modify the `parse_csv()` function so that it optionally allows user-specified columns to be picked out as follows:

```python
>>> # Read all of the data
>>> portfolio = parse_csv('Data/portfolio.csv')
>>> portfolio
[{'price': '32.20', 'name': 'AA', 'shares': '100'}, {'price': '91.10', 'name': 'IBM', 'shares': '50'}, {'price': '83.44', 'name': 'CAT', 'shares': '150'}, {'price': '51.23', 'name': 'MSFT', 'shares': '200'}, {'price': '40.37', 'name': 'GE', 'shares': '95'}, {'price': '65.10', 'name': 'MSFT', 'shares': '50'}, {'price': '70.44', 'name': 'IBM', 'shares': '100'}]

>>> # Read some of the data
>>> shares_held = parse_csv('portfolio.csv', select=['name','shares'])
>>> shares_held
[{'name': 'AA', 'shares': '100'}, {'name': 'IBM', 'shares': '50'}, {'name': 'CAT', 'shares': '150'}, {'name': 'MSFT', 'shares': '200'}, {'name': 'GE', 'shares': '95'}, {'name': 'MSFT', 'shares': '50'}, {'name': 'IBM', 'shares': '100'}]
>>>
```

An example of a column selector was given in Section 2.5.
However, here’s one way to do it:

```python
# fileparse.py
import csv

def parse_csv(filename, select=None):
    '''
    Parse a CSV file into a list of records
    '''
    with open(filename) as f:
        rows = csv.reader(f)

        # Read the file headers
        headers = next(rows)

        # If a column selector was given, find indices of the specified columns.
        # Also narrow the set of headers used for resulting dictionaries
        if select:
            indices = [headers.index(colname) for colname in select]
            headers = select
        else:
            indices = []

        records = []
        for row in rows:
            if not row:    # Skip rows with no data
                continue
            # Filter the row if specific columns were selected
            if indices:
                row = [ row[index] for index in indices ]

            # Make a dictionary
            record = dict(zip(headers, row))
            records.append(record)

    return records
```

There are a number of tricky bits to this part. Probably the most important one is the mapping of the column selections to row indices.
For example, suppose the input file had the following headers:

```pycon
>>> headers = ['name', 'date', 'time', 'shares', 'price']
>>>
```

Now, suppose the selected columns were as follows:

```pycon
>>> select = ['name', 'shares']
>>>
```

To perform the proper selection, you have to map the selected column names to column indices in the file.
That’s what this step is doing:

```pycon
>>> indices = [headers.index(colname) for colname in select ]
>>> indices
[0, 3]
>>>
```

In other words, "name" is column 0 and "shares" is column 3.
When you read a row of data from the file, the indices are used to filter it:

```pycon
>>> row = ['AA', '6/11/2007', '9:50am', '100', '32.20' ]
>>> row = [ row[index] for index in indices ]
>>> row
['AA', '100']
>>>
```

### (c) Performing Type Conversion

Modify the `parse_csv()` function so that it optionally allows type-conversions to be applied to the returned data.
For example:

```pycon
>>> portfolio = parse_csv('Data/portfolio.csv', types=[str, int, float])
>>> portfolio
[{'price': 32.2, 'name': 'AA', 'shares': 100}, {'price': 91.1, 'name': 'IBM', 'shares': 50}, {'price': 83.44, 'name': 'CAT', 'shares': 150}, {'price': 51.23, 'name': 'MSFT', 'shares': 200}, {'price': 40.37, 'name': 'GE', 'shares': 95}, {'price': 65.1, 'name': 'MSFT', 'shares': 50}, {'price': 70.44, 'name': 'IBM', 'shares': 100}]

>>> shares_held = parse_csv('Data/portfolio.csv', select=['name', 'shares'], types=[str, int])
>>> shares_held
[{'name': 'AA', 'shares': 100}, {'name': 'IBM', 'shares': 50}, {'name': 'CAT', 'shares': 150}, {'name': 'MSFT', 'shares': 200}, {'name': 'GE', 'shares': 95}, {'name': 'MSFT', 'shares': 50}, {'name': 'IBM', 'shares': 100}]
>>>
```

You already explored this in Exercise 2.7.  You'll need to insert the
following fragment of code into your solution:

```python
...
if types:
    row = [func(val) for func, val in zip(types, row) ]
...
```

### (d) Working with Headers

Some CSV files don’t include any header information.
For example, the file `prices.csv` looks like this:

```csv
"AA",9.22
"AXP",24.85
"BA",44.85
"BAC",11.27
...
```

Modify the `parse_csv()` function so that it can work with such files by creating a list of tuples instead.
For example:

```python
>>> prices = parse_csv('Data/prices.csv', types=[str,float], has_headers=False)
>>> prices
[('AA', 9.22), ('AXP', 24.85), ('BA', 44.85), ('BAC', 11.27), ('C', 3.72), ('CAT', 35.46), ('CVX', 66.67), ('DD', 28.47), ('DIS', 24.22), ('GE', 13.48), ('GM', 0.75), ('HD', 23.16), ('HPQ', 34.35), ('IBM', 106.28), ('INTC', 15.72), ('JNJ', 55.16), ('JPM', 36.9), ('KFT', 26.11), ('KO', 49.16), ('MCD', 58.99), ('MMM', 57.1), ('MRK', 27.58), ('MSFT', 20.89), ('PFE', 15.19), ('PG', 51.94), ('T', 24.79), ('UTX', 52.61), ('VZ', 29.26), ('WMT', 49.74), ('XOM', 69.35)]
>>>
```

To make this change, you’ll need to modify the code so that the first
line of data isn’t interpreted as a header line.  Also, you’ll need to
make sure you don’t create dictionaries as there are no longer any
column names to use for keys.

### (e) Picking a different column delimitier

Although CSV files are pretty common, it’s also possible that you could encounter a file that uses a different column separator such as a tab or space.
For example, the file `Data/portfolio.dat` looks like this:

```csv
name shares price
"AA" 100 32.20
"IBM" 50 91.10
"CAT" 150 83.44
"MSFT" 200 51.23
"GE" 95 40.37
"MSFT" 50 65.10
"IBM" 100 70.44
```

The `csv.reader()` function allows a different delimiter to be given as follows:

```python
rows = csv.reader(f, delimiter=' ')
```

Modify your `parse_csv()` function so that it also allows the delimiter to be changed. 

For example:

```pycon
>>> portfolio = parse_csv('Data/portfolio.dat', types=[str, int, float], delimiter=' ')
>>> portfolio
[{'price': '32.20', 'name': 'AA', 'shares': '100'}, {'price': '91.10', 'name': 'IBM', 'shares': '50'}, {'price': '83.44', 'name': 'CAT', 'shares': '150'}, {'price': '51.23', 'name': 'MSFT', 'shares': '200'}, {'price': '40.37', 'name': 'GE', 'shares': '95'}, {'price': '65.10', 'name': 'MSFT', 'shares': '50'}, {'price': '70.44', 'name': 'IBM', 'shares': '100'}]
>>>
```

If you’ve made it this far, you’ve created a nice library function that’s genuinely useful.
You can use it to parse arbitrary CSV files, select out columns of
interest, perform type conversions, without having to worry too much
about the inner workings of files or the `csv` module.

Nice!

[Next](03_Error_checking)