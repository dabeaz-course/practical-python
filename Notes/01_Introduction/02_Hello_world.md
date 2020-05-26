# 1.2 A First Python Program

This section discusses the creation of your first program, running the interpreter,
and some basic debugging.

### Running Python

Python programs run inside an interpreter.

The interpreter is a simple "console-based" application that normally starts from a command shell.

```bash
python3
Python 3.6.1 (v3.6.1:69c0db5050, Mar 21 2017, 01:21:04)
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

Expert programmers usually have no problem using the interpreter in
this way, but it's not so user-friendly for beginners.  That said,
you'll become a better Python programmer if you're able to use the
interpreter from the shell earlier rather than later.

### Interactive Mode

When you start Python, you get an *interactive* mode where you can experiment.

If you start typing statements, they will run immediately. There is no edit/compile/run/debug cycle.

```python
>>> print('hello world')
hello world
>>> 37*42
1554
>>> for i in range(5):
...     print(i)
...
0
1
2
3
4
>>>
```

This *read-eval* loop is very useful for debugging and exploration.

Let's take a closer look at the elements:

- `>>>` is the interpreter prompt for starting a new statement.
- `...` is the interpreter prompt for continuing a statements. Enter a blank like to finish typing and run the statements.

The `...` prompt may or may not be shown depending on how you are using Python.  For this course,
it is shown as blanks to make it easier to cut/paste code samples.

The underscore `_` holds the last result. 

```pycon
>>> 37 * 42
1554
>>> _ * 2
3108
>>> _ + 50
3158
>>>
```

*This is only true in the interactive mode.* You never use `_` in a program.


Type `help(command)` to get information about `command`.  Type `help()` with no name for interactive help.

```code
>>> help(range)
Help on class range in module builtins:

class range(object)
 |  range(stop) -> range object
 |  range(start, stop[, step]) -> range object
 |
 |  Return an object that produces a sequence of integers from start (inclusive)
 |  to stop (exclusive) by step.  range(i, j) produces i, i+1, i+2, ..., j-1.
 |  start defaults to 0, and stop is omitted!  range(4) produces 0, 1, 2, 3.
 |  These are exactly the valid indices for a list of 4 elements.
 |  When step is given, it specifies the increment (or decrement).
```

The official documentation is at [http://docs.python.org](http://docs.python.org).

### Creating programs

Programs are put in `.py` files.

```python
# hello.py
print('hello world')
```

You can create these files with your favorite text editor.

### Running Programs

To execute a program, run it in the terminal with the `python` command.
For example, in command-line Unix:

```bash
bash % python3 hello.py
hello world
bash %
```

Or from the Windows shell:

```shell
C:\SomeFolder>hello.py
hello world

C:\SomeFolder>c:\python36\python hello.py
hello world
```

Note: On Windows, you may need to specify a full path to the Python interpreter such as `c:\python36\python`.  

### A Sample Program

Let's begin this part by trying to solve the following problem:

> One morning, you go out and place a dollar bill on the sidewalk by the Sears tower.
> Each day thereafter, you go out double the number of bills.
> How long does it take for the stack of bills to exceed the height of the tower?

Here's a solution:

```python
# sears.py
bill_thickness = 0.11 * 0.001 # Meters (0.11 mm)
sears_height = 442 # Height (meters)
num_bills = 1
day = 1

while num_bills * bill_thickness < sears_height:
    print(day, num_bills, num_bills * bill_thickness)
    day = day + 1
    num_bills = num_bills * 2

print('Number of days', day)
print('Number of bills', num_bills)
print('Final height', num_bills * bill_thickness)
```

When we run it, we have the solution.

```bash
bash % python3 sears.py 1 1 0.00011
2 2 0.00022
3 4 0.00044
4 8 0.00088
5 16 0.00176
6 32 0.00352
...
21 1048576 115.34336
22 2097152 230.68672 Number of days 23 Number of bills 4194304 Final height 461.37344
```

Using this program as a guide, you can learn a few core concepts about Python.

### Statements

A python program is a sequence of statements:

```python
a = 3 + 4
b = a * 2
print(b)
```

Each statement is terminated by a newline. Statements are executed one after the other until you reach the end of the file.

### Comments

Comments are text that will not be executed.

```python
a = 3 + 4
# This is a comment
b = a * 2
print(b)
```

Comments are denoted by `#` and extend to the end of the line.

### Variables

A variable is a name for a value. You can use letters (lower and
upper-case) from a to z. As well as the character underscore `_`.
Numbers can also be part of the name of a variable, except as the
first character.

```python
height = 442 # valid
_height = 442 # valid
height2 = 442 # valid
2height = 442 # invalid
```

### Types

Variables do not need to be declared with the type of the value.  The type
is associated with the value on the right hand side, not name of the variable.

```python
height = 442           # An integer
height = 442           # Floating point
height = 'Really tall' # A string
```

### Case Sensitivity

Python is case sensitive. Upper and lower-case letters are considered different letters.
These are all different variables:

```python
name = 'Jake'
Name = 'Elwood'
NAME = 'Guido'
```

Language statements are always lower-case.

```python
while x < 0:   # OK
WHILE x < 0:   # ERROR
```

### Looping

Looping is a way to execute a set of instructions any number of times.
There are many ways to accomplish this in Python, one of them is the `while` statement:

```python
while num_bills * bill_thickness < sears_height:
    print(day, num_bills, num_bills * bill_thickness)
    day = day + 1
    num_bills = num_bills * 2

print('Number of days', days)
```

The statements below the `while` will execute as long as the expression after the `while` is `true`.

### Indentation

Indentation in Python is used to denote a set of statements that go together.
From our previous example:

```python
while num_bills * bill_thickness < sears_height:
    print(day, num_bills, num_bills * bill_thickness)
    day = day + 1
    num_bills = num_bills * 2

print('Number of days', days)
```

The indentation means that the following statements go together under the `while`.

```python
    print(day, num_bills, num_bills * bill_thickness)
    day = day + 1
    num_bills = num_bills * 2
```

Because the next statement is not indented, it means that it does not
belong to the previous set.  The empty line is just for
readability. It does not affect the execution.

### Indentation best practices

* Use spaces instead of tabs.
* Use 4 spaces per level.
* Use a Python-aware editor.

Indentation within the block must be consistent.

```python
while num_bills * bill_thickness < sears_height:
    print(day, num_bills, num_bills * bill_thickness)
        day = day + 1 # ERROR
    num_bills = num_bills * 2
```


### Conditionals

The `if` statement is used to execute a conditional:

```python
if a > b:
    # a is greater than b
    print('Computer says no')
else:
    # a is lower or equal to b
    print('Computer says yes')
```

Depending on the values of `a` and `b`, the execution will jump to `print('Computer says no')` or `print('Computer says yes')`.

You can check for multiple conditions with the `elif`.

```python
if a > b:
    # a is greater than b
    print('Computer says no')
elif a == b:
     # a is equal to b
    print('Computer says yes')
else:
    # a is lower to b
    print('Computer says maybe')
```

### Printing

The `print` function produces a single line of text with the values passed.

```python
print('Hello world!') # Prints the text 'Hello world!'
```

You can use variables. The text printed will be the value of the variable, not the name.

```python
x = 100
print(x) # Prints the text '100'
```

If you pass more than one item to `print` they are separated by spaces.

```python
name = 'Jake'
print('My name is', name) # Print the text 'My name is Jake'
```

`print()` always creates a new line at the end.

```python
print('Hello')
print('My name is', 'Jake')
```

This prints:

```code
Hello
My name is Jake
```

This can be avoided.

```python
print('Hello', end=' ')
print('My name is', 'Jake')
```

The previous code will print:

```code
Hello My name is Jake
```

### User input

To read a line of typed user input, use the `input()` function:

```python
name = input('Enter your name:')
print('Your name is', name)
```

`input` prints a prompt to the user and returns the response.
This is useful for small programs, learning exercises or simple debugging.
It is not widely used for real programs.

### `pass` statement

Sometimes you need to specify an empty block. The keyword `pass` is used for it.

```python
if a > b:
    pass
else:
    print('Computer says false')
```

This is also called a "no-op" statement. It does nothing. It serves as a placeholder for statements. Possibly to be added later.

## Exercises

### (a) The Bouncing Ball

A rubber ball is dropped from a height of 100 meters and each time it hits the ground, it bounces back up to 3/5 the height it fell.
Write a program "bounce.py" that prints a table showing the height of the first 10 bounces.

Your program should make a table that looks something like this:

```code
1 60.0
2 36.0
3 21.599999999999998
4 12.959999999999999
5 7.775999999999999
6 4.6655999999999995
7 2.7993599999999996
8 1.6796159999999998
9 1.0077695999999998
10 0.6046617599999998
```

*Note: You can clean up the output a bit if you use the round() function. Try using it to round the output to 4 digits.*

```code
1 60.0
2 36.0
3 21.6
4 12.96
5 7.776
6 4.6656
7 2.7994
8 1.6796
9 1.0078
10 0.6047
```

### (b) Debugging

The following code fragment contains code from the Sears tower problem.  It also has a bug in it.

```python
# sears.py

bill_thickness = 0.11 * 0.001    # Meters (0.11 mm)
sears_height   = 442             # Height (meters)
num_bills      = 1
day            = 1

while num_bills * bill_thickness < sears_height:
    print(day, num_bills, num_bills * bill_thickness)
    day = days + 1
    num_bills = num_bills * 2

print('Number of days', day)
print('Number of bills', num_bills)
print('Final height', num_bills * bill_thickness)
```

Copy and paste the code that appears above in a new program called `sears.py`.
When you run the code you will get an error message that causes the
program to crash like this:

```code
Traceback (most recent call last):
  File "sears.py", line 10, in <module>
    day = days + 1
NameError: name 'days' is not defined
```

Reading error messages is an important part of Python code. If your program
crashes, the very last line of the traceback message is the actual reason why the
the program crashed. Above that, you should see a fragment of source code and then
an identifying filename and line number. 

* Which line is the error?
* What is the error?
* Fix the error
* Run the program successfully


[Contents](../Contents) \| [Previous (1.1 Python)](01_Python) \| [Next (1.3 Numbers)](03_Numbers)
