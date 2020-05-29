[Contents](../Contents.md) \| [Previous (6.3 Producer/Consumer)](03_Producers_consumers.md) \| [Next (7 Advanced Topics)](../07_Advanced_Topics/00_Overview.md)

# 6.4 More Generators

This section introduces a few additional generator related topics
including generator expressions and the itertools module.

### Generator Expressions

A generator version of a list comprehension.

```python
>>> a = [1,2,3,4]
>>> b = (2*x for x in a)
>>> b
<generator object at 0x58760>
>>> for i in b:
...   print(i, end=' ')
...
2 4 6 8
>>>
```

Differences with List Comprehensions.

* Does not construct a list.
* Only useful purpose is iteration.
* Once consumed, can't be reused.

General syntax.

```python
(<expression> for i in s if <conditional>)
```

It can also serve as a function argument.

```python
sum(x*x for x in a)
```

It can be applied to any iterable.

```python
>>> a = [1,2,3,4]
>>> b = (x*x for x in a)
>>> c = (-x for x in b)
>>> for i in c:
...   print(i, end=' ')
...
-1 -4 -9 -16
>>>
```

The main use of generator expressions is in code that performs some
calculation on a sequence, but only uses the result once.  For
example, strip all comments from a file.

```python
f = open('somefile.txt')
lines = (line for line in f if not line.startswith('#'))
for line in lines:
    ...
f.close()
```

With generators, the code runs faster and uses little memory. It's
like a filter applied to a stream.

### Why Generators

* Many problems are much more clearly expressed in terms of iteration.
  * Looping over a collection of items and performing some kind of operation (searching, replacing, modifying, etc.).
  * Processing pipelines can be applied to a wide range of data processing problems.
* Better memory efficiency.
  * Only produce values when needed.
  * Contrast to constructing giant lists.
  * Can operate on streaming data
* Generators encourage code reuse
  * Separates the *iteration* from code that uses the iteration
  * You can build a toolbox of interesting iteration functions and *mix-n-match*.

### `itertools` module

The `itertools` is a library module with various functions designed to help with iterators/generators.

```python
itertools.chain(s1,s2)
itertools.count(n)
itertools.cycle(s)
itertools.dropwhile(predicate, s)
itertools.groupby(s)
itertools.ifilter(predicate, s)
itertools.imap(function, s1, ... sN)
itertools.repeat(s, n)
itertools.tee(s, ncopies)
itertools.izip(s1, ... , sN)
```

All functions process data iteratively.
They implement various kinds of iteration patterns.

More information at [Generator Tricks for Systems Programmers](http://www.dabeaz.com/generators/) tutorial from PyCon '08.

## Exercises

In the previous exercises, you wrote some code that followed lines being written to a log file and parsed them into a sequence of rows.
This exercise continues to build upon that.  Make sure the `Data/stocksim.py` is still running.

### Exercise 6.13: Generator Expressions

Generator expressions are a generator version of a list comprehension.
For example:

```python
>>> nums = [1, 2, 3, 4, 5]
>>> squares = (x*x for x in nums)
>>> squares
<generator object <genexpr> at 0x109207e60>
>>> for n in squares:
...     print(n)
...
1
4
9
16
25
```

Unlike a list a comprehension, a generator expression can only be used once.
Thus, if you try another for-loop, you get nothing:

```python
>>> for n in squares:
...     print(n)
...
>>>
```

### Exercise 6.14: Generator Expressions in Function Arguments

Generator expressions are sometimes placed into function arguments.
It looks a little weird at first, but try this experiment:

```python
>>> nums = [1,2,3,4,5]
>>> sum([x*x for x in nums])    # A list comprehension
55
>>> sum(x*x for x in nums)      # A generator expression
55
>>>
```
In the above example, the second version using generators would
use significantly less memory if a large list was being manipulated.

In your `portfolio.py` file, you performed a few calculations
involving list comprehensions.  Try replacing these with
generator expressions.

### Exercise 6.15: Code simplification

Generators expressions are often a useful replacement for
small generator functions.  For example, instead of writing a
function like this:

```python
def filter_symbols(rows, names):
    for row in rows:
        if row['name'] in names:
            yield row
```

You could write something like this:

```python
rows = (row for row in rows if row['name'] in names)
```

Modify the `ticker.py` program to use generator expressions
as appropriate.


[Contents](../Contents.md) \| [Previous (6.3 Producer/Consumer)](03_Producers_consumers.md) \| [Next (7 Advanced Topics)](../07_Advanced_Topics/00_Overview.md)
