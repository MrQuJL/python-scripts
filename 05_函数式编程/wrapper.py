import functools

def now():
	print('2015-3-25')

f = now
f()

print(now.__name__)

print(f.__name__)

print('----------我是分割线----------')

def log1(func):
	def wrapper(*args, **kw):
		print('call %s():' % func.__name__)
		return func(*args, **kw)
	return wrapper

log1(now)()

def log(func):
	@functools.wraps(func)
	def wrapper(*args, **kw):
		print("call %s():" % func.__name__)
		return func(*args, **kw)
	return wrapper

def metric(fn):
	print('%s executed in %s ms' % (fn.__name__, 10.24))
	return fn

def log(func):
	def wrapper(*args, **kw):
		print('call %s():' % func.__name__)
		return func(*args, **kw)
	return wrapper

@log
def now():
	print('2015-3-25')

print('--------我是--------')
now()
print(now.__name__)

def log(text):
	def decorator(func):
		def wrapper(*args, **kw):
			print('%s %s:' % (text, func.__name__))
			return func(*args, **kw)
		return wrapper
	return decorator

@log('execute')
def now():
	print('2015-3-25')

print('------自定义文本分割线-----')
now()

now = log('aaa')(now)




