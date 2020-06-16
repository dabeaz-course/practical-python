# Practical Python Programming - Instructor Notes

Author: David Beazley

## Overview

This document provides some general notes and advice on teaching the
content of my “Practical Python” course including objectives, target
audience, tricky bits, etc.   

These instructions were given to people teaching the course in
a typical three-day corporate training environment.  They might
give you some insight about teaching your own course.

## Target Audience and General Approach

This course is intended to be an “Introduction to Python” course for
people who already have some programming experience.  This is
definitely not a course designed to teach people “programming 101.”

Having said that, I have observed that the typical student in a Python
course is also not likely to be a hard-core software engineer or
programmer.  Instead, you are probably going to get a mix of
engineers, scientists, web programmers, and more inexperienced
developers.  Student background varies widely.  You might have some
students with a lot of C,C++, Java experience, others might know PHP
and HTML, others may be coming from tools like MATLAB, and others
still might have almost no traditional “programming” experience at all
despite my best attempts to make the prerequisites clear.

With this in mind, the course aims to teach Python through the general
problem of manipulating data (stock market data in particular).  This
domain has been chosen because it’s simple and something everyone
should know about it regardless of their background.  Just as an example,
students with weak programming skills are still likely to know about
common things like using a spreadsheet (e.g., Excel).  So, if they’re
really stuck, you can tell them things like “well, this list of tuples
is kind of like rows of data in a spreadsheet” or “a list
comprehension is the same idea as applying an operation to a
spreadsheet column and putting the result in a different column.”  The
key idea is to stay grounded in a real-world setting as opposed to
getting sidetracked into esoteric “computer science” problems (e.g.,
“let’s go compute fibonacci numbers.”).

This problem domain also works well for introducing other programming
topics.  For example, scientists/engineers might want to know about
data analysis or plotting.  So, you can show them how to make a plot
using matplotlib. Web programmers might want to know how to present
stock market data on a web-page.  So, you can talk about template
engines.  Syadmins might want to do something with log files.  So, you
can point them at a log file of real-time streaming stock data.
Software engineers might want to know about design.  So, you can have
them look at ways to encapsulate stock data inside an object or making
a program extensible (e.g., how would make this program produce output
in 10 different table formats).  You get the idea.

## Presentation Guidelines

The presentation slides (notes) are there to provide a narrative
structure to the course and for reference by students when they work
on exercises.  Do not laboriously go over every bullet point on every
slide--assume that students can read and that they will have time to
go back when coding.  I tend to go through the slides at a pretty
brisk pace, showing short examples interactively as I go.  I often
skip slides entirely in favor of live demos.  For example, you don't
really need to do a bunch of slides on lists.  Just go to the
interpreter and do some list examples live instead. Rule of thumb: No
more than 1 minute per slide unless it’s something unusually tricky.
Honestly, you could probably skip most of the slides and simply
lecture using live demos if you feel that it works for you.  I often
do this.

## Course Exercises

The course has about 130 hands-on exercises.  If you do every single
exercise and give students time to think and code, it will likely take
them about 10-12 hours. In practice, you will probably find that students
require more time on certain exercises.  I have some notes about this
below.

You should repeatedly emphasize to students that solution code is
available and that it is okay to look at it and copy it--especially
due to time requirements.

Prior to teaching the course, I would strongly advise that you go
through and work every single course exercise so that there are no
surprises.

During course delivery, I usually work every single exercise from
scratch, without looking at the solution, on my computer while the
students also work.  For this, I strongly advise you to have a printed
copy of the exercises on hand that you can look at without having to
pull it up on the computer screen (which is being projected).  Near
the end of the exercise time period, I will start discussing my
solution code, emphasizes different bits on the screen and talking
about them.  If there are any potential problems with the solution
(including design considerations), I’ll also talk about it.  Emphasize
to students that they may want to look at/copy solution code before
going forward.

## Section 1:  Introduction

The major goal of this section is to get people started with the
environment.  This includes using the interactive shell and
editing/run short programs.  By the end of the section, students
should be able to write short scripts that read data files and perform
small calculations.  They will know about numbers, strings, lists, and
files.  There will also be some exposure to functions, exceptions, and
modules, but a lot of details will be missing.

The first part of this course is often the longest because students
are new to the tools and may have various problems getting things to
work.  It is absolutely critical that you go around the room and make
sure that everyone can edit, run, and debug simple programs.  Make
sure Python is installed correctly.  Make sure they have the course
exercises downloaded.  Make sure the internet works.  Fix anything
else that comes up.

Timing: I aim to finish section 1 around lunch on the first day. 

## Section 2 : Working with Data

This section is probably the most important in the course.  It covers
the basics of data representation and manipulation including tuples,
lists, dicts, and sets.

Section 2.2 the most important.  Give students as much time as
they need to get exercises working within reason.  Depending on audience,
the exercises might last 45 minutes.  In the middle of this exercise,
I will often move forward to Section 2.3 (formatted printing) and
give students more time to keep working.  Together, Sections 2.2/2.3
might take an hour or more.

Section 2.4 has people explore the use of enumerate(), and zip().  I
consider these functions essential so don’t skimp on it.

Section 2.5 introduces the collections module.  There is a LOT that
could be said about collections, but it won't be fully appreciated by
students at this time.  Approach this more from the standpoint of
"here's this cool module you should look at later. Here are a few cool
examples."

Section 2.6 introduces list comprehensions which are an important
feature for processing list data.  Emphasize to students that list
comprehensions are very similar to things like SQL database queries.
At the end of this exercise, I often do an interactive demo involving
something more advanced.  Maybe do a list comprehension and plot some
data with matplotlib.  Also an opportunity to introduce Jupyter if
you're so inclined.

Section 2.7 is the most sophisticated exercise.  It relates to the use
of first-class data in Python and the fact that data structures like
lists can hold any kind of object that you want.  The exercises are
related to parsing columns of data in CSV files and concepts are later reused in
Section 3.2.

Timing: Ideally, you want to be done with section 2 on the first day.
However, it is common to finish with section 2.5 or 2.6.  So, don't
panic if you feel that you're a bit behind.

## 3. Program Organization

The main goal of this section is to introduce more details about
functions and to encourage students to use them.  The section builds
from functions into modules and script writing.

Section 3.1 is about going from simple “scripting” to functions.
Students should be discouraged from writing disorganized “scripts.”
Instead, code should at least be modularized into functions.  It makes
the code easier to understand, it makes it easier to make changes
later, and it actually runs a little bit faster.  Functions are good.

Section 3.2 is probably the most advanced set of exercises in the
whole course.  It has students write a general purpose utility
function for parsing column-oriented data.  However, it makes heavy
use of list comprehensions as well as lists of functions (e.g.,
functions as first-class objects).  You will probably need to guide
people through every single step of this code, showing how it works in
great detail.  The payoff is huge however---you can show people a
short general purpose function that does something amazingly powerful
and which would be virtually impossible to write in C, C++, or Java
without having a *LOT* of very complicated code.  There are a lot of
possible design/discussion avenues for this code.  Use your
imagination.

Section 3.3 adds error handling to the function created in Section 3.2
This is a good time to talk about exception handling generally.
Definitely talk about the dangers of catching all exceptions.  This
might be a good time to talk about the “Errors should never pass
silently” item on the “Zen of Python.”

*Note: Before Exercise 3.4, make sure students get fully working versions of report.py, pcost.py, and fileparse.py.   Copy from Solutions folder if needed *

Section 3.4 Introduces module imports.  The file written in Section
3.2-3.3 is used to simplify code in Section 3.1.  Be aware that you
may need to help students fix issues with IDLE, sys.path, and other
assorted settings related to import.

Section 3.5 talks about `__main__` and script writing.  There's a bit
about command line arguments.  You might be inclined to discuss a
module like argparse.  However, be warned that doing so opens up
a quagmire. It's usually better to just mention it and move on.

Section 3.6 opens up a discussion about design more generally in Python.
Is it better to write code that's more flexible vs code that's
hardwired to only work with filenames?  This is the first place
where you make a code change and have to refactor existing code.

Going forward from here, most of the exercises make small changes
to code that's already been written.

## 4. Classes and Objects

This section is about very basic object oriented programming.  In
general, it is not safe to assume that people have much background in
OO.  So, before starting this, I usually generally describe the OO
“style” and how it's data and methods bundled together.  Do some
examples with strings and lists to illustrate that they are “objects”
and that the methods (invoked via .) do things with the object.
Emphasize how the methods are attached to the object itself.  For
example, you do items.append(x), you don’t call a separate function
append(items, x).

Section 4.1 introduces the class statement and shows people how to
make a basic object.  Really, this just introduces classes as another
way to define a simple data structure--relating back to using tuples
and dicts for this purpose in section 2.

Section 4.2 is about inheritance and how you use to create extensible
programs.  This set of exercises is probably the most significant in terms of
OO programming and OO design.  Give students a lot of time to work on
it (30-45 minutes).  Depending on interest, you can spend a LOT of
time discussing aspects of OO. For example, different
design patterns, inheritance hierarchies, abstract base classes, etc.

Section 4.3 does a few experiments with special methods.  I wouldn't
spend too much time fooling around with this.  Special methods come up
a bit later in Exercise 6.1 and elsewhere.

Timing:   This is usually the end of the 2nd day.

## 5. Inside Objects

This section takes students behind the scenes of the object system and
how it’s built using dictionaries, how instances and classes are tied
together, and how inheritance works.  However, most important part of
this section is probably the material about encapsulation (private
attributes, properties, slots, etc.)

Section 5.1 just peels back the covers and has students observe and
play with the underlying dicts of instances and classes.

Section 5.2 is about hiding attributes behind get/set functions and
using properties.  I usually emphasize that these techniques are
commonly used in libraries and frameworks--especially in situations
where more control over what a user is allowed to do is desired.

An astute Python master will notice that I do not talk about advanced
topics such as descriptors, or attribute access methods (`__getattr__`,
`__setattr__`) at all.  I have found, through experience, that this is
just too much mental overload for students taking the intro course.
Everyone’s head is already on the verge of exploding at this point and
if you go talk about how something like descriptors work, you’ll lose
them for the rest of the day, if not the rest of the course.  Save it
for an "Advanced Python" course.

If you're looking at the clock thinking "There's no way I'm going to
finish this course", you can skip section 5 entirely.

## 6. Generators

The main purpose of this section is to introduce generators as a way
to define custom iteration and to use them for various problems
related to data handling.  The course exercises have students analyze
streaming data in the form of stock updates being written to a log
file.

There are two big ideas to emphasize. First, generators can be used to
write code based on incremental processing.  This can be very useful
for things like streaming data or huge datasets that are too large to
fit into memory all at once.  The second idea is that you can chain
generators/iterators together to create processing pipelines (kind of
like Unix pipes).  Again, this can be a really powerful way to process
and think about streams, large datasets, etc.

Some omissions: Although the iteration protocol is described, the
notes don’t go into detail about creating iterable objects (i.e.,
classes with `__iter__()` and `next()`).  In practice, I’ve found that
it’s not necessary to do this so often (generators are often
better/easier).  So, in the interest of time, I’ve made a conscious
decision to omit it.  Also not included are extended generators
(coroutines) or uses of generators for concurrency (tasklets, etc.).
That’s better covered in advanced courses.

## 7. Advanced Topics

Basically this section is an assortment of more advanced topics that
could have been covered earlier, but weren’t for various reasons
related to course flow and content of the course exercises.  If you
must know, I used to present this material earlier in the course, but
found that students were already overloaded with enough information.
Coming back to it later seems to work better---especially since by
this point, everyone is much more familiar with working in Python and
starting to get the hang of it.

Topics include variadic function arguments (*args, **kwargs), lambda,
closures, and decorators.  Discussion of decorators is only a tiny
hint of what’s possible with metaprogramming.  Feel free to say more
about what’s possible, but I’d probably stay out of metaclasses!
Lately, I have been demoing "numba" as an example of a more
interesting decorator.

If you're pressed for time, most of section 7 can be skipped or heavily
compressed (you could skip exercises for instance).

## 8. Testing and Debugging

The main purpose of this section is just to introduce various tools
and techniques related to testing, debugging, and software
development.  Show everyone the unittest module.  Introduce the
logging module.  Discuss assertions and the idea of “contracts.”  Show
people the debugger and profiler.  Most of this is self-explanatory.

## 9. Packages

At this point, students have written an assortment of files (pcost.py,
report.py, fileparse.py, tableformat.py, stock.py, portfolio.py,
follow.py, etc.).  Two main goals in this section.  First, put all of
the code into a Python package structure.  This is only a gentle
introduction to that, but they'll move the files into a directory and
everything will break.  They'll need to fix their import statements
(package relative imports) and maybe fiddle with an `__init__.py` file.
Second goal, write a simple setup.py file that they can use to package
up the code and give it away to someone.  That's it.  End of the
course.

[Contents](Contents.md)


