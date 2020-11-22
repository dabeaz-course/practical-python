[Contents](../Contents.md) \| [Previous (7.2 Anonymous Functions)](02_Anonymous_function.md) \| [Next (7.4 Decorators)](04_Function_decorators.md)

# 7.3 Returning Functions

This section introduces the idea of using functions to create other functions.

### Introduction

Consider the following function.

```python
def add(x, y):
    def do_add():
        print('Adding', x, y)
        return x + y
    return do_add
```

This is a function that returns another function.

```python
>>> a = add(3,4)
>>> a
<function do_add at 0x6a670>
>>> a()
Adding 3 4
7
```

### Local Variables

Observe how the inner function refers to variables defined by the outer
function.

```python
def add(x, y):
    def do_add():
        # `x` and `y` are defined above `add(x, y)`
        print('Adding', x, y)
        return x + y
    return do_add
```

Further observe that those variables are somehow kept alive after
`add()` has finished.

```python
>>> a = add(3,4)
>>> a
<function do_add at 0x6a670>
>>> a()
Adding 3 4      # Where are these values coming from?
7
```

### Closures

When an inner function is returned as a result, that inner function is known as a *closure*.

```python
def add(x, y):
    # `do_add` is a closure
    def do_add():
        print('Adding', x, y)
        return x + y
    return do_add
```

*Essential feature: A closure retains the values of all variables
 needed for the function to run properly later on.*   Think of a
closure as a function plus an extra environment that holds the values
of variables that it depends on.

### Using Closures

Closure are an essential feature of Python. However, their use if often subtle.
Common applications:

* Use in callback functions.
* Delayed evaluation.
* Decorator functions (later).

### Delayed Evaluation

Consider a function like this:

```python
def after(seconds, func):
    import time
    time.sleep(seconds)
    func()
```

Usage example:

```python
def greeting():
    print('Hello Guido')

after(30, greeting)
```

`after` executes the supplied function... later.

Closures carry extra information around.

```python
def add(x, y):
    def do_add():
        print(f'Adding {x} + {y} -> {x+y}')
    return do_add

def after(seconds, func):
    import time
    time.sleep(seconds)
    func()

after(30, add(2, 3))
# `do_add` has the references x -> 2 and y -> 3
```

### Code Repetition

Closures can also be used as technique for avoiding excessive code repetition.
You can write functions that make code.

## Exercises

### Exercise 7.7: Using Closures to Avoid Repetition

One of the more powerful features of closures is their use in
generating repetitive code.  If you refer back to [Exercise
5.7](../05_Object_model/02_Classes_encapsulation), recall the code for
defining a property with type checking.

```python
class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price
    ...
    @property
    def shares(self):
        return self._shares

    @shares.setter
    def shares(self, value):
        if not isinstance(value, int):
            raise TypeError('Expected int')
        self._shares = value
    ...
```

Instead of repeatedly typing that code over and over again, you can
automatically create it using a closure.

Make a file `typedproperty.py` and put the following code in
it:

```python
# typedproperty.py

def typedproperty(name, expected_type):
    private_name = '_' + name
    @property
    def prop(self):
        return getattr(self, private_name)

    @prop.setter
    def prop(self, value):
        if not isinstance(value, expected_type):
            raise TypeError(f'Expected {expected_type}')
        setattr(self, private_name, value)

    return prop
```

Now, try it out by defining a class like this:

```python
from typedproperty import typedproperty

class Stock:
    name = typedproperty('name', str)
    shares = typedproperty('shares', int)
    price = typedproperty('price', float)

    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price
```

Try creating an instance and verifying that type-checking works.

```python
>>> s = Stock('IBM', 50, 91.1)
>>> s.name
'IBM'
>>> s.shares = '100'
... should get a TypeError ...
>>>
```

### Exercise 7.8: Simplifying Function Calls

In the above example, users might find calls such as
`typedproperty('shares', int)` a bit verbose to type--especially if
they're repeated a lot.  Add the following definitions to the
`typedproperty.py` file:

```python
String = lambda name: typedproperty(name, str)
Integer = lambda name: typedproperty(name, int)
Float = lambda name: typedproperty(name, float)
```

Now, rewrite the `Stock` class to use these functions instead:

```python
class Stock:
    name = String('name')
    shares = Integer('shares')
    price = Float('price')

    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price
```

Ah, that's a bit better.   The main takeaway here is that closures and `lambda`
can often be used to simplify code and eliminate annoying repetition.  This
is often good.

### Exercise 7.9: Putting it into practice

Rewrite the `Stock` class in the file `stock.py` so that it uses typed properties
as shown.

[Contents](../Contents.md) \| [Previous (7.2 Anonymous Functions)](02_Anonymous_function.md) \| [Next (7.4 Decorators)](04_Function_decorators.md)
