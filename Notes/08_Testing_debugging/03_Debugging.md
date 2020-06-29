[Contents](../Contents.md) \| [Previous (8.2 Logging)](02_Logging.md) \| [Next (9 Packages)](../09_Packages/00_Overview.md)

# 8.3 Debugging

### Debugging Tips

So, your program has crashed...

```bash
bash % python3 blah.py
Traceback (most recent call last):
  File "blah.py", line 13, in ?
    foo()
  File "blah.py", line 10, in foo
    bar()
  File "blah.py", line 7, in bar
    spam()
  File "blah.py", 4, in spam
    line x.append(3)
AttributeError: 'int' object has no attribute 'append'
```

Now what?!

### Reading Tracebacks

The last line is the specific cause of the crash.

```bash
bash % python3 blah.py
Traceback (most recent call last):
  File "blah.py", line 13, in ?
    foo()
  File "blah.py", line 10, in foo
    bar()
  File "blah.py", line 7, in bar
    spam()
  File "blah.py", 4, in spam
    line x.append(3)
# Cause of the crash
AttributeError: 'int' object has no attribute 'append'
```

However, it's not always easy to read or understand.

*PRO TIP: Paste the whole traceback into Google.*

### Using the REPL

Use the option `-i` to keep Python alive when executing a script.

```bash
bash % python3 -i blah.py
Traceback (most recent call last):
  File "blah.py", line 13, in ?
    foo()
  File "blah.py", line 10, in foo
    bar()
  File "blah.py", line 7, in bar
    spam()
  File "blah.py", 4, in spam
    line x.append(3)
AttributeError: 'int' object has no attribute 'append'
>>>
```

It preserves the interpreter state. That means that you can go poking
around after the crash. Checking variable values and other state.

### Debugging with Print

`print()` debugging is quite common.

*Tip: Make sure you use `repr()`*

```python
def spam(x):
    print('DEBUG:', repr(x))
    ...
```

`repr()` shows you an accurate representation of a value. Not the *nice* printing output.

```python
>>> from decimal import Decimal
>>> x = Decimal('3.4')
# NO `repr`
>>> print(x)
3.4
# WITH `repr`
>>> print(repr(x))
Decimal('3.4')
>>>
```

### The Python Debugger

You can manually launch the debugger inside a program.

```python
def some_function():
    ...
    breakpoint()      # Enter the debugger (Python 3.7+)
    ...
```

This starts the debugger at the `breakpoint()` call.

In earlier Python versions, you did this.  You'll sometimes see this
mentioned in other debugging guides.

```python
import pdb
...
pdb.set_trace()       # Instead of `breakpoint()`
...
```

### Run under debugger

You can also run an entire program under debugger.

```bash
bash % python3 -m pdb someprogram.py
```

It will automatically enter the debugger before the first
statement. Allowing you to set breakpoints and change the
configuration.

Common debugger commands:

```code
(Pdb) help            # Get help
(Pdb) w(here)         # Print stack trace
(Pdb) d(own)          # Move down one stack level
(Pdb) u(p)            # Move up one stack level
(Pdb) b(reak) loc     # Set a breakpoint
(Pdb) s(tep)          # Execute one instruction
(Pdb) c(ontinue)      # Continue execution
(Pdb) l(ist)          # List source code
(Pdb) a(rgs)          # Print args of current function
(Pdb) !statement      # Execute statement
```

For breakpoints location is one of the following.

```code
(Pdb) b 45            # Line 45 in current file
(Pdb) b file.py:45    # Line 34 in file.py
(Pdb) b foo           # Function foo() in current file
(Pdb) b module.foo    # Function foo() in a module
```

## Exercises

### Exercise 8.4:  Bugs? What Bugs?

It runs. Ship it!

[Contents](../Contents.md) \| [Previous (8.2 Logging)](02_Logging.md) \| [Next (9 Packages)](../09_Packages/00_Overview.md)
