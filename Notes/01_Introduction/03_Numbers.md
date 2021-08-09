[Contents](../Contents.md) \| [Previous (1.2 A First Program)](02_Hello_world.md) \| [Next (1.4 Strings)](04_Strings.md)

# 1.3 Numbers

This section discusses mathematical calculations.

### Types of Numbers

Python has 4 types of numbers:

* Booleans
* Integers
* Floating point
* Complex (imaginary numbers)

### Booleans (bool)

Booleans have two values: `True`, `False`.

```python
a = True
b = False
```

Numerically, they're evaluated as integers with value `1`, `0`.

```python
c = 4 + True # 5
d = False
if d == 0:
    print('d is False')
```

*But, don't write code like that. It would be odd.*

### Integers (int)

Signed values of arbitrary size and base:

```python
a = 37
b = -299392993727716627377128481812241231
c = 0x7fa8      # Hexadecimal
d = 0o253       # Octal
e = 0b10001111  # Binary
```

Common operations:

```
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

### Floating point (float)

Use a decimal or exponential notation to specify a floating point value:

```python
a = 37.45
b = 4e5 # 4 x 10**5 or 400,000
c = -1.345e-10
```

Floats are represented as double precision using the native CPU representation [IEEE 754](https://en.wikipedia.org/wiki/IEEE_754).
This is the same as the `double` type in the programming language C.

> 17 digits of precision  
> Exponent from -308 to 308

Be aware that floating point numbers are inexact when representing decimals.

```python
>>> a = 2.1 + 4.2
>>> a == 6.3
False
>>> a
6.300000000000001
>>>
```

This is **not a Python issue**, but the underlying floating point hardware on the CPU.

Common Operations:

```
x + y      Add
x - y      Subtract
x * y      Multiply
x / y      Divide
x // y     Floor Divide
x % y      Modulo
x ** y     Power
abs(x)     Absolute Value
```

These are the same operators as Integers, except for the bit-wise operators.
Additional math functions are found in the `math` module.

```python
import math
a = math.sqrt(x)
b = math.sin(x)
c = math.cos(x)
d = math.tan(x)
e = math.log(x)
```


### Comparisons

The following comparison / relational operators work with numbers:

```
x < y      Less than
x <= y     Less than or equal
x > y      Greater than
x >= y     Greater than or equal
x == y     Equal to
x != y     Not equal to
```

You can form more complex boolean expressions using

`and`, `or`, `not`

Here are a few examples:

```python
if b >= a and b <= c:
    print('b is between a and c')

if not (b < a or b > c):
    print('b is still between a and c')
```

### Converting Numbers

The type name can be used to convert values:

```python
a = int(x)    # Convert x to integer
b = float(x)  # Convert x to float
```

Try it out.

```python
>>> a = 3.14159
>>> int(a)
3
>>> b = '3.14159' # It also works with strings containing numbers
>>> float(b)
3.14159
>>>
```

## Exercises

Reminder: These exercises assume you are working in the `practical-python/Work` directory. Look
for the file `mortgage.py`.

### Exercise 1.7: Dave's mortgage

Dave has decided to take out a 30-year fixed rate mortgage of $500,000
with Guido’s Mortgage, Stock Investment, and Bitcoin trading
corporation.  The interest rate is 5% and the monthly payment is
$2684.11.

Here is a program that calculates the total amount that Dave will have
to pay over the life of the mortgage:

```python
# mortgage.py

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0

while principal > 0:
    principal = principal * (1+rate/12) - payment
    total_paid = total_paid + payment

print('Total paid', total_paid)
```

Enter this program and run it. You should get an answer of `966,279.6`.

### Exercise 1.8: Extra payments

Suppose Dave pays an extra $1000/month for the first 12 months of the mortgage?

Modify the program to incorporate this extra payment and have it print the total amount paid along with the number of months required.

When you run the new program, it should report a total payment of `929,965.62` over 342 months.

### Exercise 1.9: Making an Extra Payment Calculator

Modify the program so that extra payment information can be more generally handled.
Make it so that the user can set these variables:

```python
extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000
```

Make the program look at these variables and calculate the total paid appropriately.

How much will Dave pay if he pays an extra $1000/month for 4 years starting after the first
five years have already been paid?

### Exercise 1.10: Making a table

Modify the program to print out a table showing the month, total paid so far, and the remaining principal.
The output should look something like this:

```bash
1 2684.11 499399.22
2 5368.22 498795.94
3 8052.33 498190.15
4 10736.44 497581.83
5 13420.55 496970.98
...
308 874705.88 3478.83
309 877389.99 809.21
310 880074.1 -1871.53
Total paid 880074.1
Months 310
```

### Exercise 1.11: Bonus

While you’re at it, fix the program to correct for the overpayment that occurs in the last month.

### Exercise 1.12: A Mystery

`int()` and `float()` can be used to convert numbers.  For example,

```python
>>> int("123")
123
>>> float("1.23")
1.23
>>>
```

With that in mind, can you explain this behavior?

```python
>>> bool("False")
True
>>>
```

[Contents](../Contents.md) \| [Previous (1.2 A First Program)](02_Hello_world.md) \| [Next (1.4 Strings)](04_Strings.md)
