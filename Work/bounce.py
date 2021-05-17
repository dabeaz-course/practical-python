# bounce.py
#
# Exercise 1.5
print("BOUNCE BALL")
wall = 100 #meters
bounce = 3/5 #meters
count = 0
while count < 10:
    count+=1
    ball = wall*bounce
    wall = ball
    print(count," ", ball)
    

