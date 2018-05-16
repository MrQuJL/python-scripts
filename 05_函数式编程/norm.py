L = list(map(lambda x : x * x, [1,2,3,4,5]))

print(L)

f = lambda x : x * x

print(f)

print(f(5))

def build(x, y):
	return lambda: x * x + y * y

print(build(1,2)())

L = list(filter(lambda x : x & 0x1 == 1, range(1, 20)))

print(L)







