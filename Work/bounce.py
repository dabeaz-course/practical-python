# bounce.py
#
# Exercise 1.5
# rubber ball is dropped from a height of 100 meters
# eadh time it hits the ground, bounces back up to 3/5 of the height it fell
# print first 10 bounce heights

height = 100
bounce = 1
while bounce <= 10:
    height *= 3/5
    print(bounce, round(height,4), 'meters')
    bounce += 1