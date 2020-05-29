[Contents](../Contents.md) \| [Previous (6.1 Iteration Protocol)](01_Iteration_protocol.md) \| [Next (6.3 Producer/Consumer)](03_Producers_consumers.md)

# 6.2 Customizing Iteration

This section looks at how you can customize iteration using a generator function.

### A problem

Suppose you wanted to create your own custom iteration pattern.

For example, a countdown.

```python
>>> for x in countdown(10):
...   print(x, end=' ')
...
10 9 8 7 6 5 4 3 2 1
>>>
```

There is an easy way to do this.

### Generators

A generator is a function that defines iteration.

```python
def countdown(n):
    while n > 0:
        yield n
        n -= 1
```

For example:

```python
>>> for x in countdown(10):
...   print(x, end=' ')
...
10 9 8 7 6 5 4 3 2 1
>>>
```

A generator is any function that uses the `yield` statement.

The behavior of generators is different than a normal function.
Calling a generator function creates a generator object. It does not
immediately execute the function.

```python
def countdown(n):
    # Added a print statement
    print('Counting down from', n)
    while n > 0:
        yield n
        n -= 1
```

```python
>>> x = countdown(10)
# There is NO PRINT STATEMENT
>>> x
# x is a generator object
<generator object at 0x58490>
>>>
```

The function only executes on `__next__()` call.

```python
>>> x = countdown(10)
>>> x
<generator object at 0x58490>
>>> x.__next__()
Counting down from 10
10
>>>
```

`yield` produces a value, but suspends the function execution.
The function resumes on next call to `__next__()`.

```python
>>> x.__next__()
9
>>> x.__next__()
8
```

When the generator finally returns, the iteration raises an error.

```python
>>> x.__next__()
1
>>> x.__next__()
Traceback (most recent call last):
File "<stdin>", line 1, in ? StopIteration
>>>
```

*Observation: A generator function implements the same low-level
 protocol that the for statements uses on lists, tuples, dicts, files,
 etc.*

## Exercises

### Exercise 6.4: A Simple Generator

If you ever find yourself wanting to customize iteration, you should
always think generator functions.  They're easy to write---make
a function that carries out the desired iteration logic and use `yield`
to emit values.

For example, try this generator that searches a file for lines containing
a matching substring:

```python
>>> def filematch(filename, substr):
        with open(filename, 'r') as f:
            for line in f:
                if substr in line:
                    yield line

>>> for line in open('Data/portfolio.csv'):
        print(line, end='')

name,shares,price
"AA",100,32.20
"IBM",50,91.10
"CAT",150,83.44
"MSFT",200,51.23
"GE",95,40.37
"MSFT",50,65.10
"IBM",100,70.44
>>> for line in filematch('Data/portfolio.csv', 'IBM'):
        print(line, end='')

"IBM",50,91.10
"IBM",100,70.44
>>>
```

This is kind of interesting--the idea that you can hide a bunch of
custom processing in a function and use it to feed a for-loop.
The next example looks at a more unusual case.

### Exercise 6.5: Monitoring a streaming data source

Generators can be an interesting way to monitor real-time data sources
such as log files or stock market feeds.  In this part, we'll
explore this idea.  To start, follow the next instructions carefully.

The program `Data/stocksim.py` is a program that
simulates stock market data.  As output, the program constantly writes
real-time data to a file `Data/stocklog.csv`.  In a
separate command window go into the `Data/` directory and run this program:

```bash
bash % python3 stocksim.py
```

If you are on Windows, just locate the `stocksim.py` program and
double-click on it to run it.  Now, forget about this program (just
let it run).  Using another window, look at the file
`Data/stocklog.csv` being written by the simulator.  You should see
new lines of text being added to the file every few seconds.  Again,
just let this program run in the background---it will run for several
hours (you shouldn't need to worry about it).

Once the above program is running, let's write a little program to
open the file, seek to the end, and watch for new output.  Create a
file `follow.py` and put this code in it:

```python
# follow.py
import os
import time

f = open('Data/stocklog.csv')
f.seek(0, os.SEEK_END)   # Move file pointer 0 bytes from end of file

while True:
    line = f.readline()
    if line == '':
        time.sleep(0.1)   # Sleep briefly and retry
        continue
    fields = line.split(',')
    name = fields[0].strip('"')
    price = float(fields[1])
    change = float(fields[4])
    if change < 0:
        print(f'{name:>10s} {price:>10.2f} {change:>10.2f}')
```

If you run the program, you'll see a real-time stock ticker.  Under the hood,
this code is kind of like the Unix `tail -f` command that's used to watch a log file.

Note: The use of the `readline()` method in this example is
somewhat unusual in that it is not the usual way of reading lines from
a file (normally you would just use a `for`-loop).  However, in
this case, we are using it to repeatedly probe the end of the file to
see if more data has been added (`readline()` will either
return new data or an empty string).

### Exercise 6.6: Using a generator to produce data

If you look at the code in Exercise 6.5, the first part of the code is producing
lines of data whereas the statements at the end of the `while` loop are consuming
the data.  A major feature of generator functions is that you can move all
of the data production code into a reusable function.

Modify the code in Exercise 6.5  so that the file-reading is performed by
a generator function `follow(filename)`.   Make it so the following code
works:

```python
>>> for line in follow('Data/stocklog.csv'):
          print(line, end='')

... Should see lines of output produced here ...
```

Modify the stock ticker code so that it looks like this:


```python
if __name__ == '__main__':
    for line in follow('Data/stocklog.csv'):
        fields = line.split(',')
        name = fields[0].strip('"')
        price = float(fields[1])
        change = float(fields[4])
        if change < 0:
            print(f'{name:>10s} {price:>10.2f} {change:>10.2f}')
```

### Exercise 6.7: Watching your portfolio

Modify the `follow.py` program so that it watches the stream of stock
data and prints a ticker showing information for only those stocks
in a portfolio.  For example:

```python
if __name__ == '__main__':
    import report

    portfolio = report.read_portfolio('Data/portfolio.csv')

    for line in follow('Data/stocklog.csv'):
        fields = line.split(',')
        name = fields[0].strip('"')
        price = float(fields[1])
        change = float(fields[4])
        if name in portfolio:
            print(f'{name:>10s} {price:>10.2f} {change:>10.2f}')
```

Note: For this to work, your `Portfolio` class must support the `in`
operator.  See [Exercise 6.3](01_Iteration_protocol) and make sure you
implement the `__contains__()` operator.

### Discussion

Something very powerful just happened here.  You moved an interesting iteration pattern
(reading lines at the end of a file) into its own little function.   The `follow()` function
is now this completely general purpose utility that you can use in any program.  For
example, you could use it to watch server logs, debugging logs, and other similar data sources.
That's kind of cool.

[Contents](../Contents.md) \| [Previous (6.1 Iteration Protocol)](01_Iteration_protocol.md) \| [Next (6.3 Producer/Consumer)](03_Producers_consumers.md)