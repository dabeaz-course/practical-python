# bounce.py
#
# Exercise 1.5
bounce_height = 100
bounce_nr = 0
while bounce_nr < 11:
  bounce_nr += bounce_nr
  bounce_height = (3/5)*bounce_height
  print(bounce_nr,bounce_height)
