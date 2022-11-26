[Contents](../Contents.md) \| [Previous (3.3 Error Checking)](03_Error_checking.md) \| [Next (3.5 Main Module)](05_Main_module.md)

# 3.4 Modules

This section introduces the concept of modules and working with functions that span
multiple files.

### Modules and import

Any Python source file is a module.

```python
# foo.py
def grok(a):
    ...
def spam(b):
    ...
```

The `import` statement loads and *executes* a module.

```python
# program.py
import foo

a = foo.grok(2)
b = foo.spam('Hello')
...
```

### Namespaces

A module is a collection of named values and is sometimes said to be a
*namespace*.  The names are all of the global variables and functions
defined in the source file.  After importing, the module name is used
as a prefix. Hence the *namespace*.

```python
import foo

a = foo.grok(2)
b = foo.spam('Hello')
...
```

The module name is directly tied to the file name (foo -> foo.py).

### Global Definitions

Everything defined in the *global* scope is what populates the module
namespace. Consider two modules
that define the same variable `x`.

```python
# foo.py
x = 42
def grok(a):
    ...
```

```python
# bar.py
x = 37
def spam(a):
    ...
```

In this case, the `x` definitions refer to different variables.  One
is `foo.x` and the other is `bar.x`.  Different modules can use the
same names and those names won't conflict with each other.

**Modules are isolated.**

### Modules as Environments

Modules form an enclosing environment for all of the code defined inside.

```python
# foo.py
x = 42

def grok(a):
    print(x)
```

*Global* variables are always bound to the enclosing module (same file).
Each source file is its own little universe.

### Module Execution

When a module is imported, *all of the statements in the module
execute* one after another until the end of the file is reached.  The
contents of the module namespace are all of the *global* names that
are still defined at the end of the execution process.  If there are
scripting statements that carry out tasks in the global scope
(printing, creating files, etc.) you will see them run on import.

### `import as` statement

You can change the name of a module as you import it:

```python
import math as m
def rectangular(r, theta):
    x = r * m.cos(theta)
    y = r * m.sin(theta)
    return x, y
```

It works the same as a normal import. It just renames the module in that one file.

### `from` module import

This picks selected symbols out of a module and makes them available locally.

```python
from math import sin, cos

def rectangular(r, theta):
    x = r * cos(theta)
    y = r * sin(theta)
    return x, y
```

This allows parts of a module to be used without having to type the module prefix.
It's useful for frequently used names.

### Comments on importing

Variations on import do *not* change the way that modules work.

```python
import math
# vs
import math as m
# vs
from math import cos, sin
...
```

Specifically, `import` always executes the *entire* file and modules
are still isolated environments.

The `import module as` statement is only changing the name locally.
The `from math import cos, sin` statement still loads the entire
math module behind the scenes. It's merely copying the `cos` and `sin`
names from the module into the local space after it's done.

### Module Loading

Each module loads and executes only *once*.
*Note: Repeated imports just return a reference to the previously loaded module.*

`sys.modules` is a dict of all loaded modules.

```python
>>> import sys
>>> sys.modules.keys()
['copy_reg', '__main__', 'site', '__builtin__', 'encodings', 'encodings.encodings', 'posixpath', ...]
>>>
```

**Caution:** A common confusion arises if you repeat an `import` statement after
changing the source code for a module.  Because of the module cache `sys.modules`,
repeated imports always return the previously loaded module--even if a change
was made.  The safest way to load modified code into Python is to quit and restart
the interpreter.

### Locating Modules

Python consults a path list (sys.path) when looking for modules.

```python
>>> import sys
>>> sys.path
[
  '',
  '/usr/local/lib/python36/python36.zip',
  '/usr/local/lib/python36',
  ...
]
```

The current working directory is usually first.

### Module Search Path

As noted, `sys.path` contains the search paths.
You can manually adjust if you need to.

```python
import sys
sys.path.append('/project/foo/pyfiles')
```

Paths can also be added via environment variables.

```python
% env PYTHONPATH=/project/foo/pyfiles python3
Python 3.6.0 (default, Feb 3 2017, 05:53:21)
[GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.38)]
>>> import sys
>>> sys.path
['','/project/foo/pyfiles', ...]
```

As a general rule, it should not be necessary to manually adjust
the module search path.  However, it sometimes arises if you're
trying to import Python code that's in an unusual location or
not readily accessible from the current working directory.

## Exercises

For this exercise involving modules, it is critically important to
make sure you are running Python in a proper environment.  Modules 
often present new programmers with problems related to the current working
directory or with Python's path settings.  For this course, it is
assumed that you're writing all of your code in the `Work/` directory.
For best results, you should make sure you're also in that directory
when you launch the interpreter.  If not, you need to make sure
`practical-python/Work` is added to `sys.path`.

### Exercise 3.11: Module imports

In section 3, we created a general purpose function `parse_csv()` for
parsing the contents of CSV datafiles.

Now, we’re going to see how to use that function in other programs.
First, start in a new shell window.  Navigate to the folder where you
have all your files. We are going to import them.

Start Python interactive mode.

```shell
bash % python3
Python 3.6.1 (v3.6.1:69c0db5050, Mar 21 2017, 01:21:04)
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

Once you’ve done that, try importing some of the programs you
previously wrote.  You should see their output exactly as before.
Just to emphasize, importing a module runs its code.

```python
>>> import bounce
... watch output ...
>>> import mortgage
... watch output ...
>>> import report
... watch output ...
>>>
```

If none of this works, you’re probably running Python in the wrong directory.
Now, try importing your `fileparse` module and getting some help on it.

```python
>>> import fileparse
>>> help(fileparse)
... look at the output ...
>>> dir(fileparse)
... look at the output ...
>>>
```

Try using the module to read some data:

```python
>>> portfolio = fileparse.parse_csv('Data/portfolio.csv',select=['name','shares','price'], types=[str,int,float])
>>> portfolio
... look at the output ...
>>> pricelist = fileparse.parse_csv('Data/prices.csv',types=[str,float], has_headers=False)
>>> pricelist
... look at the output ...
>>> prices = dict(pricelist)
>>> prices
... look at the output ...
>>> prices['IBM']
106.11
>>>
```

Try importing a function so that you don’t need to include the module name:

```python
>>> from fileparse import parse_csv
>>> portfolio = parse_csv('Data/portfolio.csv', select=['name','shares','price'], types=[str,int,float])
>>> portfolio
... look at the output ...
>>>
```

### Exercise 3.12: Using your library module

In section 2, you wrote a program `report.py` that produced a stock report like this:

```
      Name     Shares      Price     Change
---------- ---------- ---------- ----------
        AA        100       9.22     -22.98
       IBM         50     106.28      15.18
       CAT        150      35.46     -47.98
      MSFT        200      20.89     -30.34
        GE         95      13.48     -26.89
      MSFT         50      20.89     -44.21
       IBM        100     106.28      35.84
```

Take that program and modify it so that all of the input file
processing is done using functions in your `fileparse` module.  To do
that, import `fileparse` as a module and change the `read_portfolio()`
and `read_prices()` functions to use the `parse_csv()` function.

Use the interactive example at the start of this exercise as a guide.
Afterwards, you should get exactly the same output as before.

### Exercise 3.13: Intentionally left blank (skip)

### Exercise 3.14: Using more library imports

In section 1, you wrote a program `pcost.py` that read a portfolio and computed its cost.

```python
>>> import pcost
>>> pcost.portfolio_cost('Data/portfolio.csv')
44671.15
>>>
```

Modify the `pcost.py` file so that it uses the `report.read_portfolio()` function.

### Commentary

When you are done with this exercise, you should have three
programs. `fileparse.py` which contains a general purpose
`parse_csv()` function.  `report.py` which produces a nice report, but
also contains `read_portfolio()` and `read_prices()` functions.  And
finally, `pcost.py` which computes the portfolio cost, but makes use
of the `read_portfolio()` function written for the `report.py` program.

[Contents](../Contents.md) \| [Previous (3.3 Error Checking)](03_Error_checking.md) \| [Next (3.5 Main Module)](05_Main_module.md)
