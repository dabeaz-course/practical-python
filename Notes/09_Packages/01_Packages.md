# 9.1 Packages

This section introduces the concept of a package.

### Modules

Any Python source file is a module.

```python
# foo.py
def grok(a):
    ...
def spam(b):
    ...
```

An `import` statement loads and *executes* a module.

```python
# program.py
import foo

a = foo.grok(2)
b = foo.spam('Hello')
...
```

### Packages vs Modules

For larger collections of code, it is common to organize modules into a package.

```code
# From this
pcost.py
report.py
fileparse.py

# To this
porty/
    __init__.py
    pcost.py
    report.py
    fileparse.py
```

You pick a name and make a top-level directory. `porty` in the example above.

Add an `__init__.py` file. It may be empty.

Put your source files into it.

### Using a Package

A package serves as a namespace for imports.

This means that there are multilevel imports.

```python
import porty.report
port = porty.report.read_portfolio('port.csv')
```

There are other variations of import statements.

```python
from porty import report
port = report.read_portfolio('port.csv')

from porty.report import read_portfolio
port = read_portfolio('port.csv')
```

### Two problems

There are two main problems with this approach.

* imports between files in the same package.
* Main scripts placed inside the package.

Both break.

### Problem: Imports

Imports between files in the same package *must include the package name in the import*.
Remember the structure.

```code
porty/
    __init__.py
    pcost.py
    report.py
    fileparse.py
```

Import example.

```python
# report.py
from porty import fileparse

def read_portfolio(filename):
    return fileparse.parse_csv(...)
```

All imports are *absolute*, not relative.

```python
# report.py
import fileparse    # BREAKS. fileparse not found

...
```

### Relative Imports

However, you can use `.` to refer to the current package. Instead of the package name.

```python
# report.py
from . import fileparse

def read_portfolio(filename):
    return fileparse.parse_csv(...)
```

Syntax:

```python
from . import modname
```

This makes it easy to rename the package.

### Problem: Main Scripts

Running a submodule as a main script breaks.

```bash
bash $ python porty/pcost.py # BREAKS
...
```

*Reason: You are running Python on a single file and Python doesn't see the rest of the package structure correctly (`sys.path` is wrong).*

All imports break.

### `__init__.py` files

The primary purpose of these files is to stitch modules together.

Example: consolidating functions

```python
# porty/__init__.py
from .pcost import portfolio_cost
from .report import portfolio_report
```

Makes names appear at the *top-level* when importing.

```python
from porty import portfolio_cost
portfolio_cost('portfolio.csv')
```

Instead of using the multilevel imports.

```python
from porty import pcost
pcost.portfolio_cost('portfolio.csv')
```

### Solution for scripts

Use `-m package.module` option.

```bash
bash % python3 -m porty.pcost portfolio.csv
```

It will run the code in a proper package environment.

There is another alternative: Write a new top-level script.

```python
#!/usr/bin/env python3
# pcost.py
import porty.pcost
import sys
porty.pcost.main(sys.argv)
```

This script lives *outside* the package.

### Application Structure

Code organization and file structure is key to the maintainability of an application.

One recommended structure is the following.

```code
porty-app/
  README.txt
  script.py         # SCRIPT
  porty/
    # LIBRARY CODE
    __init__.py
    pcost.py
    report.py
    fileparse.py
```

Top-level scripts need to exist outside the code package. One level up.

```python
#!/usr/bin/env python3
# script.py
import sys
import porty

porty.report.main(sys.argv)
```

## Exercises

At this point, you have a directory with several programs:

```
pcost.py          # computes portfolio cost
report.py         # Makes a report
ticker.py         # Produce a real-time stock ticker
```

There are a variety of supporting modules with other functionality:

```
stock.py          # Stock class
portfolio.py      # Portfolio class
fileparse.py      # CSV parsing
tableformat.py    # Formatted tables
follow.py         # Follow a log file
typedproperty.py  # Typed class properties
```

In this exercise, we're going to clean up the code and put it into
a common package.

### (a) Making a simple package

Make a directory called `porty/` and put all of the above Python
files into it.  Additionally create an empty `__init__.py` file and
put it in the directory.  You should have a directory of files
like this:

```
porty/
    __init__.py
    fileparse.py
    follow.py
    pcost.py
    portfolio.py
    report.py
    stock.py
    tableformat.py
    ticker.py
    typedproperty.py
```

Remove the file `__pycache__` that's sitting in your directory.  This
contains pre-compiled Python modules from before.  We want to start
fresh.

Try importing some of package modules:

```python
>>> import porty.report
>>> import porty.pcost
>>> import porty.ticker
```

If these imports fail, go into the appropriate file and fix the
module imports to include a package-relative import.   For example,
a statement such as `import fileparse` might change to the
following:

```
# report.py
from . import fileparse
...
```

If you have a statement such as `from fileparse import parse_csv`, change
the code to the following:

```
# report.py
from .fileparse import parse_csv
...
```

### (b) Making an application directory

Putting all of your code into a "package" isn't often enough for an
application. Sometimes there are supporting files, documentation,
scripts, and other things.  These files need to exist OUTSIDE of the
`porty/` directory you made above.

Create a new directory called `porty-app`.  Move the `porty` directory
you created in part (a) into that directory.  Copy the
`Data/portfolio.csv` and `Data/prices.csv` test files into this
directory.  Additionally create a `README.txt` file with some
information about yourself.  Your code should now be organized as
follows:

```
porty-app/
    portfolio.csv
    prices.csv
    README.txt
    porty/
        __init__.py
        fileparse.py
        follow.py
        pcost.py
        portfolio.py
        report.py
        stock.py
        tableformat.py
        ticker.py
        typedproperty.py
```

To run your code, you need to make sure you are working in the top-level `porty-app/`
directory.  For example, from the terminal:

```python
shell % cd porty-app
shell % python3
>>> import porty.report
>>>
```

Try running some of your prior scripts as a main program:

```python
shell % cd porty-app
shell % python3 -m porty.report portfolio.csv prices.csv txt
      Name     Shares      Price     Change
---------- ---------- ---------- ---------- 
        AA        100       9.22     -22.98
       IBM         50     106.28      15.18
       CAT        150      35.46     -47.98
      MSFT        200      20.89     -30.34
        GE         95      13.48     -26.89
      MSFT         50      20.89     -44.21
       IBM        100     106.28      35.84

shell %
```

### (c) Top-level Scripts

Using the `python -m` command is often a bit weird.  You may want to
write a top level script that simply deals with the oddities of packages.
Create a script `print-report.py` that produces the above report:

```python
#!/usr/bin/env python3
# print-report.py
import sys
from porty.report import main
main(sys.argv)
```

Put this script in the top-level `porty-app/` directory.  Make sure you
can run it in that location:

```
shell % cd porty-app
shell % python3 print-report.py portfolio.csv prices.csv txt
      Name     Shares      Price     Change
---------- ---------- ---------- ---------- 
        AA        100       9.22     -22.98
       IBM         50     106.28      15.18
       CAT        150      35.46     -47.98
      MSFT        200      20.89     -30.34
        GE         95      13.48     -26.89
      MSFT         50      20.89     -44.21
       IBM        100     106.28      35.84

shell %
```

Your final code should now be structured something like this:

```
porty-app/
    portfolio.csv
    prices.csv
    print-report.py
    README.txt
    porty/
        __init__.py
        fileparse.py
        follow.py
        pcost.py
        portfolio.py
        report.py
        stock.py
        tableformat.py
        ticker.py
        typedproperty.py
```

[Next](02_Third_party)