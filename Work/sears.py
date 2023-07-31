# One morning, you go out and place a dollar bill
# on the sidewalk by the Sears tower in Chicago.
# Each day thereafter, you go out double the number
# of bills. How long does it take for the stack of
# bills to exceed the height of the tower?

bill_thickness = 0.11 * 0.001 # meters (0.11 mm)
sears_height = 442 # height (meters)
num_bills = 1
day = 1

def print_day(day, num_bills, height):
    remaining_height = sears_height - height
    print('{:<10}{:<21}{:<20}{:<30}'
        .format(
            f'day: {day}',
            f'num_bills: {num_bills}',
            f'height: {height}',
            f'height_remaining: {round(remaining_height, 2)}'))
    

while num_bills * bill_thickness < sears_height:
    print_day(day, num_bills, num_bills * bill_thickness)
    day += 1
    num_bills *= 2

print_day(day, num_bills, num_bills * bill_thickness)