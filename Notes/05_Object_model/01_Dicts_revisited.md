[Contents](../Contents.md) \| [Previous (4.4 Exceptions)](../04_Classes_objects/04_Defining_exceptions.md) \| [Next (5.2 Encapsulation)](02_Classes_encapsulation.md)

# 5.1 Dictionaries Revisited

The Python object system is largely based on an implementation
involving dictionaries.  This section discusses that.

### Dictionaries, Revisited

Remember that a dictionary is a collection of named values.

```python
stock = {
    'name' : 'GOOG',
    'shares' : 100,
    'price' : 490.1
}
```

Dictionaries are commonly used for simple data structures.  However,
they are used for critical parts of the interpreter and may be the
*most important type of data in Python*.

### Dicts and Modules

Within a module, a dictionary holds all of the global variables and
functions.

```python
# foo.py

x = 42
def bar():
    ...

def spam():
    ...
```

If you inspect `foo.__dict__` or `globals()`, you'll see the dictionary.

```python
{
    'x' : 42,
    'bar' : <function bar>,
    'spam' : <function spam>
}
```

### Dicts and Objects

User defined objects also use dictionaries for both instance data and
classes.  In fact, the entire object system is mostly an extra layer
that's put on top of dictionaries.

A dictionary holds the instance data, `__dict__`.

```python
>>> s = Stock('GOOG', 100, 490.1)
>>> s.__dict__
{'name' : 'GOOG', 'shares' : 100, 'price': 490.1 }
```

You populate this dict (and instance) when assigning to `self`.

```python
class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price
```

The instance data, `self.__dict__`, looks like this:

```python
{
    'name': 'GOOG',
    'shares': 100,
    'price': 490.1
}
```

**Each instance gets its own private dictionary.**

```python
s = Stock('GOOG', 100, 490.1)     # {'name' : 'GOOG','shares' : 100, 'price': 490.1 }
t = Stock('AAPL', 50, 123.45)     # {'name' : 'AAPL','shares' : 50, 'price': 123.45 }
```

If you created 100 instances of some class, there are 100 dictionaries
sitting around holding data.

### Class Members

A separate dictionary also holds the methods.

```python
class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    def cost(self):
        return self.shares * self.price

    def sell(self, nshares):
        self.shares -= nshares
```

The dictionary is in `Stock.__dict__`.

```python
{
    'cost': <function>,
    'sell': <function>,
    '__init__': <function>
}
```

### Instances and Classes

Instances and classes are linked together.  The `__class__` attribute
refers back to the class.

```python
>>> s = Stock('GOOG', 100, 490.1)
>>> s.__dict__
{ 'name': 'GOOG', 'shares': 100, 'price': 490.1 }
>>> s.__class__
<class '__main__.Stock'>
>>>
```

The instance dictionary holds data unique to each instance, whereas
the class dictionary holds data collectively shared by *all*
instances.

### Attribute Access

When you work with objects, you access data and methods using the `.` operator.

```python
x = obj.name          # Getting
obj.name = value      # Setting
del obj.name          # Deleting
```

These operations are directly tied to the dictionaries sitting underneath the covers.

### Modifying Instances

Operations that modify an object update the underlying dictionary.

```python
>>> s = Stock('GOOG', 100, 490.1)
>>> s.__dict__
{ 'name':'GOOG', 'shares': 100, 'price': 490.1 }
>>> s.shares = 50       # Setting
>>> s.date = '6/7/2007' # Setting
>>> s.__dict__
{ 'name': 'GOOG', 'shares': 50, 'price': 490.1, 'date': '6/7/2007' }
>>> del s.shares        # Deleting
>>> s.__dict__
{ 'name': 'GOOG', 'price': 490.1, 'date': '6/7/2007' }
>>>
```

### Reading Attributes

Suppose you read an attribute on an instance.

```python
x = obj.name
```

The attribute may exist in two places:

* Local instance dictionary.
* Class dictionary.

Both dictionaries must be checked.  First, check in local `__dict__`.
If not found, look in `__dict__` of class through `__class__`.

```python
>>> s = Stock(...)
>>> s.name
'GOOG'
>>> s.cost()
49010.0
>>>
```

This lookup scheme is how the members of a *class* get shared by all instances.

### How inheritance works

Classes may inherit from other classes.

```python
class A(B, C):
    ...
```

The base classes are stored in a tuple in each class.

```python
>>> A.__bases__
(<class '__main__.B'>, <class '__main__.C'>)
>>>
```

This provides a link to parent classes.

### Reading Attributes with Inheritance

Logically, the process of finding an attribute is as follows. First,
check in local `__dict__`.  If not found, look in `__dict__` of the
class.  If not found in class, look in the base classes through
`__bases__`.   However, there are some subtle aspects of this discussed next.

### Reading Attributes with Single Inheritance

In inheritance hierarchies, attributes are found by walking up the
inheritance tree in order.

```python
class A: pass
class B(A): pass
class C(A): pass
class D(B): pass
class E(D): pass
```
With single inheritance, there is single path to the top.
You stop with the first match.

### Method Resolution Order or MRO

Python precomputes an inheritance chain and stores it in the *MRO* attribute on the class.
You can view it.

```python
>>> E.__mro__
(<class '__main__.E'>, <class '__main__.D'>,
 <class '__main__.B'>, <class '__main__.A'>,
 <type 'object'>)
>>>
```

This chain is called the **Method Resolution Order**.  To find an
attribute, Python walks the MRO in order. The first match wins.

### MRO in Multiple Inheritance

With multiple inheritance, there is no single path to the top.
Let's take a look at an example.

```python
class A: pass
class B: pass
class C(A, B): pass
class D(B): pass
class E(C, D): pass
```

What happens when you access an attribute?

```python
e = E()
e.attr
```

An attribute search process is carried out, but what is the order? That's a problem.

Python uses *cooperative multiple inheritance* which obeys some rules
about class ordering.

* Children are always checked before parents
* Parents (if multiple) are always checked in the order listed.

The MRO is computed by sorting all of the classes in a hierarchy
according to those rules.

```python
>>> E.__mro__
(
  <class 'E'>,
  <class 'C'>,
  <class 'A'>,
  <class 'D'>,
  <class 'B'>,
  <class 'object'>)
>>>
```

The underlying algorithm is called the "C3 Linearization Algorithm."
The precise details aren't important as long as you remember that a
class hierarchy obeys the same ordering rules you might follow if your
house was on fire and you had to evacuate--children first, followed by
parents.

### An Odd Code Reuse (Involving Multiple Inheritance)

Consider two completely unrelated objects:

```python
class Dog:
    def noise(self):
        return 'Bark'

    def chase(self):
        return 'Chasing!'

class LoudDog(Dog):
    def noise(self):
        # Code commonality with LoudBike (below)
        return super().noise().upper()
```

And

```python
class Bike:
    def noise(self):
        return 'On Your Left'

    def pedal(self):
        return 'Pedaling!'

class LoudBike(Bike):
    def noise(self):
        # Code commonality with LoudDog (above)
        return super().noise().upper()
```

There is a code commonality in the implementation of `LoudDog.noise()` and
`LoudBike.noise()`.  In fact, the code is exactly the same.  Naturally,
code like that is bound to attract software engineers.

### The "Mixin" Pattern

The *Mixin* pattern is a class with a fragment of code.

```python
class Loud:
    def noise(self):
        return super().noise().upper()
```

This class is not usable in isolation.
It mixes with other classes via inheritance.

```python
class LoudDog(Loud, Dog):
    pass

class LoudBike(Loud, Bike):
    pass
```

Miraculously, loudness was now implemented just once and reused
in two completely unrelated classes.  This sort of trick is one
of the primary uses of multiple inheritance in Python.

### Why `super()`

Always use `super()` when overriding methods.

```python
class Loud:
    def noise(self):
        return super().noise().upper()
```

`super()` delegates to the *next class* on the MRO.

The tricky bit is that you don't know what it is.  You especially don't
know what it is if multiple inheritance is being used.

### Some Cautions

Multiple inheritance is a powerful tool. Remember that with power
comes responsibility.  Frameworks / libraries sometimes use it for
advanced features involving composition of components.  Now, forget
that you saw that.

## Exercises

In Section 4, you defined a class `Stock` that represented a holding of stock.
In this exercise, we will use that class.  Restart the interpreter and make a
few instances:

```python
>>> ================================ RESTART ================================
>>> from stock import Stock
>>> goog = Stock('GOOG',100,490.10)
>>> ibm  = Stock('IBM',50, 91.23)
>>>
```

### Exercise 5.1: Representation of Instances

At the interactive shell, inspect the underlying dictionaries of the
two instances you created:

```python
>>> goog.__dict__
... look at the output ...
>>> ibm.__dict__
... look at the output ...
>>>
```

### Exercise 5.2: Modification of Instance Data

Try setting a new attribute on one of the above instances:

```python
>>> goog.date = '6/11/2007'
>>> goog.__dict__
... look at output ...
>>> ibm.__dict__
... look at output ...
>>>
```

In the above output, you'll notice that the `goog` instance has a
attribute `date` whereas the `ibm` instance does not.  It is important
to note that Python really doesn't place any restrictions on
attributes.  For example, the attributes of an instance are not
limited to those set up in the `__init__()` method.

Instead of setting an attribute, try placing a new value directly into
the `__dict__` object:

```python
>>> goog.__dict__['time'] = '9:45am'
>>> goog.time
'9:45am'
>>>
```

Here, you really notice the fact that an instance is just a layer on
top of a dictionary.  Note: it should be emphasized that direct
manipulation of the dictionary is uncommon--you should always write
your code to use the (.) syntax.

### Exercise 5.3: The role of classes

The definitions that make up a class definition are shared by all
instances of that class.  Notice, that all instances have a link back
to their associated class:

```python
>>> goog.__class__
... look at output ...
>>> ibm.__class__
... look at output ...
>>>
```

Try calling a method on the instances:

```python
>>> goog.cost()
49010.0
>>> ibm.cost()
4561.5
>>>
```

Notice that the name 'cost' is not defined in either `goog.__dict__`
or `ibm.__dict__`.  Instead, it is being supplied by the class
dictionary.  Try this:

```python
>>> Stock.__dict__['cost']
... look at output ...
>>>
```

Try calling the `cost()` method directly through the dictionary:

```python
>>> Stock.__dict__['cost'](goog)
49010.0
>>> Stock.__dict__['cost'](ibm)
4561.5
>>>
```

Notice how you are calling the function defined in the class
definition and how the `self` argument gets the instance.

Try adding a new attribute to the `Stock` class:

```python
>>> Stock.foo = 42
>>>
```

Notice how this new attribute now shows up on all of the instances:

```python
>>> goog.foo
42
>>> ibm.foo
42
>>>
```

However, notice that it is not part of the instance dictionary:

```python
>>> goog.__dict__
... look at output and notice there is no 'foo' attribute ...
>>>
```

The reason you can access the `foo` attribute on instances is that
Python always checks the class dictionary if it can't find something
on the instance itself.

Note: This part of the exercise illustrates something known as a class
variable.  Suppose, for instance, you have a class like this:

```python
class Foo(object):
     a = 13                  # Class variable
     def __init__(self,b):
         self.b = b          # Instance variable
```

In this class, the variable `a`, assigned in the body of the
class itself, is a "class variable."  It is shared by all of the
instances that get created.  For example:

```python
>>> f = Foo(10)
>>> g = Foo(20)
>>> f.a          # Inspect the class variable (same for both instances)
13
>>> g.a
13
>>> f.b          # Inspect the instance variable (differs)
10
>>> g.b
20
>>> Foo.a = 42   # Change the value of the class variable
>>> f.a
42
>>> g.a
42
>>>
```

### Exercise 5.4: Bound methods

A subtle feature of Python is that invoking a method actually involves
two steps and something known as a bound method.   For example:

```python
>>> s = goog.sell
>>> s
<bound method Stock.sell of Stock('GOOG', 100, 490.1)>
>>> s(25)
>>> goog.shares
75
>>>
```

Bound methods actually contain all of the pieces needed to call a
method.  For instance, they keep a record of the function implementing
the method:

```python
>>> s.__func__
<function sell at 0x10049af50>
>>>
```

This is the same value as found in the `Stock` dictionary.

```python
>>> Stock.__dict__['sell']
<function sell at 0x10049af50>
>>>
```

Bound methods also record the instance, which is the `self`
argument.

```python
>>> s.__self__
Stock('GOOG',75,490.1)
>>>
```

When you invoke the function using `()` all of the pieces come
together.  For example, calling `s(25)` actually does this:

```python
>>> s.__func__(s.__self__, 25)    # Same as s(25)
>>> goog.shares
50
>>>
```

### Exercise 5.5: Inheritance

Make a new class that inherits from `Stock`.

```
>>> class NewStock(Stock):
        def yow(self):
            print('Yow!')

>>> n = NewStock('ACME', 50, 123.45)
>>> n.cost()
6172.50
>>> n.yow()
Yow!
>>>
```

Inheritance is implemented by extending the search process for attributes.
The `__bases__` attribute has a tuple of the immediate parents:

```python
>>> NewStock.__bases__
(<class 'stock.Stock'>,)
>>>
```

The `__mro__` attribute has a tuple of all parents, in the order that
they will be searched for attributes.

```python
>>> NewStock.__mro__
(<class '__main__.NewStock'>, <class 'stock.Stock'>, <class 'object'>)
>>>
```

Here's how the `cost()` method of instance `n` above would be found:

```python
>>> for cls in n.__class__.__mro__:
        if 'cost' in cls.__dict__:
            break

>>> cls
<class '__main__.Stock'>
>>> cls.__dict__['cost']
<function cost at 0x101aed598>
>>>
```

[Contents](../Contents.md) \| [Previous (4.4 Exceptions)](../04_Classes_objects/04_Defining_exceptions.md) \| [Next (5.2 Encapsulation)](02_Classes_encapsulation.md)
