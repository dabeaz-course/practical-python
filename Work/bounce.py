# bounce.py
#
# Exercise 1.5

height = 100
bounce = 1
while bounce < 11:
    height = (3/5)*(height)
    print(bounce, round(height,4))
    bounce += 1

