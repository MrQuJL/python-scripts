def power(x, n = 2):
	s = 1
	while n > 0:
		n = n - 1
		s = s * x
	return s

print(power(5, 2))

print(power(5, 3))

print(power(5))

def enroll(name, gender, age = 6, city = 'Beijing'):
	print('name', name)
	print('gender', gender)
	print('age', age)
	print('city', city)
	return None

#enroll('Sarah', 'F')

enroll('Adam', 'M', city = 'shanghai')

def add_end(L=None):
	if L is None:
		L = []
	L.append('END')
	return L

L = add_end([1, 2, 3])

print(L)

L = add_end(['x', 'y', 'z'])

print(L)

print(add_end())

print(add_end())

def calc(*numbers):#可变参数，接收到的是一个tuple
	sum = 0
	for i in numbers:
		sum = sum + i * i
	return sum

print('''-------我是分割线-------''')

print(calc())

print(calc(1, 2, 3))

nums = [1, 2, 3]
nums1 = (1, 2, 3, 4)

print(calc(*nums1))

def person(name, age, **kw): #关键字参数，内部是一个dict
	if 'city' in kw:
		pass
	if 'job' in kw:
		pass
	print('name', name, 'age', age, 'other:', kw)

person('Michael', 30)

person('Bob', 35, city='Beijing')

person('Adam', 45, gender='M', job='Engineer')

extra = {'city' : 'Beijing', 'job' : 'Engineer'}

person('Adam', 45, **extra)

# 限制关键字参数的个数
def person(name, age, *, city, job):
	print(name, age, city, job)

person('Jack', 24, city = 'Beijing', job = 'Engineer')

def person(name, age, *args, city='北京', job):
	print(name, age, args, city, job)

person('Jack', 24, city='Beijing', job='Engineer')

person('张三', 34, 1, job = '程序猿')

def f1(a, b, c = 0, *args, **kw):
	print('a=', a, 'b=', b, 'c=', c, 'args=', args, 'kw=', kw)

def f2(a, b, c = 0, *, d, **kw):
	print('a=', a, 'b=', b, 'c=', c, 'd=', d, 'kw=', kw)

f1(1, 2)

f1(1, 2, 3)

f1(1, 2, 3, 'a', 'b')

f1(1, 2, 3, 'a', 'b', x = 99)

f2(1, 2, d = 99, ext=None)

###############################

args = (1, 2, 3, 4)

kw = {'d' : 99, 'x' : '#'}

f1(*args, **kw)

args = (1, 2, 3)

kw = {'d' : 88, 'x' : '#'}

f2(*args, **kw)

def product(*m):
	sum = 1
	for i in m:
		sum = sum * i
	return sum

print(product(1, 2, 3))

def person(name, age, *, city='Beijing', job):
	print(name, age, city, job)

person('张三', 33, job='工作')

