max = 0
min = 0
while True:
	x = input("please input a number:")
	if  x == 'done':
		break
	try:
		x = float(x)
	except:
		print(" %s is not a number"% x)
		continue
	if max is 0 or max < x:
		max = x
	if min is 0 or min > x:
		min = x
print(max,min)
input( )