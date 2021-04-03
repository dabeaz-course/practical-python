num_bills = 1
bill_thickness = 0.11 * 0.001 #metres because each bill is 0.11mm
bill_height = bill_thickness * num_bills
sears_height = 442 #metres
day = 1
while  bill_height  <= sears_height: #changed from if to while because of solution
	print(day, num_bills, bill_height) #copied this part from the solution
	num_bills = num_bills * 2
	bill_height = num_bills * bill_thickness
	day = day + 1
# else:
#	print(day)
print('Number of days', day) #copied
print('Number of bills', num_bills) #copied
print('Final Height', bill_height) #copied
