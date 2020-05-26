# 4.1 Classes

### The `class` statement

Use the `class` statement to define a new object.

```python
class Player(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.health = 100

    def move(self, dx, dy):
        self.dx += dx
        self.dy += dy

    def damage(self, pts):
        self.health -= pts
```

In a nutshell, a class is a set of functions that carry out various operations on so-called *instances*.

### Instances

Instances are the actual *objects* that you manipulate in your program.

They are created by calling the class as a function.

```python
>>> a = Player(2, 3)
>>> b = Player(10, 20)
>>>
```

`a` anb `b` are instances of `Player`.

*Emphasize: The class statement is just the definition (it does nothing by itself). Similar to a function definition.*

### Instance Data

Each instance has its own local data.

```python
>>> a.x
2
>>> b.x
10
```

This data is initialized by the `__init__()`.

```python
class Player(object):
    def __init__(self, x, y):
        # Any value stored on `self` is instance data
        self.x = x
        self.y = y
        self.health = 100
```

There are no restrictions on the total number or type of attributes stored.

### Instance Methods

Instance methods are functions applied to instances of an object.

```python
class Player(object):
    ...
    # `move` is a method
    def move(self, dx, dy):
        self.x += dx
        self.y += dy
```

The object itself is always passed as first argument.

```python
>>> a.move(1, 2)

# matches `a` to `self`
# matches `1` to `dx`
# matches `2` to `dy`
def move(self, dx, dy):
```

By convention, the instance is called `self`. However, the actual name
used is unimportant. The object is always passed as the first
argument. It is simply Python programming style to call this argument
`self`.

### Class Scoping

Classes do not define a scope.

```python
class Player(object):
    ...
    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def left(self, amt):
        move(-amt, 0)       # NO. Calls a global `move` function
        self.move(-amt, 0)  # YES. Calls method `move` from above.
```

If you want to operate on an instance, you always have to refer too it explicitly (e.g., `self`).

## Exercises

### Exercise 4.1: Objects as Data Structures

In section 2 and 3, we worked with data represented as tuples and dictionaries.
For example, a holding of stock could be represented as a tuple like this:

```python
s = ('GOOG',100,490.10)
```

or as a dictionary like this:

```python
s = { 'name'   : 'GOOG',
      'shares' : 100,
      'price'  : 490.10
}
```

You can even write functions for manipulating such data. For example:

```python
def cost(s):
    return s['shares'] * s['price']
```

However, as your program gets large, you might want to create a better sense of organization.
Thus, another approach for representing data would be to define a class.

Create a file called `stock.py` and define a class `Stock` that represents a single holding of stock.
Have the instances of `Stock` have `name`, `shares`, and `price` attributes.

```python
>>> import stock
>>> s = stock.Stock('GOOG',100,490.10)
>>> s.name
'GOOG'
>>> s.shares
100
>>> s.price
490.1
>>>
```

Create a few more `Stock` objects and manipulate them. For example:

```python
>>> a = stock.Stock('AAPL',50,122.34)
>>> b = stock.Stock('IBM',75,91.75)
>>> a.shares * a.price
6117.0
>>> b.shares * b.price
6881.25
>>> stocks = [a,b,s]
>>> stocks
[<stock.Stock object at 0x37d0b0>, <stock.Stock object at 0x37d110>, <stock.Stock object at 0x37d050>]
>>> for t in stocks:
      print(f'{t.name:>10s} {t.shares:>10d} {t.price:>10.2f}')

... look at the output ...
>>>
```

One thing to emphasize here is that the class `Stock` acts like a factory for creating instances of objects.
Basically, you just call it as a function and it creates a new object for you.

Also, it needs to be emphasized that each object is distinct---they
each have their own data that is separate from other objects that have
been created.  An object defined by a class is somewhat similar to a
dictionary, just with somewhat different syntax.
For example, instead of writing `s['name']` or `s['price']`, you now
write `s.name` and `s.price`.

### Exercise 4.2: Reading Data into a List of Objects

In your `stock.py` program, write a function
`read_portfolio(filename)` that reads portfolio data from a file into
a list of `Stock` objects.  This function is going to mimic the
behavior of earlier code you have written.  Here’s how your function
will behave:

```python
>>> import stock
>>> portfolio = stock.read_portfolio('Data/portfolio.csv')
>>> portfolio
[<stock.Stock object at 0x81d70>, <stock.Stock object at 0x81cf0>, <stock.Stock object at 0x81db0>,
  <stock.Stock object at 0x81df0>, <stock.Stock object at 0x81e30>, <stock.Stock object at 0x81e70>,
  <stock.Stock object at 0x81eb0>]
>>>
```

It is important to emphasize that `read_portfolio()` is a top-level function, not a method of the `Stock` class.
This function is merely creating a list of `Stock` objects; it’s not an operation on an individual `Stock` instance.

Try performing some calculations with the above data. First, try printing a formatted table:

```python
>>> for s in portfolio:
          print(f'{s.name:>10s} {s.shares:>10d} {s.price:>10.2f}')

... look at the output ...
>>>
```

Try a list comprehension:

```python
>>> more100 = [s for s in portfolio if s.shares > 100]
>>> for s in more100:
          print(f'{s.name:>10s} {s.shares:>10d} {s.price:>10.2f}')

... look at the output ...
>>>
```

Again, notice the similarity between `Stock` objects and dictionaries. They’re basically the same idea, but the syntax for accessing values differs.

### Exercise 4.3: Adding some Methods

With classes, you can attach functions to your objects.  These are
known as methods and are functions that operate on the data stored
inside an object.

Add a `cost()` and `sell()` method to your `Stock` object. They should
work like this:

```python
>>> import stock
>>> s = stock.Stock('GOOG',100,490.10)
>>> s.cost()
49010.0
>>> s.shares
100
>>> s.sell(25)
>>> s.shares
75
>>> s.cost()
36757.5
>>>
```

[Contents](../Contents) \| [Previous (3.6 Design discussion)](../03_Program_organization/06_Design_discussion) \| [Next (4.2 Inheritance)](02_Inheritance)
