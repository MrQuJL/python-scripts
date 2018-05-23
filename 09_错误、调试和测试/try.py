try:
	print('try...')
	r = 10 / 0
	print('result:', r)
except ZeroDivisionError as e:
	print('except:', e)
finally:
	print('finally...')
print('END')

try:
	print('try...')
	r = 10 / int('2')
	print('result:', r)
except ValueError as e:
	print('ValueError:', e)
except ZeroDivisionError as e:
	print('ZeroDivisionError:', e)
else:
	print('no error!')
finally:
	print('finally...')
print('END')

print('---------我是分割线------------')

try:
	#foo()
	pass
except ValueError as e:
	print('ValueError')
except UnicodeError as e:
	print('UnicodeError')

# UnicodeError是ValueError的子类

# Python所有的错误都是从BaseException类派生的

def foo(s):
	return 10 / int(s)

def bar(s):
	return foo(s) * 2

def main():
	try:
		bar('0')
	except Exception as e:
		print('Error:', e)
	finally:
		print('finally...')

main()

import logging

def foo(s):
	return 10 / int(s)

def bar(s):
	return foo(s) * 2

def main():
	try:
		bar('0')
	except Exception as e:
		logging.exception(e)


main()
print('END')

class FooError(ValueError):
	pass

def foo(s):
	n = int(s)
	if n == 0:
		raise FooError('invalid value: %s' % s)
	return 10 / n


#foo('0')

def foo(s):
	n = int(s)
	if n == 0:
		raise ValueError('invalid value: %s' % s)
	return 10 / n

def bar():
	try:
		foo('0')
	except ValueError as e:
		print('ValueError!----')
		raise

#bar()

try:
	10 / 0
except ZeroDivisionError:
	raise ValueError('input error!')




