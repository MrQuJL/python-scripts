L = [x * x for x in range(10)]

print(L)

g = (x * x for x in range(10))

for i in g:
	print(i)

def fib(max):
	n, a, b = 0, 0, 1
	while n < max:
		yield b
		a, b = b, a + b#a = b, b = a + b
		n = n + 1
	return 'done'

f = fib(6)

print(f)









