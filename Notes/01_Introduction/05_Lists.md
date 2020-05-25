# 1.5 Lists

This section introduces lists, one of Python's basic objects for storing collections of data.

### Creating a List

Use square brackets to create a list:

```python
names = [ 'Elwood', 'Jake', 'Curtis' ]
nums = [ 39, 38, 42, 65, 111]
```

Sometimes lists are created by other methods.  For example, a string can be split into a
list using the `split()` method:

```pycon
>>> line = 'GOOG,100,490.10'
>>> row = line.split(',')
>>> row
['GOOG', '100', '490.10']
>>>
```

### List operations

Lists can hold items of any type. Add a new item using `append()`:

```python
names.append('Murphy')    # Adds at end
names.insert(2, 'Aretha') # Inserts in middle
```

Use `+` to concatenate lists:

```python
s = [1, 2, 3]
t = ['a', 'b']
s + t           # [1, 2, 3, 'a', 'b']
```

Lists are indexed by integers. Starting at 0.

```python
names = [ 'Elwood', 'Jake', 'Curtis' ]

names[0]  # 'Elwood'
names[1]  # 'Jake'
names[2]  # 'Curtis'
```

Negative indices count from the end.

```python
names[-1] # 'Curtis'
```

You can change on element in the list.

```python
names[1] = 'Joliet Jake'
names                     # [ 'Elwood', 'Joliet Jake', 'Curtis' ]
```

Length of the list.

```python
names = ['Elwood','Jake','Curtis']
len(names)  # 3
```

Membership test (`in`, `not in`).

```python
'Elwood' in names       # True
'Britney' not in names  # True
```

Replication (`s * n`).

```python
s = [1, 2, 3]
s * 3   # [1, 2, 3, 1, 2, 3, 1, 2, 3]
```

### List Iteration and Search

Iterating over the list contents.

```python
for name in names:
    # use name
    # e.g. print(name)
    ...
```

This is similar to a `foreach` statement from other programming languages.

To find something quickly, use `index()`. 

```python
names = ['Elwood','Jake','Curtis']
names.index('Curtis')   # 2
```

If the element is present more than one, it will return the index of the first occurrence.

If the element is not found, it will raise a `ValueError` exception.

### List Removal

You can remove either with the element value or the index number.

```python
# Using the value
names.remove('Curtis')

# Using the index
del names[1]
```

Removing results in items moving down to fill the space vacated. There are no holes in the list.
If there are more than one occurrence of the element, `.remove()` will remove only the first occurrence.

### List Sorting

Lists can be sorted 'in-place'.

```python
s = [10, 1, 7, 3]
s.sort()                    # [1, 3, 7, 10]

# Reverse order
s = [10, 1, 7, 3]
s.sort(reverse=True)        # [10, 7, 3, 1]

# It works with any ordered data
s = ['foo', 'bar', 'spam']
s.sort()                    # ['bar', 'foo', 'spam']
```

### Lists and Math

*Caution: Lists were not designed for math operations.*

```pycon
>>> nums = [1, 2, 3, 4, 5]
>>> nums * 2
[1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
>>> nums + [10, 11, 12, 13, 14]
[1, 2, 3, 4, 5, 10, 11, 12, 13, 14] >>>
```

Specifically, lists don't represent vectors/matrices as in MATLAB, Octave, IDL, etc.
However, there are some packages to help you with that (e.g. numpy).

## Exercises

In this exercise, we experiment with Python's list datatype. In the last exercise, you worked with strings containing stock symbols.

```pycon
>>> symbols = 'HPQ,AAPL,IBM,MSFT,YHOO,DOA,GOOG'
```

Split it into a list of names using the `split()` operation of strings:

```pycon
>>> symlist = symbols.split(',')
```

### (a) Extracting and reassigning list elements

Try a few lookups:

```python
>>> symlist[0]
'HPQ'
>>> symlist[1]
'AAPL'
>>> symlist[-1]
'GOOG'
>>> symlist[-2]
'DOA'
>>>
```

Try reassigning one value:

```python
>>> symlist[2] = 'AIG'
>>> symlist
['HPQ', 'AAPL', 'AIG', 'MSFT', 'YHOO', 'DOA', 'GOOG']
>>>
```

Take a few slices:

```python
>>> symlist[0:3]
['HPQ', 'AAPL', 'AIG']
>>> symlist[-2:]
['DOA', 'GOOG']
>>>
```

Create an empty list and append an item to it.

```python
>>> mysyms = []
>>> mysyms.append('GOOG')
>>> mysyms
['GOOG']
```

You can reassign a portion of a list to another list. For example:

```python
>>> symlist[-2:] = mysyms
>>> symlist
['HPQ', 'AAPL', 'AIG', 'MSFT', 'YHOO', 'GOOG']
>>>
```

When you do this, the list on the left-hand-side (`symlist`) will be resized as appropriate to make the right-hand-side (`mysyms`) fit.
For instance, in the above example, the last two items of `symlist` got replaced by the single item in the list `mysyms`.

### (b) Looping over list items

The `for` loop works by looping over data in a sequence such as a list.
Check this out by typing the following loop and watching what happens:

```pycon
>>> for s in symlist:
        print('s =', s)
# Look at the output
```

### (c) Membership tests

Use the `in` or `not in` operator to check if `'AIG'`,`'AA'`, and `'CAT'` are in the list of symbols.

```pycon
>>> # Is 'AIG' IN the `symlist`?
True
>>> # Is 'AA' IN the `symlist`?
False
>>> # Is 'CAT' NOT IN the `symlist`?
True
>>>
```

### (d) Appending, inserting, and deleting items

Use the `append()` method to add the symbol `'RHT'` to end of `symlist`.

```pycon
>>> # append 'RHT'
>>> symlist
['HPQ', 'AAPL', 'AIG', 'MSFT', 'YHOO', 'GOOG', 'RHT']
>>> 
```

Use the `insert()` method to insert the symbol `'AA'` as the second item in the list.

```pycon
>>> # Insert 'AA' as the second item in the list
>>> symlist
['HPQ', 'AA', 'AAPL', 'AIG', 'MSFT', 'YHOO', 'GOOG', 'RHT']
>>>
```

Use the `remove()` method to remove `'MSFT'` from the list.

```pycon
>>> # Remove 'MSFT'
>>> symlist
['HPQ', 'AA', 'AAPL', 'AIG', 'YHOO', 'GOOG', 'RHT']
>>>
```

Append a duplicate entry for `'YHOO'` at the end of the list.

*Note: it is perfectly fine for a list to have duplicate values.*

```pycon
>>> # Append 'YHOO'
>>> symlist
['HPQ', 'AA', 'AAPL', 'AIG', 'YHOO', 'GOOG', 'RHT', 'YHOO']
>>>
```

Use the `index()` method to find the first position of `'YHOO'` in the list.

```pycon
>>> # Find the first index of 'YHOO'
4
>>> symlist[4]
'YHOO'
>>>
```

Count how many times `'YHOO'` is in the list:

```pycon
>>> symlist.count('YHOO')
2
>>>
```

Remove the first occurrence of `'YHOO'`.

```pycon
>>> # Remove first occurrence 'YHOO'
>>> symlist
['HPQ', 'AA', 'AAPL', 'AIG', 'GOOG', 'RHT', 'YHOO']
>>>
```

Just so you know, there is no method to find or remove all occurrences of an item.
However, we'll see an elegant way to do this in section 2.

### (e) Sorting

Want to sort a list?  Use the `sort()` method. Try it out:

```pycon
>>> symlist.sort()
>>> symlist
['AA', 'AAPL', 'AIG', 'GOOG', 'HPQ', 'RHT', 'YHOO']
>>>
```

Want to sort in reverse? Try this:

```pycon
>>> symlist.sort(reverse=True)
>>> symlist
['YHOO', 'RHT', 'HPQ', 'GOOG', 'AIG', 'AAPL', 'AA']
>>>
```

Note: Sorting a list modifies its contents 'in-place'.  That is, the elements of the list are shuffled around, but no new list is created as a result.

### (f) Putting it all back together

Want to take a list of strings and join them together into one string?
Use the `join()` method of strings like this (note: this looks funny at first).

```pycon
>>> a = ','.join(symlist)
>>> a
'YHOO,RHT,HPQ,GOOG,AIG,AAPL,AA'
>>> b = ':'.join(symlist)
>>> b
'YHOO:RHT:HPQ:GOOG:AIG:AAPL:AA'
>>> c = ''.join(symlist)
>>> c
'YHOORHTHPQGOOGAIGAAPLAA'
>>>
```

### (g) Lists of anything

Lists can contain any kind of object, including other lists (e.g., nested lists).
Try this out:

```pycon
>>> nums = [101, 102, 103]
>>> items = ['spam', symlist, nums]
>>> items
['spam', ['YHOO', 'RHT', 'HPQ', 'GOOG', 'AIG', 'AAPL', 'AA'], [101, 102, 103]]
```

Pay close attention to the above output. `items` is a list with three elements.
The first element is a string, but the other two elements are lists.

You can access items in the nested lists by using multiple indexing operations.

```pycon
>>> items[0]
'spam'
>>> items[0][0]
's'
>>> items[1]
['YHOO', 'RHT', 'HPQ', 'GOOG', 'AIG', 'AAPL', 'AA']
>>> items[1][1]
'RHT'
>>> items[1][1][2]
'T'
>>> items[2]
[101, 102, 103]
>>> items[2][1]
102
>>>
```

Even though it is technically possible to make very complicated list
structures, as a general rule, you want to keep things simple.
Usually lists hold items that are all the same kind of value.  For
example, a list that consists entirely of numbers or a list of text
strings.  Mixing different kinds of data together in the same list is
often a good way to make your head explode so it's best avoided.

[Next](06_Files)