[Contents](../Contents.md) \| [Previous (2.3 Formatting)](03_Formatting.md) \| [Next (2.5 Collections)](05_Collections.md)

# 2.4 Sequences

### Sequence Datatypes

Python has three *sequence* datatypes.

* String: `'Hello'`. A string is a sequence of characters.
* List: `[1, 4, 5]`.
* Tuple: `('GOOG', 100, 490.1)`.

All sequences are ordered, indexed by integers, and have a length.

```python
a = 'Hello'               # String
b = [1, 4, 5]             # List
c = ('GOOG', 100, 490.1)  # Tuple

# Indexed order
a[0]                      # 'H'
b[-1]                     # 5
c[1]                      # 100

# Length of sequence
len(a)                    # 5
len(b)                    # 3
len(c)                    # 3
```

Sequences can be replicated: `s * n`.

```python
>>> a = 'Hello'
>>> a * 3
'HelloHelloHello'
>>> b = [1, 2, 3]
>>> b * 2
[1, 2, 3, 1, 2, 3]
>>>
```

Sequences of the same type can be concatenated: `s + t`.

```python
>>> a = (1, 2, 3)
>>> b = (4, 5)
>>> a + b
(1, 2, 3, 4, 5)
>>>
>>> c = [1, 5]
>>> a + c
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can only concatenate tuple (not "list") to tuple
```

### Slicing

Slicing means to take a subsequence from a sequence.
The syntax is `s[start:end]`. Where `start` and `end` are the indexes of the subsequence you want.

```python
a = [0,1,2,3,4,5,6,7,8]

a[2:5]    # [2,3,4]
a[-5:]    # [4,5,6,7,8]
a[:3]     # [0,1,2]
```

* Indices `start` and `end` must be integers.
* Slices do *not* include the end value. It is like a half-open interval from math.
* If indices are omitted, they default to the beginning or end of the list.

### Slice re-assignment

On lists, slices can be reassigned and deleted.

```python
# Reassignment
a = [0,1,2,3,4,5,6,7,8]
a[2:4] = [10,11,12]       # [0,1,10,11,12,4,5,6,7,8]
```

*Note: The reassigned slice doesn't need to have the same length.*

```python
# Deletion
a = [0,1,2,3,4,5,6,7,8]
del a[2:4]                # [0,1,4,5,6,7,8]
```

### Sequence Reductions

There are some common functions to reduce a sequence to a single value.

```python
>>> s = [1, 2, 3, 4]
>>> sum(s)
10
>>> min(s)
1
>>> max(s)
4
>>> t = ['Hello', 'World']
>>> max(t)
'World'
>>>
```

### Iteration over a sequence

The for-loop iterates over the elements in a sequence.

```python
>>> s = [1, 4, 9, 16]
>>> for i in s:
...     print(i)
...
1
4
9
16
>>>
```

On each iteration of the loop, you get a new item to work with.
This new value is placed into the iteration variable. In this example, the
iteration variable is `x`:

```python
for x in s:         # `x` is an iteration variable
    ...statements
```

On each iteration, the previous value of the iteration variable is overwritten (if any).
After the loop finishes, the variable retains the last value.

### break statement

You can use the `break` statement to break out of a loop early.

```python
for name in namelist:
    if name == 'Jake':
        break
    ...
    ...
statements
```

When the `break` statement executes, it exits the loop and moves
on the next `statements`.  The `break` statement only applies to the
inner-most loop. If this loop is within another loop, it will not
break the outer loop.

### continue statement

To skip one element and move to the next one, use the `continue` statement.

```python
for line in lines:
    if line == '\n':    # Skip blank lines
        continue
    # More statements
    ...
```

This is useful when the current item is not of interest or needs to be ignored in the processing.

### Looping over integers

If you need to count, use `range()`.

```python
for i in range(100):
    # i = 0,1,...,99
```

The syntax is `range([start,] end [,step])`

```python
for i in range(100):
    # i = 0,1,...,99
for j in range(10,20):
    # j = 10,11,..., 19
for k in range(10,50,2):
    # k = 10,12,...,48
    # Notice how it counts in steps of 2, not 1.
```

* The ending value is never included. It mirrors the behavior of slices.
* `start` is optional. Default `0`.
* `step` is optional. Default `1`.
* `range()` computes values as needed. It does not actually store a large range of numbers.

### enumerate() function

The `enumerate` function adds an extra counter value to iteration.

```python
names = ['Elwood', 'Jake', 'Curtis']
for i, name in enumerate(names):
    # Loops with i = 0, name = 'Elwood'
    # i = 1, name = 'Jake'
    # i = 2, name = 'Curtis'
```

The general form is `enumerate(sequence [, start = 0])`. `start` is optional.
A good example of using `enumerate()` is tracking line numbers while reading a file:

```python
with open(filename) as f:
    for lineno, line in enumerate(f, start=1):
        ...
```

In the end, `enumerate` is just a nice shortcut for:

```python
i = 0
for x in s:
    statements
    i += 1
```

Using `enumerate` is less typing and runs slightly faster.

### For and tuples

You can iterate with multiple iteration variables.

```python
points = [
  (1, 4),(10, 40),(23, 14),(5, 6),(7, 8)
]
for x, y in points:
    # Loops with x = 1, y = 4
    #            x = 10, y = 40
    #            x = 23, y = 14
    #            ...
```

When using multiple variables, each tuple is *unpacked* into a set of iteration variables.
The number of variables must match the number of items in each tuple.

### zip() function

The `zip` function takes multiple sequences and makes an iterator that combines them.

```python
columns = ['name', 'shares', 'price']
values = ['GOOG', 100, 490.1 ]
pairs = zip(columns, values)
# ('name','GOOG'), ('shares',100), ('price',490.1)
```

To get the result you must iterate. You can use multiple variables to unpack the tuples as shown earlier.

```python
for column, value in pairs:
    ...
```

A common use of `zip` is to create key/value pairs for constructing dictionaries.

```python
d = dict(zip(columns, values))
```

## Exercises

### Exercise 2.13: Counting

Try some basic counting examples:

```python
>>> for n in range(10):            # Count 0 ... 9
        print(n, end=' ')

0 1 2 3 4 5 6 7 8 9
>>> for n in range(10,0,-1):       # Count 10 ... 1
        print(n, end=' ')

10 9 8 7 6 5 4 3 2 1
>>> for n in range(0,10,2):        # Count 0, 2, ... 8
        print(n, end=' ')

0 2 4 6 8
>>>
```

### Exercise 2.14: More sequence operations

Interactively experiment with some of the sequence reduction operations.

```python
>>> data = [4, 9, 1, 25, 16, 100, 49]
>>> min(data)
1
>>> max(data)
100
>>> sum(data)
204
>>>
```

Try looping over the data.

```python
>>> for x in data:
        print(x)

4
9
...
>>> for n, x in enumerate(data):
        print(n, x)

0 4
1 9
2 1
...
>>>
```

Sometimes the `for` statement, `len()`, and `range()` get used by
novices in some kind of horrible code fragment that looks like it
emerged from the depths of a rusty C program.

```python
>>> for n in range(len(data)):
        print(data[n])

4
9
1
...
>>>
```

Don’t do that! Not only does reading it make everyone’s eyes bleed,
it’s inefficient with memory and it runs a lot slower.  Just use a
normal `for` loop if you want to iterate over data.  Use `enumerate()`
if you happen to need the index for some reason.

### Exercise 2.15: A practical enumerate() example

Recall that the file `Data/missing.csv` contains data for a stock
portfolio, but has some rows with missing data.  Using `enumerate()`,
modify your `pcost.py` program so that it prints a line number with
the warning message when it encounters bad input.

```python
>>> cost = portfolio_cost('Data/missing.csv')
Row 4: Couldn't convert: ['MSFT', '', '51.23']
Row 7: Couldn't convert: ['IBM', '', '70.44']
>>>
```

To do this, you’ll need to change a few parts of your code.

```python
...
for rowno, row in enumerate(rows, start=1):
    try:
        ...
    except ValueError:
        print(f'Row {rowno}: Bad row: {row}')
```

### Exercise 2.16: Using the zip() function

In the file `Data/portfolio.csv`, the first line contains column
headers. In all previous code, we’ve been discarding them.

```python
>>> f = open('Data/portfolio.csv')
>>> rows = csv.reader(f)
>>> headers = next(rows)
>>> headers
['name', 'shares', 'price']
>>>
```

However, what if you could use the headers for something useful? This
is where the `zip()` function enters the picture.  First try this to
pair the file headers with a row of data:

```python
>>> row = next(rows)
>>> row
['AA', '100', '32.20']
>>> list(zip(headers, row))
[ ('name', 'AA'), ('shares', '100'), ('price', '32.20') ]
>>>
```

Notice how `zip()` paired the column headers with the column values.
We’ve used `list()` here to turn the result into a list so that you
can see it. Normally, `zip()` creates an iterator that must be
consumed by a for-loop.

This pairing is an intermediate step to building a
dictionary. Now try this:

```python
>>> record = dict(zip(headers, row))
>>> record
{'price': '32.20', 'name': 'AA', 'shares': '100'}
>>>
```

This transformation is one of the most useful tricks to know about
when processing a lot of data files.  For example, suppose you wanted
to make the `pcost.py` program work with various input files, but
without regard for the actual column number where the name, shares,
and price appear.

Modify the `portfolio_cost()` function in `pcost.py` so that it looks like this:

```python
# pcost.py

def portfolio_cost(filename):
    ...
        for rowno, row in enumerate(rows, start=1):
            record = dict(zip(headers, row))
            try:
                nshares = int(record['shares'])
                price = float(record['price'])
                total_cost += nshares * price
            # This catches errors in int() and float() conversions above
            except ValueError:
                print(f'Row {rowno}: Bad row: {row}')
        ...
```

Now, try your function on a completely different data file
`Data/portfoliodate.csv` which looks like this:

```csv
name,date,time,shares,price
"AA","6/11/2007","9:50am",100,32.20
"IBM","5/13/2007","4:20pm",50,91.10
"CAT","9/23/2006","1:30pm",150,83.44
"MSFT","5/17/2007","10:30am",200,51.23
"GE","2/1/2006","10:45am",95,40.37
"MSFT","10/31/2006","12:05pm",50,65.10
"IBM","7/9/2006","3:15pm",100,70.44
```

```python
>>> portfolio_cost('Data/portfoliodate.csv')
44671.15
>>>
```

If you did it right, you’ll find that your program still works even
though the data file has a completely different column format than
before. That’s cool!

The change made here is subtle, but significant.  Instead of
`portfolio_cost()` being hardcoded to read a single fixed file format,
the new version reads any CSV file and picks the values of interest
out of it.  As long as the file has the required columns, the code will work.

Modify the `report.py` program you wrote in Section 2.3 so that it uses
the same technique to pick out column headers.

Try running the `report.py` program on the `Data/portfoliodate.csv`
file and see that it produces the same answer as before.

### Exercise 2.17: Inverting a dictionary

A dictionary maps keys to values. For example, a dictionary of stock prices.

```python
>>> prices = {
        'GOOG' : 490.1,
        'AA' : 23.45,
        'IBM' : 91.1,
        'MSFT' : 34.23
    }
>>>
```

If you use the `items()` method, you can get `(key,value)` pairs:

```python
>>> prices.items()
dict_items([('GOOG', 490.1), ('AA', 23.45), ('IBM', 91.1), ('MSFT', 34.23)])
>>>
```

However, what if you wanted to get a list of `(value, key)` pairs instead?
*Hint: use `zip()`.*

```python
>>> pricelist = list(zip(prices.values(),prices.keys()))
>>> pricelist
[(490.1, 'GOOG'), (23.45, 'AA'), (91.1, 'IBM'), (34.23, 'MSFT')]
>>>
```

Why would you do this? For one, it allows you to perform certain kinds
of data processing on the dictionary data.

```python
>>> min(pricelist)
(23.45, 'AA')
>>> max(pricelist)
(490.1, 'GOOG')
>>> sorted(pricelist)
[(23.45, 'AA'), (34.23, 'MSFT'), (91.1, 'IBM'), (490.1, 'GOOG')]
>>>
```

This also illustrates an important feature of tuples. When used in
comparisons, tuples are compared element-by-element starting with the
first item. Similar to how strings are compared
character-by-character.

`zip()` is often used in situations like this where you need to pair
up data from different places.  For example, pairing up the column
names with column values in order to make a dictionary of named
values.

Note that `zip()` is not limited to pairs. For example, you can use it
with any number of input lists:

```python
>>> a = [1, 2, 3, 4]
>>> b = ['w', 'x', 'y', 'z']
>>> c = [0.2, 0.4, 0.6, 0.8]
>>> list(zip(a, b, c))
[(1, 'w', 0.2), (2, 'x', 0.4), (3, 'y', 0.6), (4, 'z', 0.8))]
>>>
```

Also, be aware that `zip()` stops once the shortest input sequence is exhausted.

```python
>>> a = [1, 2, 3, 4, 5, 6]
>>> b = ['x', 'y', 'z']
>>> list(zip(a,b))
[(1, 'x'), (2, 'y'), (3, 'z')]
>>>
```

[Contents](../Contents.md) \| [Previous (2.3 Formatting)](03_Formatting.md) \| [Next (2.5 Collections)](05_Collections.md)
