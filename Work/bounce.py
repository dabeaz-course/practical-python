# bounce.py
#
# Exercise 1.5

starting_height = 100 #meters
actual_height = starting_height #meters
nb_bounces = 10

while nb_bounces > 0 :
    actual_height = (actual_height*3)/5
    print(round(actual_height,5))
    nb_bounces = nb_bounces -1