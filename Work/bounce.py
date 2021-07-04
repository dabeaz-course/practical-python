# bounce.py
#
# Exercise 1.5

# Output height of the first 10 bounces. (program does not need to run for more than that)

# Bounce happens indefintely until ball stops bouncing
# Denote 0 height as the end of the program.
# Ball will bounce 3/5 of its original height (currently 100m) at each bounce.

# Assume height is in meters (arbitrary what the units are)
height = 100

bounce = 0

while bounce != 10:
    height = height * (3/5)
    bounce = bounce + 1
    print(f'{bounce}  {round(height,4)}')


