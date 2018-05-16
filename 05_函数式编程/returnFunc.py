def calc_sum(*args):
	ax = 0
	for n in args:
		ax = ax + n
	return ax

print(calc_sum(1,2,3,4,5))

def lazy_sum(*args):
	def sum():
		ax = 0
		for n in args:
			ax = ax + n
		return ax
	return sum

f = lazy_sum(1,3,5,7,9)

print(f)

print(f())

f1 = lazy_sum(1,3,5,7,9)
f2 = lazy_sum(1,3,5,7,9)

print(f1 == f2)

print('---------我是分割线--------------')

def count():
	fs = []
	for i in range(1,4):
		def f():
			return i * i
		fs.append(f)
	return fs

f1, f2, f3 = count()

print(f1())

print(f2())

print(f3())

def count():
	def f(j):
		def g():
			return j*j
		return g
	fs = []
	for i in range(1,4):
		fs.append(f(i))
	return fs

f1, f2, f3 = count()

print(f1())

print(f2())

print(f3())



