import functools

print(int('12345'))

print(int('12345',base=8))

print(int('12345', 16))

def int2(x, base=2):
	return int(x, base)

print(int2('100000'))

print(int2('101010101'))

int2 = functools.partial(int, base=2)

print(int2('1000000'))

print(int2('10101010'))

print(int2('1000010', base=10))

max2 = functools.partial(max, 10)

print(max2(4,5,6))











