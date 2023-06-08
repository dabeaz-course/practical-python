# bounce.py
#
# Exercise 1.5
height = 100
bounce = 3/5

for i in range(1,11):
    new_height = round(height * bounce, 4) 
    print(f'{i} {new_height}')
    height = new_height

