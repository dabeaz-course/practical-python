[Contents](../Contents.md) \| [Previous (9.1 Packages)](01_Packages.md) \| [Next (9.3 Distribution)](03_Distribution.md)

# 9.2 Third Party Modules

Python has a large library of built-in modules (*batteries included*).

There are even more third party modules. Check them in the [Python Package Index](https://pypi.org/) or PyPi.
Or just do a Google search for a specific topic.

How to handle third-party dependencies is an ever-evolving topic with
Python.  This section merely covers the basics to help you wrap
your brain around how it works.

### The Module Search Path

`sys.path` is a directory that contains the list of all directories
checked by the `import` statement. Look at it:

```python
>>> import sys
>>> sys.path
... look at the result ...
>>>
```

If you import something and it's not located in one of those
directories, you will get an `ImportError` exception.

### Standard Library Modules

Modules from Python's standard library usually come from a location
such as `/usr/local/lib/python3.6'.  You can find out for certain
by trying a short test:

```python
>>> import re
>>> re
<module 're' from '/usr/local/lib/python3.6/re.py'>
>>>
```

Simply looking at a module in the REPL is a good debugging tip
to know about.  It will show you the location of the file.

### Third-party Modules

Third party modules are usually located in a dedicated
`site-packages` directory.   You'll see it if you perform
the same steps as above:

```python
>>> import numpy
>>> numpy
<module 'numpy' from '/usr/local/lib/python3.6/site-packages/numpy/__init__.py'>
>>>
```

Again, looking at a module is a good debugging tip if you're
trying to figure out why something related to `import` isn't working
as expected.

### Installing Modules

The most common technique for installing a third-party module is to use
`pip`.  For example:

```bash
bash % python3 -m pip install packagename
```

This command will download the package and install it in the `site-packages`
directory.

### Problems

* You may be using an installation of Python that you don't directly control.
  * A corporate approved installation
  * You're using the Python version that comes with the OS.
* You might not have permission to install global packages in the computer.
* There might be other dependencies.

### Virtual Environments

A common solution to package installation issues is to create a
so-called "virtual environment" for yourself.  Naturally, there is no
"one way" to do this--in fact, there are several competing tools and
techniques.  However, if you are using a standard Python installation,
you can try typing this:

```bash
bash % python -m venv mypython
bash %
```

After a few moments of waiting, you will have a new directory
`mypython` that's your own little Python install.  Within that
directory you'll find a `bin/` directory (Unix) or a `Scripts/`
directory (Windows).  If you run the `activate` script found there, it
will "activate" this version of Python, making it the default `python`
command for the shell.  For example:

```bash
bash % source mypython/bin/activate
(mypython) bash %
```

From here, you can now start installing Python packages for yourself.
For example:

```
(mypython) bash % python -m pip install pandas
...
```

For the purposes of experimenting and trying out different
packages, a virtual environment will usually work fine.  If,
on the other hand, you're creating an application and it
has specific package dependencies, that is a slightly
different problem.

### Handling Third-Party Dependencies in Your Application

If you have written an application and it has specific third-party
dependencies, one challenge concerns the creation and preservation of
the environment that includes your code and the dependencies.  Sadly,
this has been an area of great confusion and frequent change over
Python's lifetime.  It continues to evolve even now.

Rather than provide information that's bound to be out of date soon,
I refer you to the [Python Packaging User Guide](https://packaging.python.org).

## Exercises

### Exercise 9.4 : Creating a Virtual Environment

See if you can recreate the steps of making a virtual environment and installing
pandas into it as shown above.

[Contents](../Contents.md) \| [Previous (9.1 Packages)](01_Packages.md) \| [Next (9.3 Distribution)](03_Distribution.md)






