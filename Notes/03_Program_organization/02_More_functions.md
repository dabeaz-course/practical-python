[Contents](../Contents.md) \| [Previous (3.1 Scripting)](01_Script.md) \| [Next (3.3 Error Checking)](03_Error_checking.md)

# 3.2 More on Functions

Although functions were introduced earlier, very few details were provided on how
they actually work at a deeper level.  This section aims to fill in some gaps
and discuss matters such as calling conventions, scoping rules, and more.

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

Sometimes you want an argument to be optional.  If so, assign a default value
in the function definition.

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

In most cases, keyword arguments improve code clarity--especially for arguments that
serve as flags or which are related to optional features.

### Design Best Practices

Always give short, but meaningful names to functions arguments.

Someone using a function may want to use the keyword calling style.

```python
d = read_prices('prices.csv', debug=True)
```

Python development tools will show the names in help features and documentation.

### Returning Values

The `return` statement returns a value

```python
def square(x):
    return x * x
```

If no return value is given or `return` is missing, `None` is returned.

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

Functions can only return one value.  However, a function may return
multiple values by returning them in a tuple.

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
Variables defined outside are "global". Variables inside a function
are "local".

### Local Variables

Variables assigned inside functions are private.

```python
def read_portfolio(filename):
    portfolio = []
    for line in open(filename):
        fields = line.split(',')
        s = (fields[0], int(fields[1]), float(fields[2]))
        portfolio.append(s)
    return portfolio
```

In this example, `filename`, `portfolio`, `line`, `fields` and `s` are local variables.
Those variables are not retained or accessible after the function call.

```python
>>> stocks = read_portfolio('portfolio.csv')
>>> fields
Traceback (most recent call last):
File "<stdin>", line 1, in ?
NameError: name 'fields' is not defined
>>>
```

Locals also can't conflict with variables found elsewhere.

### Global Variables

Functions can freely access the values of globals defined in the same
file.

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

The global declaration must appear before its use and the corresponding
variable must exist in the same file as the function.   Having seen this,
know that it is considered poor form.  In fact, try to avoid `global` entirely
if you can.  If you need a function to modify some kind of state outside
of the function, it's better to use a class instead (more on this later).

### Argument Passing

When you call a function, the argument variables are names that refer
to the passed values. These values are NOT copies (see [section
2.7](../02_Working_with_data/07_Objects)). If mutable data types are
passed (e.g. lists, dicts), they can be modified *in-place*.

```python
def foo(items):
    items.append(42)    # Modifies the input object

a = [1, 2, 3]
foo(a)
print(a)                # [1, 2, 3, 42]
```

**Key point: Functions don't receive a copy of the input arguments.**

### Reassignment vs Modifying

Make sure you understand the subtle difference between modifying a
value and reassigning a variable name.

```python
def foo(items):
    items.append(42)    # Modifies the input object

a = [1, 2, 3]
foo(a)
print(a)                # [1, 2, 3, 42]

# VS
def bar(items):
    items = [4,5,6]    # Changes local `items` variable to point to a different object

b = [1, 2, 3]
bar(b)
print(b)                # [1, 2, 3]
```

*Reminder: Variable assignment never overwrites memory. The name is merely bound to a new value.*

## Exercises

This set of exercises have you implement what is, perhaps, the most
powerful and difficult part of the course.  There are a lot of steps
and many concepts from past exercises are put together all at once.
The final solution is only about 25 lines of code, but take your time
and make sure you understand each part.

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

Start this exercise by opening the file called
`Work/fileparse.py`. This is where we will be doing our work.

### Exercise 3.3: Reading CSV Files

To start, let’s just focus on the problem of reading a CSV file into a
list of dictionaries.  In the file `fileparse.py`, define a
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

```python
>>> portfolio = parse_csv('Data/portfolio.csv')
>>> portfolio
[{'price': '32.20', 'name': 'AA', 'shares': '100'}, {'price': '91.10', 'name': 'IBM', 'shares': '50'}, {'price': '83.44', 'name': 'CAT', 'shares': '150'}, {'price': '51.23', 'name': 'MSFT', 'shares': '200'}, {'price': '40.37', 'name': 'GE', 'shares': '95'}, {'price': '65.10', 'name': 'MSFT', 'shares': '50'}, {'price': '70.44', 'name': 'IBM', 'shares': '100'}]
>>>
```

This is good except that you can’t do any kind of useful calculation
with the data because everything is represented as a string.  We’ll
fix this shortly, but let’s keep building on it.

### Exercise 3.4: Building a Column Selector

In many cases, you’re only interested in selected columns from a CSV
file, not all of the data.  Modify the `parse_csv()` function so that
it optionally allows user-specified columns to be picked out as
follows:

```python
>>> # Read all of the data
>>> portfolio = parse_csv('Data/portfolio.csv')
>>> portfolio
[{'price': '32.20', 'name': 'AA', 'shares': '100'}, {'price': '91.10', 'name': 'IBM', 'shares': '50'}, {'price': '83.44', 'name': 'CAT', 'shares': '150'}, {'price': '51.23', 'name': 'MSFT', 'shares': '200'}, {'price': '40.37', 'name': 'GE', 'shares': '95'}, {'price': '65.10', 'name': 'MSFT', 'shares': '50'}, {'price': '70.44', 'name': 'IBM', 'shares': '100'}]

>>> # Read only some of the data
>>> shares_held = parse_csv('Data/portfolio.csv', select=['name','shares'])
>>> shares_held
[{'name': 'AA', 'shares': '100'}, {'name': 'IBM', 'shares': '50'}, {'name': 'CAT', 'shares': '150'}, {'name': 'MSFT', 'shares': '200'}, {'name': 'GE', 'shares': '95'}, {'name': 'MSFT', 'shares': '50'}, {'name': 'IBM', 'shares': '100'}]
>>>
```

An example of a column selector was given in [Exercise 2.23](../02_Working_with_data/06_List_comprehension).
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

There are a number of tricky bits to this part. Probably the most
important one is the mapping of the column selections to row indices.
For example, suppose the input file had the following headers:

```python
>>> headers = ['name', 'date', 'time', 'shares', 'price']
>>>
```

Now, suppose the selected columns were as follows:

```python
>>> select = ['name', 'shares']
>>>
```

To perform the proper selection, you have to map the selected column names to column indices in the file.
That’s what this step is doing:

```python
>>> indices = [headers.index(colname) for colname in select ]
>>> indices
[0, 3]
>>>
```

In other words, "name" is column 0 and "shares" is column 3.
When you read a row of data from the file, the indices are used to filter it:

```python
>>> row = ['AA', '6/11/2007', '9:50am', '100', '32.20' ]
>>> row = [ row[index] for index in indices ]
>>> row
['AA', '100']
>>>
```

### Exercise 3.5: Performing Type Conversion

Modify the `parse_csv()` function so that it optionally allows
type-conversions to be applied to the returned data.  For example:

```python
>>> portfolio = parse_csv('Data/portfolio.csv', types=[str, int, float])
>>> portfolio
[{'price': 32.2, 'name': 'AA', 'shares': 100}, {'price': 91.1, 'name': 'IBM', 'shares': 50}, {'price': 83.44, 'name': 'CAT', 'shares': 150}, {'price': 51.23, 'name': 'MSFT', 'shares': 200}, {'price': 40.37, 'name': 'GE', 'shares': 95}, {'price': 65.1, 'name': 'MSFT', 'shares': 50}, {'price': 70.44, 'name': 'IBM', 'shares': 100}]

>>> shares_held = parse_csv('Data/portfolio.csv', select=['name', 'shares'], types=[str, int])
>>> shares_held
[{'name': 'AA', 'shares': 100}, {'name': 'IBM', 'shares': 50}, {'name': 'CAT', 'shares': 150}, {'name': 'MSFT', 'shares': 200}, {'name': 'GE', 'shares': 95}, {'name': 'MSFT', 'shares': 50}, {'name': 'IBM', 'shares': 100}]
>>>
```

You already explored this in [Exercise 2.24](../02_Working_with_data/07_Objects).
You'll need to insert the following fragment of code into your solution:

```python
...
if types:
    row = [func(val) for func, val in zip(types, row) ]
...
```

### Exercise 3.6: Working without Headers

Some CSV files don’t include any header information.
For example, the file `prices.csv` looks like this:

```csv
"AA",9.22
"AXP",24.85
"BA",44.85
"BAC",11.27
...
```

Modify the `parse_csv()` function so that it can work with such files
by creating a list of tuples instead.  For example:

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

### Exercise 3.7: Picking a different column delimitier

Although CSV files are pretty common, it’s also possible that you
could encounter a file that uses a different column separator such as
a tab or space.  For example, the file `Data/portfolio.dat` looks like
this:

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

The `csv.reader()` function allows a different column delimiter to be given as follows:

```python
rows = csv.reader(f, delimiter=' ')
```

Modify your `parse_csv()` function so that it also allows the
delimiter to be changed.

For example:

```python
>>> portfolio = parse_csv('Data/portfolio.dat', types=[str, int, float], delimiter=' ')
>>> portfolio
[{'price': '32.20', 'name': 'AA', 'shares': '100'}, {'price': '91.10', 'name': 'IBM', 'shares': '50'}, {'price': '83.44', 'name': 'CAT', 'shares': '150'}, {'price': '51.23', 'name': 'MSFT', 'shares': '200'}, {'price': '40.37', 'name': 'GE', 'shares': '95'}, {'price': '65.10', 'name': 'MSFT', 'shares': '50'}, {'price': '70.44', 'name': 'IBM', 'shares': '100'}]
>>>
```

### Commentary

If you’ve made it this far, you’ve created a nice library function
that’s genuinely useful.  You can use it to parse arbitrary CSV files,
select out columns of interest, perform type conversions, without
having to worry too much about the inner workings of files or the
`csv` module.

[Contents](../Contents.md) \| [Previous (3.1 Scripting)](01_Script.md) \| [Next (3.3 Error Checking)](03_Error_checking.md)
