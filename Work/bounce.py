# bounce.py
#
# Exercise 1.5

starting_height = 100 #meters
actual_height = starting_height #meters
nb_bounces = 10

while nb_bounces > 0 :
    actual_height = (actual_height*3)/5
    print(actual_height)
    nb_bounces = nb_bounces -1