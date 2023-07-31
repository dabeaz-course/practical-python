# bounce.py
#
# Exercise 1.5

def bounce():
    current_height = 100 # meters
    fall_fraction = 3 / 5 # fraction of from_height

    for i in range(1, 11):
        current_height *= fall_fraction
        print(i, round(current_height, 4))

bounce()