# sears.py ==> calculate how long it takes for stack of dollar bills to exceed
# height of Sears Tower in Chicago if doubling the number of bills added each
# day
bill_thickness = 0.11 * 0.001 # Meters (0.11mm)
sears_height = 442 # height of Sears Tower in meters
num_bills = 1
day = 1

while num_bills * bill_thickness < sears_height:
    print(day, num_bills, num_bills * bill_thickness)
    day += 1
    num_bills *= 2

print('Number of days ', day)
print('Number of bills ', num_bills)
print('Final height: ', num_bills * bill_thickness)
