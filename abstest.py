def my_abs(x):
	if x>=0:
		return x
	else:
		return -x
#print(my_abs(9))

import math
def  quadratic(a,b,c):
	x=(-b+math.sqrt(b*b-4*a*c))/2*a
	y=(-b-math.sqrt(b*b-4*a*c))/2*a
	return x,y
x=quadratic(2,3,1)
print(x)
