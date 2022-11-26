[Contents](../Contents.md) \| [Previous (7.5 Decorated Methods)](../07_Advanced_Topics/05_Decorated_methods.md) \| [Next (8.2 Logging)](02_Logging.md)

# 8.1 Testing

## Testing Rocks, Debugging Sucks

The dynamic nature of Python makes testing critically important to
most applications.  There is no compiler to find your bugs. The only
way to find bugs is to run the code and make sure you try out all of
its features.

## Assertions

The `assert` statement is an internal check for the program.  If an
expression is not true, it raises a `AssertionError` exception.

`assert` statement syntax.

```python
assert <expression> [, 'Diagnostic message']
```

For example.

```python
assert isinstance(10, int), 'Expected int'
```

It shouldn't be used to check the user-input (i.e., data entered
on a web form or something).  It's purpose is more for internal
checks and invariants (conditions that should always be true).

### Contract Programming

Also known as Design By Contract, liberal use of assertions is an
approach for designing software. It prescribes that software designers
should define precise interface specifications for the components of
the software.

For example, you might put assertions on all inputs of a function.

```python
def add(x, y):
    assert isinstance(x, int), 'Expected int'
    assert isinstance(y, int), 'Expected int'
    return x + y
```

Checking inputs will immediately catch callers who aren't using
appropriate arguments.

```python
>>> add(2, 3)
5
>>> add('2', '3')
Traceback (most recent call last):
...
AssertionError: Expected int
>>>
```

### Inline Tests

Assertions can also be used for simple tests.

```python
def add(x, y):
    return x + y

assert add(2,2) == 4
```

This way you are including the test in the same module as your code.

*Benefit: If the code is obviously broken, attempts to import the
 module will crash.*

This is not recommended for exhaustive testing. It's more of a
basic "smoke test".  Does the function work on any example at all?
If not, then something is definitely broken.

### `unittest` Module

Suppose you have some code.

```python
# simple.py

def add(x, y):
    return x + y
```

Now, suppose you want to test it.  Create a separate testing file like this.

```python
# test_simple.py

import simple
import unittest
```

Then define a testing class.

```python
# test_simple.py

import simple
import unittest

# Notice that it inherits from unittest.TestCase
class TestAdd(unittest.TestCase):
    ...
```

The testing class must inherit from `unittest.TestCase`.

In the testing class, you define the testing methods.

```python
# test_simple.py

import simple
import unittest

# Notice that it inherits from unittest.TestCase
class TestAdd(unittest.TestCase):
    def test_simple(self):
        # Test with simple integer arguments
        r = simple.add(2, 2)
        self.assertEqual(r, 5)
    def test_str(self):
        # Test with strings
        r = simple.add('hello', 'world')
        self.assertEqual(r, 'helloworld')
```

*Important: Each method must start with `test`.

### Using `unittest`

There are several built in assertions that come with `unittest`. Each of them asserts a different thing.

```python
# Assert that expr is True
self.assertTrue(expr)

# Assert that x == y
self.assertEqual(x,y)

# Assert that x != y
self.assertNotEqual(x,y)

# Assert that x is near y
self.assertAlmostEqual(x,y,places)

# Assert that callable(arg1,arg2,...) raises exc
self.assertRaises(exc, callable, arg1, arg2, ...)
```

This is not an exhaustive list. There are other assertions in the
module.

### Running `unittest`

To run the tests, turn the code into a script.

```python
# test_simple.py

...

if __name__ == '__main__':
    unittest.main()
```

Then run Python on the test file.

```bash
bash % python3 test_simple.py
F.
========================================================
FAIL: test_simple (__main__.TestAdd)
--------------------------------------------------------
Traceback (most recent call last):
  File "testsimple.py", line 8, in test_simple
    self.assertEqual(r, 5)
AssertionError: 4 != 5
--------------------------------------------------------
Ran 2 tests in 0.000s
FAILED (failures=1)
```

### Commentary

Effective unit testing is an art and it can grow to be quite
complicated for large applications.

The `unittest` module has a huge number of options related to test
runners, collection of results and other aspects of testing. Consult
the documentation for details.

### Third Party Test Tools

The built-in `unittest` module has the advantage of being available everywhere--it's
part of Python.  However, many programmers also find it to be quite verbose.
A popular alternative is [pytest](https://docs.pytest.org/en/latest/).   With pytest,
your testing file simplifies to something like the following:

```python
# test_simple.py
import simple

def test_simple():
    assert simple.add(2,2) == 4

def test_str():
    assert simple.add('hello','world') == 'helloworld'
```

To run the tests, you simply type a command such as `python -m pytest`.  It will
discover all of the tests and run them.

There's a lot more to `pytest` than this example, but it's usually pretty easy to
get started should you decide to try it out.

## Exercises

In this exercise, you will explore the basic mechanics of using
Python's `unittest` module.

In earlier exercises, you wrote a file `stock.py` that contained a
`Stock` class.  For this exercise, it assumed that you're using the
code written for [Exercise
7.9](../07_Advanced_Topics/03_Returning_functions) involving
typed-properties.  If, for some reason, that's not working, you might
want to copy the solution from `Solutions/7_9` to your working
directory.

### Exercise 8.1: Writing Unit Tests

In a separate file `test_stock.py`, write a set a unit tests
for the `Stock` class.   To get you started, here is a small
fragment of code that tests instance creation:


```python
# test_stock.py

import unittest
import stock

class TestStock(unittest.TestCase):
    def test_create(self):
        s = stock.Stock('GOOG', 100, 490.1)
        self.assertEqual(s.name, 'GOOG')
        self.assertEqual(s.shares, 100)
        self.assertEqual(s.price, 490.1)

if __name__ == '__main__':
    unittest.main()
```

Run your unit tests.   You should get some output that looks like this:

```
.
----------------------------------------------------------------------
Ran 1 tests in 0.000s

OK
```

Once you're satisfied that it works, write additional unit tests that
check for the following:

- Make sure the `s.cost` property returns the correct value (49010.0)
- Make sure the `s.sell()` method works correctly.  It should
  decrement the value of `s.shares` accordingly.
- Make sure that the `s.shares` attribute can't be set to a non-integer value.

For the last part, you're going to need to check that an exception is raised.
An easy way to do that is with code like this:

```python
class TestStock(unittest.TestCase):
    ...
    def test_bad_shares(self):
         s = stock.Stock('GOOG', 100, 490.1)
         with self.assertRaises(TypeError):
             s.shares = '100'
```

[Contents](../Contents.md) \| [Previous (7.5 Decorated Methods)](../07_Advanced_Topics/05_Decorated_methods.md) \| [Next (8.2 Logging)](02_Logging.md)
