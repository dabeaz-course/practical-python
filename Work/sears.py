

Sears_height = 442 #in meters
Bill_thickness = 0.00011 #in meters: 0.11 mm
num_bills = 1
day = 1

while num_bills*Bill_thickness < Sears_height:
    print(day, num_bills, num_bills*Bill_thickness)
    day += 1
    num_bills = num_bills*2
    
print('Number of days', day)
print('Number of bills', num_bills)
print('Final height', num_bills*Bill_thickness)