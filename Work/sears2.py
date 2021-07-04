# sears.py

# One morning, you go out and place a dollar bill on the sidewalk 
# by the Sears tower in Chicago. Each day thereafter, you go out double
# the number of bills. 
# How long does it take for the stack of bills to 
# exceed the height of the tower?

bill_thickness = 0.11 * 0.001 # Meters (0.11 mm)
sears_height = 442 # Height (meters)
num_bills = 1
day = 1

while (num_bills * bill_thickness) < sears_height:
    num_bills = num_bills * 2
    day += 1

print(f'Height Exceeded: Bills: {num_bills}, Height: {num_bills*bill_thickness}, Days: {day}')
