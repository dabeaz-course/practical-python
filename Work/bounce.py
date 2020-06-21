# bounce.py
#
# Exercise 1.5
def bounce(height):
    for i in range(1, 11):
        height = round(height * 3 / 5, 4)
        print(f'{i} {height}')

bounce(100)