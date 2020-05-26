# 9.2 Third Party Modules

### Introduction

Python has a large library of built-in modules (*batteries included*).

There are even more third party modules. Check them in the [Python Package Index](https://pypi.org/) or PyPi. Or just do a Google search for a topic.

### Some Notable Modules

* `requests`: Accessing web services.
* `numpy`, `scipy`: Arrays and vector mathematics.
* `pandas`: Stats and data analysis.
* `django`, `flask`: Web programming.
* `sqlalchemy`: Databases and ORM.
* `ipython`: Alternative interactive shell.

### Installing Modules

Most common classic technique: `pip`.

```bash
bash % python3 -m pip install packagename
```

This command will download the package and install it globally in your Python folder. Somewhere like:

```code
/usr/local/lib/python3.6/site-packages
```

### Problems

* You may be using an installation of Python that you don't directly control.
  * A corporate approved installation
  * The Python version that comes with the OS.
* You might not have permission to install global packages in the computer.
* Your program might have unusual dependencies.

### Talk about environments...


## Exercises

(rewrite)
