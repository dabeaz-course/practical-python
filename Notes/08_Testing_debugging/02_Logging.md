[Contents](../Contents.md) \| [Previous (8.1 Testing)](01_Testing.md) \| [Next (8.3 Debugging)](03_Debugging.md)

# 8.2 Logging

This section briefly introduces the logging module.

### logging Module

The `logging` module is a standard library module for recording
diagnostic information.  It's also a very large module with a lot of
sophisticated functionality.  We will show a simple example to
illustrate its usefulness.

### Exceptions Revisited

In the exercises, we wrote a function `parse()` that looked something
like this:

```python
# fileparse.py
def parse(f, types=None, names=None, delimiter=None):
    records = []
    for line in f:
        line = line.strip()
        if not line: continue
        try:
            records.append(split(line,types,names,delimiter))
        except ValueError as e:
            print("Couldn't parse :", line)
            print("Reason :", e)
    return records
```

Focus on the `try-except` statement. What should you do in the `except` block?

Should you print a warning message?

```python
try:
    records.append(split(line,types,names,delimiter))
except ValueError as e:
    print("Couldn't parse :", line)
    print("Reason :", e)
```

Or do you silently ignore it?

```python
try:
    records.append(split(line,types,names,delimiter))
except ValueError as e:
    pass
```

Neither solution is satisfactory because you often want *both* behaviors (user selectable).

### Using logging

The `logging` module can address this.

```python
# fileparse.py
import logging
log = logging.getLogger(__name__)

def parse(f,types=None,names=None,delimiter=None):
    ...
    try:
        records.append(split(line,types,names,delimiter))
    except ValueError as e:
        log.warning("Couldn't parse : %s", line)
        log.debug("Reason : %s", e)
```

The code is modified to issue warning messages or a special `Logger`
object. The one created with `logging.getLogger(__name__)`.

### Logging Basics

Create a logger object.

```python
log = logging.getLogger(name)   # name is a string
```

Issuing log messages.

```python
log.critical(message [, args])
log.error(message [, args])
log.warning(message [, args])
log.info(message [, args])
log.debug(message [, args])
```

*Each method represents a different level of severity.*

All of them create a formatted log message. `args` is used with the `%` operator to create the message.

```python
logmsg = message % args # Written to the log
```

### Logging Configuration

The logging behavior is configured separately.

```python
# main.py

...

if __name__ == '__main__':
    import logging
    logging.basicConfig(
        filename  = 'app.log',      # Log output file
        level     = logging.INFO,   # Output level
    )
```

Typically, this is a one-time configuration at program startup.  The
configuration is separate from the code that makes the logging calls.

### Comments

Logging is highly configurable.  You can adjust every aspect of it:
output files, levels, message formats, etc.  However, the code that
uses logging doesn't have to worry about that.

## Exercises

### Exercise 8.2: Adding logging to a module

In `fileparse.py`, there is some error handling related to
exceptions caused by bad input. It looks like this:

```python
# fileparse.py
import csv

def parse_csv(lines, select=None, types=None, has_headers=True, delimiter=',', silence_errors=False):
    '''
    Parse a CSV file into a list of records with type conversion.
    '''
    if select and not has_headers:
        raise RuntimeError('select requires column headers')

    rows = csv.reader(lines, delimiter=delimiter)

    # Read the file headers (if any)
    headers = next(rows) if has_headers else []

    # If specific columns have been selected, make indices for filtering and set output columns
    if select:
        indices = [ headers.index(colname) for colname in select ]
        headers = select

    records = []
    for rowno, row in enumerate(rows, 1):
        if not row:     # Skip rows with no data
            continue

        # If specific column indices are selected, pick them out
        if select:
            row = [ row[index] for index in indices]

        # Apply type conversion to the row
        if types:
            try:
                row = [func(val) for func, val in zip(types, row)]
            except ValueError as e:
                if not silence_errors:
                    print(f"Row {rowno}: Couldn't convert {row}")
                    print(f"Row {rowno}: Reason {e}")
                continue

        # Make a dictionary or a tuple
        if headers:
            record = dict(zip(headers, row))
        else:
            record = tuple(row)
        records.append(record)

    return records
```

Notice the print statements that issue diagnostic messages.  Replacing those
prints with logging operations is relatively simple.  Change the code like this:

```python
# fileparse.py
import csv
import logging
log = logging.getLogger(__name__)

def parse_csv(lines, select=None, types=None, has_headers=True, delimiter=',', silence_errors=False):
    '''
    Parse a CSV file into a list of records with type conversion.
    '''
    if select and not has_headers:
        raise RuntimeError('select requires column headers')

    rows = csv.reader(lines, delimiter=delimiter)

    # Read the file headers (if any)
    headers = next(rows) if has_headers else []

    # If specific columns have been selected, make indices for filtering and set output columns
    if select:
        indices = [ headers.index(colname) for colname in select ]
        headers = select

    records = []
    for rowno, row in enumerate(rows, 1):
        if not row:     # Skip rows with no data
            continue

        # If specific column indices are selected, pick them out
        if select:
            row = [ row[index] for index in indices]

        # Apply type conversion to the row
        if types:
            try:
                row = [func(val) for func, val in zip(types, row)]
            except ValueError as e:
                if not silence_errors:
                    log.warning("Row %d: Couldn't convert %s", rowno, row)
                    log.debug("Row %d: Reason %s", rowno, e)
                continue

        # Make a dictionary or a tuple
        if headers:
            record = dict(zip(headers, row))
        else:
            record = tuple(row)
        records.append(record)

    return records
```

Now that you've made these changes, try using some of your code on
bad data.

```python
>>> import report
>>> a = report.read_portfolio('Data/missing.csv')
Row 4: Bad row: ['MSFT', '', '51.23']
Row 7: Bad row: ['IBM', '', '70.44']
>>>
```

If you do nothing, you'll only get logging messages for the `WARNING`
level and above.  The output will look like simple print statements.
However, if you configure the logging module, you'll get additional
information about the logging levels, module, and more.  Type these
steps to see that:

```python
>>> import logging
>>> logging.basicConfig()
>>> a = report.read_portfolio('Data/missing.csv')
WARNING:fileparse:Row 4: Bad row: ['MSFT', '', '51.23']
WARNING:fileparse:Row 7: Bad row: ['IBM', '', '70.44']
>>>
```

You will notice that you don't see the output from the `log.debug()`
operation. Type this to change the level.

```
>>> logging.getLogger('fileparse').setLevel(logging.DEBUG)
>>> a = report.read_portfolio('Data/missing.csv')
WARNING:fileparse:Row 4: Bad row: ['MSFT', '', '51.23']
DEBUG:fileparse:Row 4: Reason: invalid literal for int() with base 10: ''
WARNING:fileparse:Row 7: Bad row: ['IBM', '', '70.44']
DEBUG:fileparse:Row 7: Reason: invalid literal for int() with base 10: ''
>>>
```

Turn off all, but the most critical logging messages:

```
>>> logging.getLogger('fileparse').setLevel(logging.CRITICAL)
>>> a = report.read_portfolio('Data/missing.csv')
>>>
```

### Exercise 8.3: Adding Logging to a Program

To add logging to an application, you need to have some mechanism to
initialize the logging module in the main module.  One way to
do this is to include some setup code that looks like this:

```
# This file sets up basic configuration of the logging module.
# Change settings here to adjust logging output as needed.
import logging
logging.basicConfig(
    filename = 'app.log',            # Name of the log file (omit to use stderr)
    filemode = 'w',                  # File mode (use 'a' to append)
    level    = logging.WARNING,      # Logging level (DEBUG, INFO, WARNING, ERROR, or CRITICAL)
)
```

Again, you'd need to put this someplace in the startup steps of your
program.  For example, where would you put this in your `report.py` program?

[Contents](../Contents.md) \| [Previous (8.1 Testing)](01_Testing.md) \| [Next (8.3 Debugging)](03_Debugging.md)
