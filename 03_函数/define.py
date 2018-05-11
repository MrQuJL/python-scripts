
def nop():
	pass #做占位符

def my_abs(x):
	if not isinstance(x, (int, float)):
		raise TypeError('bad bad bad')
	if x >= 0:
		return x
	else:
		return -x

#my_abs('s')

import math

def move(x, y, step, angle):
	nx = x + step * math.cos(angle)
	ny = y - step * math.sin(angle)
	return nx, ny

x, y = move(100, 100, 60, math.pi / 6)
print(x , y)

r = move(100, 100, 60, math.pi / 6)
print(r[1])

def quadratic(a, b, c):
	x1 = -b + math.sqrt(math.pow(b, 2) - 4 * a * c) / 2 * a
	x2 = -b - math.sqrt(math.pow(b, 2) - 4 * a * c) / 2 * a
	pass
	return x1, x2

print('quadratic(2, 3, 1) =', quadratic(2, 3, 1))
print('quadratic(1, 3, -4) =', quadratic(1, 3, -4))

