# bounce.py
#
# Exercise 1.5

height = 100 #meters
bounce_height = 0.6 #height of each bounce
num_bounce = 10 #number of bounces
bounce = 1

while bounce <= num_bounce:
    height = height * bounce_height
    print(bounce, round(height, 4))
    bounce = bounce + 1
   
