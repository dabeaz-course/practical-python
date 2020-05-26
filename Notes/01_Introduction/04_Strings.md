# 1.4 Strings

This section covers the basics of text manipulation.

### Representing Text

String are text literals written in programs with quotes.

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

Triple quotes capture all text enclosed in multiple lines.

### String escape codes

Escape codes are used to represent control characters and characters that can't be easily typed
at the keyboard.  Here are some common escape codes:

```
'\n'      Line feed
'\r'      Carriage return
'\t'      Tab
'\''      Literal single quote
'\"'      Literal double quote
'\\'`     Literal backslash
```

### String Representation

Each character represents a raw unicode code point.

<!-- TODO: Add Picture of following characters -->

```python
a = '\xf1'          # a = 'ñ'
b = '\u2200'        # b = '∀'
c = '\U0001D122'    # c = '𝄢'
d = '\N{FORALL}'    # d = '∀'
```

Strings work like an array for accessing its characters. You use an integer index, starting at 0.

```python
a = 'Hello world'
b = a[0]          # 'H'
c = a[4]          # 'o'
d = a[-1]         # 'd' (end of string)
```

You can also slice or select substrings with `:`.

```python
d = a[:5]     # 'Hello'
e = a[6:]     # 'world'
f = a[3:8]    # 'lowo'
g = a[-5:]    # 'world'
```

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
tt = 'hi' not in s      # True

# Replication (s * n)
rep = s * 5             # 'HelloHelloHelloHelloHello'
```

### String methods

Strings have methods that perform various operations with the string data.

Stripping any leading / trailing white space.

```python
s = '  Hello '
t = s.strip()     # 'Hello'
```

Case conversion.

```python
s = 'Hello'
l = s.lower()     # 'hello'
u = s.upper()     # 'HELLO'
```

Replacing text.

```python
s = 'Hello world'
t = s.replace('Hello' , 'Hallo')   # 'Hallo world'
```

**More string methods:**

Strings have a wide variety of other methods for testing and manipulating the text data:

```python
s.endswith(suffix)     # Check if string ends with suffix
s.find(t)              # First occurrence of t in s
s.index(t)             # First occurrence of t in s
s.isalpha()            # Check if characters are alphabetic
s.isdigit()            # Check if characters are numeric
s.islower()            # Check if characters are lower-case
s.isupper()            # Check if characters are upper-case
s.join(slist)          # Joins lists using s as delimiter
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

Use `str()` to convert a value to a string.

```python
>>> x = 42
>>> str(x)
'42'
>>>
```

### Byte Strings

A string of 8-bit bytes.

```python
data = b'Hello World\r\n'
```

By putting a little b before our string literal we specify that it is a byte string as opposed to a text string.

Most of the usual string operations work.

```python
len(data)                         # 13
data[0:5]                         # b'Hello'
data.replace(b'Hello', b'Cruel')  # b'Cruel World\r\n'
```

Indexing is a bit different because it returns byte values.

```python
data[0]   # 72 (ASCII code for 'H')
```

Conversion to/from text.

```python
text = data.decode('utf-8') # bytes -> text
data = text.encode('utf-8') # text -> bytes
```

### Raw Strings

Raw strings are strings with uninterpreted backslash.  They are little by prefixing the initial quote with a lowercase "r".

```python
>>> rs = r'c:\newdata\test' # Raw (uninterpreted backslash)
>>> rs
'c:\\newdata\\test'
```

The string is the literal text, exactly as typed.
This is useful in situations where the backslash has special significance. Example: filename, regular expressions, etc.

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

**Note: This requires Python 3.6 or newer.**

## Exercises


In this exercise, we experiment with operations on Python's string type.
You may want to do most of this exercise at the Python interactive prompt where you can easily see the results.
Important note:

> In exercises where you are supposed to interact with the interpreter,
> `>>>` is the interpreter prompt that you get when Python wants
> you to type a new statement.  Some statements in the exercise span
> multiple lines--to get these statements to run, you may have to hit
> 'return' a few times.  Just a reminder that you *DO NOT* type
> the `>>>` when working these examples.

Start by defining a string containing a series of stock ticker symbols like this:

```pycon
>>> symbols = 'AAPL,IBM,MSFT,YHOO,SCO'
>>>
```

### (a): Extracting individual characters and substrings

Strings are arrays of characters. Try extracting a few characters:

```pycon
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

### (b) Strings as read-only objects

In Python, strings are read-only.

Verify this by trying to change the first character of `symbols` to a lower-case 'a'.

```python
>>> symbols[0] = 'a'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object does not support item assignment
>>> 
```

### (c) String concatenation

Although string data is read-only, you can always reassign a variable
to a newly created string.

Try the following statement which concatenates a new symbol "GOOG" to
the end of `symbols`:

```pycon
>>> symbols = symbols + 'GOOG'
>>> symbols
'AAPL,IBM,MSFT,YHOO,SCOGOOG'
>>>
```

Oops!  That's not what we wanted. Fix it so that the `symbols` variable holds the value `'HPQ,AAPL,IBM,MSFT,YHOO,SCO,GOOG'`.

In these examples, it might look like the original string is being
modified, in an apparent violation of strings being read only.  Not
so. Operations on strings create an entirely new string each
time. When the variable name `symbols` is reassigned, it points to the
newly created string.  Afterwards, the old string is destroyed since
it's not being used anymore.

### (d) Membership testing (substring testing)

Experiment with the `in` operator to check for substrings.  At the interactive prompt, try these operations:

```pycon
>>> 'IBM' in symbols
?
>>> 'AA' in symbols
?
>>> 'CAT' in symbols
?
>>>
```

*Why did the check for "AA" return `True`?*

### (e) String Methods

At the Python interactive prompt, try experimenting with some of the string methods.

```pycon
>>> symbols.lower()
?
>>> symbols
?
>>>
```

Remember, strings are always read-only.  If you want to save the result of an operation, you need to place it in a variable:

```pycon
>>> lowersyms = symbols.lower()
>>>
```

Try some more operations:

```pycon
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

### (f) f-strings

Sometimes you want to create a string and embed the values of
variables into it.

To do that, use an f-string. For example:

```pycon
>>> name = 'IBM'
>>> shares = 100
>>> price = 91.1
>>> f'{shares} shares of {name} at ${price:0.2f}'
'100 shares of IBM at $91.10'
>>> 
```

Modify the `mortgage.py` program from Exercise 1.3 to create its output using f-strings.
Try to make it so that output is nicely aligned.

### Commentary

As you start to experiment with the interpreter, you often want to know more about the operations supported by different objects.
For example, how do you find out what operations are available on a string?

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
['__add__', '__class__', '__contains__', ..., 'find', 'format', 'index', 'isalnum', 'isalpha', 'isdigit', 'islower', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
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

IDEs and alternative interactive shells often give you more help here.
For example, a popular alternative to Python's normal interactive mode
is IPython (http://ipython.org).  IPython provides some nice features
such as tab-completion of method names, more integrated help and more.

[Contents](../Contents) \| [Previous (1.3 Numbers)](03_Numbers) \| [Next (1.5 Lists)](05_Lists)
