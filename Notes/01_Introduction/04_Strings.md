[Contents](../Contents.md) \| [Previous (1.3 Numbers)](03_Numbers.md) \| [Next (1.5 Lists)](05_Lists.md)

# 1.4 Strings

This section introduces ways to work with text.

### Representing Literal Text

String literals are written in programs with quotes.

```python
# Single quote
a = 'Yeah but no but yeah but...'

# Double quote
b = "computer says no"

# Triple quotes
c = '''
Look into my eyes, look into my eyes, the eyes, the eyes, the eyes,
not around the eyes,
don't look around the eyes,
look into my eyes, you're under.
'''
```

Normally strings may only span a single line. Triple quotes capture all text enclosed across multiple lines
including all formatting.

There is no difference between using single (') versus double (")
quotes. *However, the same type of quote used to start a string must be used to
terminate it*.

### String escape codes

Escape codes are used to represent control characters and characters that can't be easily typed
directly at the keyboard.  Here are some common escape codes:

```
'\n'      Line feed
'\r'      Carriage return
'\t'      Tab
'\''      Literal single quote
'\"'      Literal double quote
'\\'      Literal backslash
```

### String Representation

Each character in a string is stored internally as a so-called Unicode "code-point" which is
an integer.  You can specify an exact code-point value using the following escape sequences:

```python
a = '\xf1'          # a = 'ñ'
b = '\u2200'        # b = '∀'
c = '\U0001D122'    # c = '𝄢'
d = '\N{FOR ALL}'   # d = '∀'
```

The [Unicode Character Database](https://unicode.org/charts) is a reference for all
available character codes.

### String Indexing

Strings work like an array for accessing individual characters. You use an integer index, starting at 0.
Negative indices specify a position relative to the end of the string.

```python
a = 'Hello world'
b = a[0]          # 'H'
c = a[4]          # 'o'
d = a[-1]         # 'd' (end of string)
```

You can also slice or select substrings specifying a range of indices with `:`.

```python
d = a[:5]     # 'Hello'
e = a[6:]     # 'world'
f = a[3:8]    # 'lo wo'
g = a[-5:]    # 'world'
```

The character at the ending index is not included.  Missing indices assume the beginning or ending of the string.

### String operations

Concatenation, length, membership and replication.

```python
# Concatenation (+)
a = 'Hello' + 'World'   # 'HelloWorld'
b = 'Say ' + a          # 'Say HelloWorld'

# Length (len)
s = 'Hello'
len(s)                  # 5

# Membership test (`in`, `not in`)
t = 'e' in s            # True
f = 'x' in s            # False
g = 'hi' not in s       # True

# Replication (s * n)
rep = s * 5             # 'HelloHelloHelloHelloHello'
```

### String methods

Strings have methods that perform various operations with the string data.

Example: stripping any leading / trailing white space.

```python
s = '  Hello '
t = s.strip()     # 'Hello'
```

Example: Case conversion.

```python
s = 'Hello'
l = s.lower()     # 'hello'
u = s.upper()     # 'HELLO'
```

Example: Replacing text.

```python
s = 'Hello world'
t = s.replace('Hello' , 'Hallo')   # 'Hallo world'
```

**More string methods:**

Strings have a wide variety of other methods for testing and manipulating the text data.
This is a small sample of methods:

```python
s.endswith(suffix)     # Check if string ends with suffix
s.find(t)              # First occurrence of t in s
s.index(t)             # First occurrence of t in s
s.isalpha()            # Check if characters are alphabetic
s.isdigit()            # Check if characters are numeric
s.islower()            # Check if characters are lower-case
s.isupper()            # Check if characters are upper-case
s.join(slist)          # Join a list of strings using s as delimiter
s.lower()              # Convert to lower case
s.replace(old,new)     # Replace text
s.rfind(t)             # Search for t from end of string
s.rindex(t)            # Search for t from end of string
s.split([delim])       # Split string into list of substrings
s.startswith(prefix)   # Check if string starts with prefix
s.strip()              # Strip leading/trailing space
s.upper()              # Convert to upper case
```

### String Mutability

Strings are "immutable" or read-only.
Once created, the value can't be changed.

```python
>>> s = 'Hello World'
>>> s[1] = 'a'
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
TypeError: 'str' object does not support item assignment
>>>
```

**All operations and methods that manipulate string data, always create new strings.**

### String Conversions

Use `str()` to convert any value to a string. The result is a string holding the
same text that would have been produced by the `print()` statement.

```python
>>> x = 42
>>> str(x)
'42'
>>>
```

### Byte Strings

A string of 8-bit bytes, commonly encountered with low-level I/O, is written as follows:

```python
data = b'Hello World\r\n'
```

By putting a little b before the first quotation, you specify that it is a byte string as opposed to a text string.

Most of the usual string operations work.

```python
len(data)                         # 13
data[0:5]                         # b'Hello'
data.replace(b'Hello', b'Cruel')  # b'Cruel World\r\n'
```

Indexing is a bit different because it returns byte values as integers.

```python
data[0]   # 72 (ASCII code for 'H')
```

Conversion to/from text strings.

```python
text = data.decode('utf-8') # bytes -> text
data = text.encode('utf-8') # text -> bytes
```

The `'utf-8'` argument specifies a character encoding.  Other common
values include `'ascii'` and `'latin1'`.

### Raw Strings

Raw strings are string literals with an uninterpreted backslash. They
are specified by prefixing the initial quote with a lowercase "r".

```python
>>> rs = r'c:\newdata\test' # Raw (uninterpreted backslash)
>>> rs
'c:\\newdata\\test'
```

The string is the literal text enclosed inside, exactly as typed.
This is useful in situations where the backslash has special
significance. Example: filename, regular expressions, etc.

### f-Strings

A string with formatted expression substitution.

```python
>>> name = 'IBM'
>>> shares = 100
>>> price = 91.1
>>> a = f'{name:>10s} {shares:10d} {price:10.2f}'
>>> a
'       IBM        100      91.10'
>>> b = f'Cost = ${shares*price:0.2f}'
>>> b
'Cost = $9110.00'
>>>
```

**Note: This requires Python 3.6 or newer.**  The meaning of the format codes
is covered later.

## Exercises

In these exercises, you'll experiment with operations on Python's
string type.  You should do this at the Python interactive prompt
where you can easily see the results.  Important note:

> In exercises where you are supposed to interact with the interpreter,
> `>>>` is the interpreter prompt that you get when Python wants
> you to type a new statement.  Some statements in the exercise span
> multiple lines--to get these statements to run, you may have to hit
> 'return' a few times.  Just a reminder that you *DO NOT* type
> the `>>>` when working these examples.

Start by defining a string containing a series of stock ticker symbols like this:

```python
>>> symbols = 'AAPL,IBM,MSFT,YHOO,SCO'
>>>
```

### Exercise 1.13: Extracting individual characters and substrings

Strings are arrays of characters. Try extracting a few characters:

```python
>>> symbols[0]
?
>>> symbols[1]
?
>>> symbols[2]
?
>>> symbols[-1]        # Last character
?
>>> symbols[-2]        # Negative indices are from end of string
?
>>>
```

In Python, strings are read-only.

Verify this by trying to change the first character of `symbols` to a lower-case 'a'.

```python
>>> symbols[0] = 'a'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object does not support item assignment
>>>
```

### Exercise 1.14: String concatenation

Although string data is read-only, you can always reassign a variable
to a newly created string.

Try the following statement which concatenates a new symbol "GOOG" to
the end of `symbols`:

```python
>>> symbols = symbols + 'GOOG'
>>> symbols
'AAPL,IBM,MSFT,YHOO,SCOGOOG'
>>>
```

Oops!  That's not what you wanted. Fix it so that the `symbols` variable holds the value `'AAPL,IBM,MSFT,YHOO,SCO,GOOG'`.

```python
>>> symbols = ?
>>> symbols
'AAPL,IBM,MSFT,YHOO,SCO,GOOG'
>>>
```

Add `'HPQ'` to the front the string:

```python
>>> symbols = ?
>>> symbols
'HPQ,AAPL,IBM,MSFT,YHOO,SCO,GOOG'
>>>
```

In these examples, it might look like the original string is being
modified, in an apparent violation of strings being read only.  Not
so. Operations on strings create an entirely new string each
time. When the variable name `symbols` is reassigned, it points to the
newly created string.  Afterwards, the old string is destroyed since
it's not being used anymore.

### Exercise 1.15: Membership testing (substring testing)

Experiment with the `in` operator to check for substrings.  At the
interactive prompt, try these operations:

```python
>>> 'IBM' in symbols
?
>>> 'AA' in symbols
True
>>> 'CAT' in symbols
?
>>>
```

*Why did the check for `'AA'` return `True`?*

### Exercise 1.16: String Methods

At the Python interactive prompt, try experimenting with some of the string methods.

```python
>>> symbols.lower()
?
>>> symbols
?
>>>
```

Remember, strings are always read-only.  If you want to save the result of an operation, you need to place it in a variable:

```python
>>> lowersyms = symbols.lower()
>>>
```

Try some more operations:

```python
>>> symbols.find('MSFT')
?
>>> symbols[13:17]
?
>>> symbols = symbols.replace('SCO','DOA')
>>> symbols
?
>>> name = '   IBM   \n'
>>> name = name.strip()    # Remove surrounding whitespace
>>> name
?
>>>
```

### Exercise 1.17: f-strings

Sometimes you want to create a string and embed the values of
variables into it.

To do that, use an f-string. For example:

```python
>>> name = 'IBM'
>>> shares = 100
>>> price = 91.1
>>> f'{shares} shares of {name} at ${price:0.2f}'
'100 shares of IBM at $91.10'
>>>
```

Modify the `mortgage.py` program from [Exercise 1.10](03_Numbers.md) to create its output using f-strings.
Try to make it so that output is nicely aligned.


### Exercise 1.18: Regular Expressions

One limitation of the basic string operations is that they don't
support any kind of advanced pattern matching.  For that, you
need to turn to Python's `re` module and regular expressions.
Regular expression handling is a big topic, but here is a short
example:

```python
>>> text = 'Today is 3/27/2018. Tomorrow is 3/28/2018.'
>>> # Find all occurrences of a date
>>> import re
>>> re.findall(r'\d+/\d+/\d+', text)
['3/27/2018', '3/28/2018']
>>> # Replace all occurrences of a date with replacement text
>>> re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\1-\2', text)
'Today is 2018-3-27. Tomorrow is 2018-3-28.'
>>>
```

For more information about the `re` module, see the official documentation at
[https://docs.python.org/library/re.html](https://docs.python.org/3/library/re.html).


### Commentary

As you start to experiment with the interpreter, you often want to
know more about the operations supported by different objects.  For
example, how do you find out what operations are available on a
string?

Depending on your Python environment, you might be able to see a list
of available methods via tab-completion.  For example, try typing
this:

```python
>>> s = 'hello world'
>>> s.<tab key>
>>>
```

If hitting tab doesn't do anything, you can fall back to the
builtin-in `dir()` function.  For example:

```python
>>> s = 'hello'
>>> dir(s)
['__add__', '__class__', '__contains__', ..., 'find', 'format',
'index', 'isalnum', 'isalpha', 'isdigit', 'islower', 'isspace',
'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'partition',
'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit',
'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase',
'title', 'translate', 'upper', 'zfill']
>>>
```

`dir()` produces a list of all operations that can appear after the `(.)`.
Use the `help()` command to get more information about a specific operation:

```python
>>> help(s.upper)
Help on built-in function upper:

upper(...)
    S.upper() -> string

    Return a copy of the string S converted to uppercase.
>>>
```

[Contents](../Contents.md) \| [Previous (1.3 Numbers)](03_Numbers.md) \| [Next (1.5 Lists)](05_Lists.md)
