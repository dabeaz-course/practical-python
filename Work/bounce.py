# bounce.py
#
# Exercise 1.5

height = 100
bounce_back = 3 / 5

i = 1
while i <= 10:
    height = height * bounce_back
    print(i, round(height, 4))
    i += 1
