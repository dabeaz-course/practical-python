# bounce.py
#
# Exercise 1.5
height = 100
bounce = 1

while bounce <= 10:
    print(bounce, height)
    bounce += 1
    height = (height - (height * 0.4))
    