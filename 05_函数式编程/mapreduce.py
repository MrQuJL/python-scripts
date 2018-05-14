from functools import reduce

def f(x):
	return x * x

r = map(f, [1,2,3,4,5,6,7,8,9])
# r的结果是一个Iterator

print(list(r))

print(list(map(str,[1,2,3,4,5,6,7,8,9])))

def add(x, y):
	return x + y

print(reduce(add, [1,3,5,7,9]))

def fn(x, y):
	return x * 10 + y

print(reduce(fn,[1,3,5,7,9]))

# str --> int

def fn(x, y):
	return x * 10 + y

def char2num(s):
	digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
	return digits[s];

print(reduce(fn,map(char2num, '1357')))

print('------这是一个将字符串转换成int的高阶函数------')

DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

def str2int(s):
	def fn(x, y):
		return x * 10 + y
	def char2num(s):
		return DIGITS[s]
	return reduce(fn, map(char2num, s))

# 利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']

def normalize(name):
	L = name[0].upper() + name[1:].lower()
	return L

L1 = ['adam', 'LISA', 'barT']
print(list(map(normalize, L1)))

# Python提供的sum()函数可以接受一个list并求和，请编写一个prod()函数，可以接受一个list并利用reduce()求积：

print(sum([1,2,3,4,5]))

def prod(L):
	def fun1(x, y):
		return x * y
	return reduce(fun1, L)

print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print('测试成功!')
else:
    print('测试失败!')

# 利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456：

print('----------把字符串转换成浮点数------------')

def str2float(s):
	def str2f(s):
		return float(s)
	return str2f(s)

print(str2float('123.456'))











