# Course Setup and Overview

Welcome to Practical Python Programming!   This page has some important information
about course setup and logistics.

## Course Duration and Time Requirements

This course was originally given as an instructor-led in-person
training that spanned 3 to 4 days.  To complete the course in its
entirety, you should minimally plan on committing 25-35 hours of work.
Most participants find the material to be quite challenging without
peeking at solution code (see below).

## Setup and Python Installation

You need nothing more than a basic Python 3.6 installation or newer.
There is no dependency on any particular operating system, editor,
IDE, or extra Python-related tooling.  There are no third-party
dependencies.

That said, most of this course involves learning how to write scripts
and small programs that involve data read from files.  Therefore, you
need to make sure you're in an environment where you can easily work
with files.  This includes using an editor to create Python programs
and being able to run those programs from the shell/terminal.

You might be inclined to work on this course using a more interactive
environment such as Jupyter Notebooks. **I DO NOT ADVISE THIS!**
Although notebooks are great for experimentation, many of the
exercises in this course teach concepts related to program
organization.  This includes working with functions, modules, import
statements, and refactoring of programs whose source code spans
multiple files.  In my experience, it is hard to replicate this kind
of working environment in notebooks.

## Forking/Cloning the Course Repository

To prepare your environment for the course, I recommend creating your
own fork of the course GitHub repo at
[https://github.com/dabeaz-course/practical-python](https://github.com/dabeaz-course/practical-python).
Once you are done, you can clone it to your local machine:

```
bash % git clone https://github.com/yourname/practical-python
bash % cd practical-python
bash %
```

Do all of your work within the `practical-python/` directory.  If you
commit your solution code back to your fork of the repository, it will
keep all of your code together in one place and you'll have a nice
historical record of your work when you're done.

If you don't want to create a personal fork or don't have a GitHub account,
you can still clone the course directory to your machine:

```
bash % git clone https://github.com/dabeaz-course/practical-python
bash % cd practical-python
bash %
```

With this option, you just won't be able to commit code changes except
to the local copy on your machine.

## Coursework Layout

Do all of your coding work in the `Work/` directory.  Within that
directory, there is a `Data/` directory.  The `Data/` directory
contains a variety of datafiles and other scripts used during the
course. You will frequently have to access files located in `Data/`.
Course exercises are written with the assumption that you are creating
programs in the `Work/` directory.

## Course Order

Course material should be completed in section order, starting with
section 1.  Course exercises in later sections build upon code written in
earlier sections.  Many of the later exercises involve minor refactoring
of existing code.

## Solution Code

The `Solutions/` directory contains full solution code to selected
exercises.  Feel free to look at this if you need a hint.  To get the
most out of the course however, you should try to create your own
solutions first.

[Contents](Contents.md) \| [Next (1 Introduction to Python)](01_Introduction/00_Overview.md)









