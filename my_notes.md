# Notes

## 01_Introduction

* '_' can be used in interactive mode to access the value evaluated in the last line.
* Suppressing the newline after print():
    ```py
    print(abc, end='')
    ```
* To specify an empty code block:
    ```py
    if a > b:
        pass
    ```
* Python has 4 types of numbers:
    * Booleans
    * Integers
    * Floating point
    * Complex (imaginary numbers)
* Numerically, 'True' is evaluated as 1 and 'False' as 0.
* Integer examples:
    ```py
    a = 142
    b = 0x324 # hexadecimal
    c = 0o234 # octal
    d = 0b01101 # binary
    ```
* Operations:
    ```py
    x + y      Add
    x - y      Subtract
    x * y      Multiply
    x / y      Divide (produces a float)
    x // y     Floor Divide (produces an integer)
    x % y      Modulo (remainder)
    x ** y     Power
    x << n     Bit shift left
    x >> n     Bit shift right
    x & y      Bit-wise AND
    x | y      Bit-wise OR
    x ^ y      Bit-wise XOR
    ~x         Bit-wise NOT
    abs(x)     Absolute value
    ```
* Python 'float' is the same as 'double' in C. 
* Triple quotes (''') capture all text enclosed across multiple lines including all formatting.
* String escape codes:
    ```
    '\n'      Line feed
    '\r'      Carriage return. It takes the cursor to the beginning of the line, overwriting everything in the line.
    '\t'      Tab
    '\''      Literal single quote
    '\"'      Literal double quote
    '\\'      Literal backslash
    ```
* 
    ```py
    a = 'Hello world!'
    print(a[-6:]) # 'world!'
    ```
* String membership test
    ```py
    s = 'are'
    t = 'e' in s       # True
    g = 'q' not in s   # True
    ```
* s.strip() strips any leading or trailing whitespace.
* Replaces all instance of the first string with the second string.
    ```py
    s = 'Hello adf Hello adsfHelloHello'
    t = s.replace('Hello' , 'Hallo')   # 'Hallo adf Hallo adsfHalloHallo'
    ```
* String methods:
    ```
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
* The index() method is similar to find() method for strings. The only difference is that find() method returns -1 if the substring is not found, whereas index() throws an exception.
* Strings are **immutable** or read-only. All operations and methods that manipulate string data, always create new strings.
* str(x) conversts any value to a string.
* Byte strings: A string of 8 bit bytes.
    ```py
    data = b'Hello World\r\n'
    len(data)                         # 13
    data[0:5]                         # b'Hello'
    data.replace(b'Hello', b'Cruel')  # b'Cruel World\r\n'
    text = data.decode('utf-8') # bytes -> text
    data = text.encode('utf-8') # text -> bytes
    ```
* Raw strings are string literals with uniterpreted backslash. Useful for filenames, regex, etc.
    ```py
    a = r'asdf\saf\sdf'
    ```
* f-Strings have formatted expression substitution.
    ```py
    name = "Ashwin"
    age = "21"
    print(f'Name: {name} Age: {age})
    print(f'{1+2}') # 3
    ```