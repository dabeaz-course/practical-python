[Contents](../Contents.md) \| [Previous (3.2 More on Functions)](02_More_functions.md) \| [Next (3.4 Modules)](04_Modules.md)

# 3.3 Error Checking

Although exceptions were introduced earlier, this section fills in some additional
details about error checking and exception handling.

### How programs fail

Python performs no checking or validation of function argument types
or values.  A function will work on any data that is compatible with
the statements in the function.

```python
def add(x, y):
    return x + y

add(3, 4)               # 7
add('Hello', 'World')   # 'HelloWorld'
add('3', '4')           # '34'
```

If there are errors in a function, they appear at run time (as an exception).

```python
def add(x, y):
    return x + y

>>> add(3, '4')
Traceback (most recent call last):
...
TypeError: unsupported operand type(s) for +:
'int' and 'str'
>>>
```

To verify code, there is a strong emphasis on testing (covered later).

### Exceptions

Exceptions are used to signal errors.
To raise an exception yourself, use `raise` statement.

```python
if name not in authorized:
    raise RuntimeError(f'{name} not authorized')
```

To catch an exception use `try-except`.

```python
try:
    authenticate(username)
except RuntimeError as e:
    print(e)
```

### Exception Handling

Exceptions propagate to the first matching `except`.

```python
def grok():
    ...
    raise RuntimeError('Whoa!')   # Exception raised here

def spam():
    grok()                        # Call that will raise exception

def bar():
    try:
       spam()
    except RuntimeError as e:     # Exception caught here
        ...

def foo():
    try:
         bar()
    except RuntimeError as e:     # Exception does NOT arrive here
        ...

foo()
```

To handle the exception, put statements in the `except` block. You can add any
statements you want to handle the error.

```python
def grok(): ...
    raise RuntimeError('Whoa!')

def bar():
    try:
      grok()
    except RuntimeError as e:   # Exception caught here
        statements              # Use this statements
        statements
        ...

bar()
```

After handling, execution resumes with the first statement after the
`try-except`.

```python
def grok(): ...
    raise RuntimeError('Whoa!')

def bar():
    try:
      grok()
    except RuntimeError as e:   # Exception caught here
        statements
        statements
        ...
    statements                  # Resumes execution here
    statements                  # And continues here
    ...

bar()
```

### Built-in Exceptions

There are about two-dozen built-in exceptions.  Usually the name of
the exception is indicative of what's wrong (e.g., a `ValueError` is
raised because you supplied a bad value). This is not an
exhaustive list. Check the documentation for more.

```python
ArithmeticError
AssertionError
EnvironmentError
EOFError
ImportError
IndexError
KeyboardInterrupt
KeyError
MemoryError
NameError
ReferenceError
RuntimeError
SyntaxError
SystemError
TypeError
ValueError
```

### Exception Values

Exceptions have an associated value. It contains more specific
information about what's wrong.

```python
raise RuntimeError('Invalid user name')
```

This value is part of the exception instance that's placed in the variable supplied to `except`.

```python
try:
    ...
except RuntimeError as e:   # `e` holds the exception raised
    ...
```

`e` is an instance of the exception type. However, it often looks like a string when
printed.

```python
except RuntimeError as e:
    print('Failed : Reason', e)
```

### Catching Multiple Errors

You can catch different kinds of exceptions using multiple `except` blocks.

```python
try:
  ...
except LookupError as e:
  ...
except RuntimeError as e:
  ...
except IOError as e:
  ...
except KeyboardInterrupt as e:
  ...
```

Alternatively, if the statements to handle them is the same, you can group them:

```python
try:
  ...
except (IOError,LookupError,RuntimeError) as e:
  ...
```

### Catching All Errors

To catch any exception, use `Exception` like this:

```python
try:
    ...
except Exception:       # DANGER. See below
    print('An error occurred')
```

In general, writing code like that is a bad idea because you'll have
no idea why it failed.

### Wrong Way to Catch Errors

Here is the wrong way to use exceptions.

```python
try:
    go_do_something()
except Exception:
    print('Computer says no')
```

This catches all possible errors and it may make it impossible to debug
when the code is failing for some reason you didn't expect at all
(e.g. uninstalled Python module, etc.).

### Somewhat Better Approach

If you're going to catch all errors, this is a more sane approach.

```python
try:
    go_do_something()
except Exception as e:
    print('Computer says no. Reason :', e)
```

It reports a specific reason for failure.  It is almost always a good
idea to have some mechanism for viewing/reporting errors when you
write code that catches all possible exceptions.

In general though, it's better to catch the error as narrowly as is
reasonable. Only catch the errors you can actually handle. Let
other errors pass by--maybe some other code can handle them.

### Reraising an Exception

Use `raise` to propagate a caught error.

```python
try:
    go_do_something()
except Exception as e:
    print('Computer says no. Reason :', e)
    raise
```

This allows you to take action (e.g. logging) and pass the error on to
the caller.

### Exception Best Practices

Don't catch exceptions. Fail fast and loud. If it's important, someone
else will take care of the problem.  Only catch an exception if you
are *that* someone.  That is, only catch errors where you can recover
and sanely keep going.

### `finally` statement

It specifies code that must run regardless of whether or not an
exception occurs.

```python
lock = Lock()
...
lock.acquire()
try:
    ...
finally:
    lock.release()  # this will ALWAYS be executed. With and without exception.
```

Commonly used to safely manage resources (especially locks, files, etc.).

### `with` statement

In modern code, `try-finally` is often replaced with the `with` statement.

```python
lock = Lock()
with lock:
    # lock acquired
    ...
# lock released
```

A more familiar example:

```python
with open(filename) as f:
    # Use the file
    ...
# File closed
```

`with` defines a usage *context* for a resource.  When execution
leaves that context, resources are released. `with` only works with
certain objects that have been specifically programmed to support it.

## Exercises

### Exercise 3.8: Raising exceptions

The `parse_csv()` function you wrote in the last section allows
user-specified columns to be selected, but that only works if the
input data file has column headers.

Modify the code so that an exception gets raised if both the `select`
and `has_headers=False` arguments are passed.  For example:

```python
>>> parse_csv('Data/prices.csv', select=['name','price'], has_headers=False)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "fileparse.py", line 9, in parse_csv
    raise RuntimeError("select argument requires column headers")
RuntimeError: select argument requires column headers
>>>
```

Having added this one check, you might ask if you should be performing
other kinds of sanity checks in the function.  For example, should you
check that the filename is a string, that types is a list, or anything
of that nature?

As a general rule, it’s usually best to skip such tests and to just
let the program fail on bad inputs.  The traceback message will point
at the source of the problem and can assist in debugging.

The main reason for adding the above check is to avoid running the code
in a non-sensical mode (e.g., using a feature that requires column
headers, but simultaneously specifying that there are no headers).

This indicates a programming error on the part of the calling code.
Checking for cases that "aren't supposed to happen" is often a good idea.

### Exercise 3.9: Catching exceptions

The `parse_csv()` function you wrote is used to process the entire
contents of a file.  However, in the real-world, it’s possible that
input files might have corrupted, missing, or dirty data.  Try this
experiment:

```python
>>> portfolio = parse_csv('Data/missing.csv', types=[str, int, float])
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "fileparse.py", line 36, in parse_csv
    row = [func(val) for func, val in zip(types, row)]
ValueError: invalid literal for int() with base 10: ''
>>>
```

Modify the `parse_csv()` function to catch all `ValueError` exceptions
generated during record creation and print a warning message for rows
that can’t be converted.

The message should include the row number and information about the
reason why it failed.  To test your function, try reading the file
`Data/missing.csv` above.  For example:

```python
>>> portfolio = parse_csv('Data/missing.csv', types=[str, int, float])
Row 4: Couldn't convert ['MSFT', '', '51.23']
Row 4: Reason invalid literal for int() with base 10: ''
Row 7: Couldn't convert ['IBM', '', '70.44']
Row 7: Reason invalid literal for int() with base 10: ''
>>>
>>> portfolio
[{'price': 32.2, 'name': 'AA', 'shares': 100}, {'price': 91.1, 'name': 'IBM', 'shares': 50}, {'price': 83.44, 'name': 'CAT', 'shares': 150}, {'price': 40.37, 'name': 'GE', 'shares': 95}, {'price': 65.1, 'name': 'MSFT', 'shares': 50}]
>>>
```

### Exercise 3.10: Silencing Errors

Modify the `parse_csv()` function so that parsing error messages can
be silenced if explicitly desired by the user.  For example:

```python
>>> portfolio = parse_csv('Data/missing.csv', types=[str,int,float], silence_errors=True)
>>> portfolio
[{'price': 32.2, 'name': 'AA', 'shares': 100}, {'price': 91.1, 'name': 'IBM', 'shares': 50}, {'price': 83.44, 'name': 'CAT', 'shares': 150}, {'price': 40.37, 'name': 'GE', 'shares': 95}, {'price': 65.1, 'name': 'MSFT', 'shares': 50}]
>>>
```

Error handling is one of the most difficult things to get right in
most programs.  As a general rule, you shouldn’t silently ignore
errors.  Instead, it’s better to report problems and to give the user
an option to the silence the error message if they choose to do so.

[Contents](../Contents.md) \| [Previous (3.2 More on Functions)](02_More_functions.md) \| [Next (3.4 Modules)](04_Modules.md)
