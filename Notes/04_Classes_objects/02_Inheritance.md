# 4.2 Inheritance

Inheritance is a commonly used tool for writing extensible programs.  This section explores that idea.

### Introduction

Inheritance is used to specialize existing objects:

```python
class Parent:
    ...

class Child(Parent): # Check how `Parent` is between the parenthesis
    ...
```

The new class `Child` is called a derived class or subclass.
The `Parent` class is known as base class or superclass. 
`Parent` is specified in `()` after the class name, `class Child(Parent):`.

### Extending

With inheritance, you are taking an existing class and:

* Adding new methods
* Redefining some of the existing methods
* Adding new attributes to instances

In the end you are **extending existing code**.

### Example

Suppose that this is your starting class:

```python
class Stock(object):
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    def cost(self):
        return self.shares * self.price

    def sell(self, nshares):
        self.shares -= nshares
```

You can change any part of this via inheritance.

### Add a new method

```python
class MyStock(Stock):
    def panic(self):
        self.sell(self.shares)
```

Usage example.

```python
>>> s = MyStock('GOOG', 100, 490.1)
>>> s.sell(25)
>>> s.shares 75
>>> s.panic()
>>> s.shares 0
>>>
```

### Redefining an existing method

```python
class MyStock(Stock):
    def cost(self):
        return 1.25 * self.shares * self.price
```

Usage example.

```python
>>> s = MyStock('GOOG', 100, 490.1)
>>> s.cost()
61262.5
>>>
```

The new method takes the place of the old one. The other methods are unaffected.

## Overriding

Sometimes a class extends an existing method, but it wants to use the original implementation.
For this, use `super()`:

```python
class Stock(object):
    ...
    def cost(self):
        return self.shares * self.price
    ...

class MyStock(Stock):
    def cost(self):
        # Check the call to `super`
        actual_cost = super().cost()
        return 1.25 * actual_cost
```

Use `super()` to call the previous version.

*Caution: Python 2 is different.*

```python
actual_cost = super(MyStock, self).cost()
```

### `__init__` and inheritance

If `__init__` is redefined, it is mandatory to initialize the parent.

```python
class Stock(object):
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

class MyStock(Stock):
    def __init__(self, name, shares, price, factor):
        # Check the call to `super` and `__init__`
        super().__init__(name, shares, price)
        self.factor = factor

    def cost(self):
        return self.factor * super().cost()
```

You should call the `init` on the `super` which is the way to call the previous version as shown previously.

### Using Inheritance

Inheritance is sometimes used to organize related objects.

```python
class Shape(object):
    ...

class Circle(Shape):
    ...

class Rectangle(Shape):
    ...
```

Think of a logical hierarchy or taxonomy.   However, a more common usage is
related to making reusable or extensible code:

```python
class CustomHandler(TCPHandler):
    def handle_request(self):
        ...
        # Custom processing
```

The base class contains some general purpose code.
Your class inherits and customized specific parts. Maybe it plugs into a framework.

### "is a" relationship

Inheritance establishes a type relationship.

```python
class Shape(object):
    ...

class Circle(Shape):
    ...
```

Check for object instance.

```python
>>> c = Circle(4.0)
>>> isinstance(c, Shape)
True
>>>
```

*Important: Code that works with the parent is also supposed to work with the child.*

### `object` base class

If a class has no parent, you sometimes see `object` used as the base.

```python
class Shape(object):
    ...
```

`object` is the parent of all objects in Python.

*Note: it's not technically required in Python 3. If omitted in Python 2, it results in an "old style class" which should be avoided.*

### Multiple Inheritance

You can inherit from multiple classes by specifying them in the definition of the class.

```python
class Mother(object):
    ...

class Father(object):
    ...

class Child(Mother, Father):
    ...
```

The class `Child` inherits features from both parents.  There are some rather tricky details. Don't do it unless you know what you are doing.
We're not going to explore multiple inheritance further in this course.

## Exercises

### Exercise 4.4: Print Portfolio

A major use of inheritance is in writing code that’s meant to be extended or customized in various ways—especially in libraries or frameworks.
To illustrate, start by adding the following function to your `stock.py` program:

```python
# stock.py
...
def print_portfolio(portfolio):
    '''
    Make a nicely formatted table showing portfolio contents.
    '''
    headers = ('Name','Shares','Price')
    for h in headers:
        print(f'{h:>10s}',end=' ')
    print()
    print(('-'*10 + ' ')*len(headers))
    for s in portfolio:
        print(f'{s.name:>10s} {s.shares:>10d} {s.price:>10.2f}')
```

Add a little testing section to the bottom of your `stock.py` file that runs the above function:

```python
if __name__ == '__main__':
    portfolio = read_portfolio('Data/portfolio.csv')
    print_portfolio(portfolio)
```

When you run your `stock.py`, you should get this output:

```bash
          Name     Shares      Price
    ---------- ---------- ----------
            AA        100      32.20
           IBM         50      91.10
           CAT        150      83.44
          MSFT        200      51.23
            GE         95      40.37
          MSFT         50      65.10
           IBM        100      70.44
```

### Exercise 4.5: An Extensibility Problem

Suppose that you wanted to modify the `print_portfolio()` function to
support a variety of different output formats such as plain-text,
HTML, CSV, or XML.  To do this, you could try to write one gigantic
function that did everything.  However, doing so would likely lead to
an unmaintainable mess. Instead, this is a perfect opportunity to use
inheritance instead.

To start, focus on the steps that are involved in a creating a
table. At the top of the table is a set of table headers. After that,
rows of table data appear.  Let’s take those steps and and put them into their own class.

Create a file called `tableformat.py` and define the following class:

```python
# tableformat.py

class TableFormatter(object):
    def headings(self, headers):
        '''
        Emit the table headings.
        '''
        raise NotImplementedError()

    def row(self, rowdata):
        '''
        Emit a single row of table data.
        '''
        raise NotImplementedError()
```

This class does nothing, but it serves as a kind of design specification for additional classes that will be defined shortly.

Modify the `print_portfolio()` function so that it accepts a `TableFormatter` object as input and invokes methods on it to produce the output.
For example, like this:

```python
# stock.py
...
def print_portfolio(portfolio, formatter):
    '''
    Make a nicely formatted table showing portfolio contents.
    '''
    formatter.headings(['Name', 'Shares', 'Price'])
    for s in portfolio:
        # Form a row of output data (as strings)
        rowdata = [s.name, str(s.shares), f'{s.price:0.2f}' ]
        formatter.row(rowdata)
```

Finally, try your new class by modifying the main program like this:

```python
# stock.py
...
if __name__ == '__main__':
    from tableformat import TableFormatter
    portfolio = read_portfolio('Data/portfolio.csv')
    formatter = TableFormatter()
    print_portfolio(portfolio, formatter)
```

When you run this new code, your program will immediately crash with a `NotImplementedError` exception.
That’s not too exciting, but continue to the next part.

### Exercise 4.6: Using Inheritance to Produce Different Output

The `TableFormatter` class you defined in part (a) is meant to be extended via inheritance.
In fact, that’s the whole idea. To illustrate, define a class `TextTableFormatter` like this:

```python
# tableformat.py
...
class TextTableFormatter(TableFormatter):
    '''
    Emit a table in plain-text format
    '''
    def headings(self, headers):
        for h in headers:
            print(f'{h:>10s}', end=' ')
        print()
        print(('-'*10 + ' ')*len(headers))

    def row(self, rowdata):
        for d in rowdata:
            print(f'{d:>10s}', end=' ')
        print()
```

Modify your main program in `stock.py` like this and try it:

```python
# stock.py
...
if __name__ == '__main__':
    from tableformat import TextTableFormatter
    portfolio = read_portfolio('Data/portfolio.csv')
    formatter = TextTableFormatter()
    print_portfolio(portfolio, formatter)
```

This should produce the same output as before:

```bash
          Name     Shares      Price
    ---------- ---------- ----------
            AA        100      32.20
           IBM         50      91.10
           CAT        150      83.44
          MSFT        200      51.23
            GE         95      40.37
          MSFT         50      65.10
           IBM        100      70.44
```

However, let’s change the output to something else. Define a new class `CSVTableFormatter` that produces output in CSV format:

```python
# tableformat.py
...
class CSVTableFormatter(TableFormatter):
    '''
    Output portfolio data in CSV format.
    '''
    def headings(self, headers):
        print(','.join(headers))

    def row(self, rowdata):
        print(','.join(rowdata))
```

Modify your main program as follows:

```python
# stock.py
...
if __name__ == '__main__':
    from tableformat import CSVTableFormatter
    portfolio = read_portfolio('Data/portfolio.csv')
    formatter = CSVTableFormatter()
    print_portfolio(portfolio, formatter)
```

You should now see CSV output like this:

```csv
Name,Shares,Price
AA,100,32.20
IBM,50,91.10
CAT,150,83.44
MSFT,200,51.23
GE,95,40.37
MSFT,50,65.10
IBM,100,70.44
```

Using a similar idea, define a class `HTMLTableFormatter` that produces a table with the following output:

```html
<tr> <th>Name</th> <th>Shares</th> <th>Price</th> </tr>
<tr> <td>AA</td> <td>100</td> <td>32.20</td> </tr>
<tr> <td>IBM</td> <td>50</td> <td>91.10</td> </tr>
```

Test your code by modifying the main program to create a `HTMLTableFormatter` object instead of a `CSVTableFormatter` object.

### Exercise 4.7: Polymorphism in Action

A major feature of object-oriented programming is that you can plug an
object into a program and it will work without having to change any of
the existing code. For example, if you wrote a program that expected
to use a `TableFormatter` object, it would work no matter what kind of
`TableFormatter` you actually gave it.

This behavior is sometimes referred to as *polymorphism*.

One potential problem is making it easier for the user to pick the formatter that they want.
This can sometimes be fixed by defining a helper function.

In the `tableformat.py` file, add a function `create_formatter(name)`
that allows a user to create a formatter given an output name such as
`'txt'`, `'csv'`, or `'html'`.

For example:

```python
# stock.py
...
if __name__ == '__main__':
    from tableformat import create_formatter
    portfolio = read_portfolio('Data/portfolio.csv')
    formatter = create_formatter('csv')
    print_portfolio(portfolio, formatter)
```

When you run this program, you’ll see output such as this:

```csv
Name,Shares,Price
AA,100,32.20
IBM,50,91.10
CAT,150,83.44
MSFT,200,51.23
GE,95,40.37
MSFT,50,65.10
IBM,100,70.44
```

Try changing the format to `'txt'` and `'html'` just to make sure your
code is working correctly.  If the user provides a bad output format
to the `create_formatter()` function, have it raise a `RuntimeError`
exception. For example:

```python
>>> from tableformat import create_formatter
>>> formatter = create_formatter('xls')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "tableformat.py", line 68, in create_formatter
    raise RuntimeError('Unknown table format %s' % name)
RuntimeError: Unknown table format xls
>>>
```

Writing extensible code is one of the most common uses of inheritance in libraries and frameworks.
For example, a framework might instruct you to define your own object that inherits from a provided base class.
You’re then told to fill in various methods that implement various bits of functionality.
That said, designing object oriented programs can be extremely
difficult. For more information, you should probably look for books on
the topic of design patterns.

That said, understanding what happened in this exercise will take you
pretty far in terms of using most library modules and knowing
what inheritance is good for (extensibility).

[Contents](../Contents) \| [Previous (4.1 Classes)](01_Class) \| [Next (4.3 Special methods)](03_Special_methods)
