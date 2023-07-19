# bounce.py
#
# Exercise 1.5
height = 100
bounce = 0

while bounce < 10:
    bounce += 1
    height = (height - (height * 0.4))
    print(bounce, round(height, ndigits=4))
