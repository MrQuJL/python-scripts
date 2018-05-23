# 错误、调试和测试

## 错误处理

* 高级语言通常都内置了一套try...except...finally...的错误处理机制，Python也不例外。

* 看一下try的具体用法：

	```
		try:
			print('try...')
			r = 10 / 0
			print('result:', r)
		except ZeroDivisionError as e:
			print('except:', e)
		finally:
			print('finally...')
		print('END')
	```

* 你还可以猜测，错误应该有很多种类，如果发生了不同类型的错误，应该由不同的except语句块处理。没错，可以有多个except来捕获不同类型的错误：

	```
		try:
			print('try...')
			r = 10 / int('a')
			print('result:', r)
		except ValueError as e:
			print('ValueError:', e)
		except ZeroDivisionError as e:
			print('ZeroDivisionError:', e)
		finally:
			print('finally...')
		print('END')
	```

* int()函数可能会抛出ValueError，所以我们用一个except捕获ValueError，用另一个except捕获ZeroDivisionError。

* 此外，如果没有错误发生，可以在except语句块后面加一个else，当没有错误发生时，会自动执行else语句：

	```
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
	```

* Python的错误其实也是class，所有的错误类型都继承自BaseException，所以在使用except时需要注意的是，它不但捕获该类型的错误，还把其子类也“一网打尽”。比如：

	```
		try:
			foo()
		except ValueError as e:
			print('ValueError')
		except UnicodeError as e:
			print('UnicodeError')
	```
* 第二个except永远也捕获不到UnicodeError，因为UnicodeError是ValueError的子类，如果有，也被第一个except给捕获了。

* 如果不捕获错误，自然可以让Python解释器来打印出错误堆栈，但程序也被结束了。既然我们能捕获错误，就可以把错误堆栈打印出来，然后分析错误原因，同时，让程序继续执行下去。

	```
		# err_logging.py

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
	```

* 同样是出错，但程序打印完错误信息后会继续执行，并正常退出：

	```
		$ python3 err_logging.py
		ERROR:root:division by zero
		Traceback (most recent call last):
		  File "err_logging.py", line 13, in main
			bar('0')
		  File "err_logging.py", line 9, in bar
			return foo(s) * 2
		  File "err_logging.py", line 6, in foo
			return 10 / int(s)
		ZeroDivisionError: division by zero
		END
	```

* 如果要抛出错误，首先根据需要，可以定义一个错误的class，选择好继承关系，然后，用raise语句抛出一个错误的实例：

	```
		# err_raise.py
		class FooError(ValueError):
			pass

		def foo(s):
			n = int(s)
			if n==0:
				raise FooError('invalid value: %s' % s)
			return 10 / n

		foo('0')
	```

* 只有在必要的时候才定义我们自己的错误类型。如果可以选择Python已有的内置的错误类型（比如ValueError，TypeError），尽量使用Python内置的错误类型。

* 最后，我们来看另一种错误处理的方式：

	```
		# err_reraise.py

		def foo(s):
			n = int(s)
			if n==0:
				raise ValueError('invalid value: %s' % s)
			return 10 / n

		def bar():
			try:
				foo('0')
			except ValueError as e:
				print('ValueError!')
				raise

		bar()
	```

* 在bar()函数中，我们明明已经捕获了错误，但是，打印一个ValueError!后，又把错误通过raise语句抛出去了，这不有病么？

* 其实这种错误处理方式不但没病，而且相当常见。捕获错误目的只是记录一下，便于后续追踪。但是，由于当前函数不知道应该怎么处理该错误，所以，最恰当的方式是继续往上抛，让顶层调用者去处理。好比一个员工处理不了一个问题时，就把问题抛给他的老板，如果他的老板也处理不了，就一直往上抛，最终会抛给CEO去处理。

* raise语句如果不带参数，就会把当前错误原样抛出。此外，在except中raise一个Error，还可以把一种类型的错误转化成另一种类型：

	```
		try:
			10 / 0
		except ZeroDivisionError:
			raise ValueError('input error!')
	```

* 只要是合理的转换逻辑就可以，但是，决不应该把一个IOError转换成毫不相干的ValueError。

## 调试




## 单元测试




## 文档测试











