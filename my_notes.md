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