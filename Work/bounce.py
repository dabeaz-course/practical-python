# bounce.py
#
# Exercise 1.5
# Exercise 1.5: The Bouncing Ball

# A rubber ball is dropped from a height of 100 meters.
# Each time it hits the ground, it bounces back up to 3/5 the height it fell.
# Write a program bounce.py that prints a table showing the height of the first 10 bounces.

# Your program should make a table that looks something like this:
height = 100
bounce = 3/5
bounce_no = 0

while bounce_no < 10:
    height = height * bounce
    bounce_no = bounce_no + 1
    print(round(height, 2), bounce_no)