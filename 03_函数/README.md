# 函数

## 调用函数

* 要调用一个函数，需要知道函数的名称和参数，比如求绝对值的函数abs

	```
		>>> abs(100)
		100
		>>> abs(-20)
		20
		>>> abs(12.34)
		12.34
	```

* abs只有一个参数，参数类型如果不是数字会报错

* 而max函数max()可以接收任意多个参数，并返回最大的那个

* 数据类型转换, Python内置的常用函数还包括数据类型转换函数，比如int()函数可以把其他数据类型转换为整数

	```
		>>> int('123')
		123
		>>> int(12.34)
		12
		>>> float('12.34')
		12.34
		>>> str(1.23)
		'1.23'
		>>> str(100)
		'100'
		>>> bool(1)
		True
		>>> bool('')
		False
	```

* 也可以给函数起别名

	```
		>>> a = abs # 变量a指向abs函数
		>>> a(-1) # 所以也可以通过a调用abs函数
		1
	```

* hex()函数可以把一个整数转换成十六进制表示的字符串

## 定义函数

* 在Python中，定义一个函数要使用def语句，依次写出函数名、括号、括号中的参数和冒号:，然后，在缩进块中编写函数体，函数的返回值用return语句返回。

* 如果你已经把my_abs()的函数定义保存为abstest.py文件了，那么，可以在该文件的当前目录下启动Python解释器，用from abstest import my_abs来导入my_abs()函数，注意abstest是文件名（不含.py扩展名）：

	```
		from abstest import my_abs
	```

* 空函数

	```
		def nop():
			pass
	```

* pass语句什么都不做，那有什么用？实际上pass可以用来作为占位符，比如现在还没想好怎么写函数的代码，就可以先放一个pass，让代码能运行起来。

* pass还可以用在其他语句里，比如：

	```
		if age >= 18:
			pass
	```

* 还可以对传入的参数进行类型检查

	```
		def my_abs(x):
			if not isinstance(x, (int, float)):
				raise TypeError('bad operand type')
			if x >= 0:
				return x
			else:
				return -x
	```

* 函数可以返回多个值

	```
		import math

		def move(x, y, step, angle=0):
			nx = x + step * math.cos(angle)
			ny = y - step * math.sin(angle)
			return nx, ny
		
		>>> x, y = move(100, 100, 60, math.pi / 6)
		>>> print(x, y)
		151.96152422706632 70.0
	```

* **但其实这只是一种假象，Python函数返回的仍然是单一值**

	```
		>>> r = move(100, 100, 60, math.pi / 6)
		>>> print(r)
		(151.96152422706632, 70.0)
	```

* 原来返回值是一个tuple！但是，在语法上，返回一个tuple可以省略括号，而多个变量可以同时接收一个tuple，按位置赋给对应的值，所以，Python的函数返回多值其实就是返回一个tuple，但写起来更方便。

* 函数执行完毕也没有return语句时，自动return None。

* 函数可以同时返回多个值，但其实就是一个tuple。

## 函数的参数

1. 位置参数

	* 我们先写一个计算x的n次方的函数：

		```
			def power(x, n):
				s = 1
				while n > 0:
					n = n - 1
					s = s * x
				return s
		```

2. 默认参数

	* 由于我们经常计算x2，所以，完全可以把第二个参数n的默认值设定为2
	
		```
			def power(x, n=2):
				s = 1
				while n > 0:
					n = n - 1
					s = s * x
				return s
		```

	* 这样，当我们调用power(5)时，相当于调用power(5, 2)

	* 注：一是必选参数在前，默认参数在后，否则Python的解释器会报错

	* 当函数有多个参数时，把变化大的参数放前面，变化小的参数放后面。变化小的参数就可以作为默认参数

	* 默认参数的最大好处是可以降低函数的调用难度

	* 默认参数很有用，但使用不当，也会掉坑里。默认参数有个最大的坑，演示如下：

		```
			def add_end(L=[]):
				L.append('END')
				return L
			
			print(add_end())
			print(add_end())
			## 两次调用的结果不一致是因为L是一个引用类型的参数，每次调用之后引用所指向的内容已经发生了改变，所以会产生多次调用结果不一致的现象
		```

	* 定义默认参数要牢记一点：默认参数必须指向不变对象！

	* 可以通过None这个不变对象来实现:
		
		```
			def add_end(L=None):
				if L is None:
					L = []
				L.append('END')
				return L
		```

	* 这样，无论调用多少次，都不会有问题

	* 为什么要设计str、None这样的不变对象呢？因为不变对象一旦创建，对象内部的数据就不能修改，这样就减少了由于修改数据导致的错误。此外，由于对象不变，多任务环境下同时读取对象不需要加锁，同时读一点问题都没有。我们在编写程序时，如果可以设计一个不变对象，那就尽量设计成不变对象。

3. 可变参数

	* 可变参数的定义是这个样子的:

		```
			def calc(*numbers):
				sum = 0
				for n in numbers:
					sum = sum + n * n
				return sum
		```
	
	* 在函数内部，参数numbers接收到的是一个tuple

	* 在函数外部，传入的既可以是list也可以是tuple，调用方式如下：

		```
			calc(1, 2, 3) or
			nums = [1, 2, 3]
			calc(*nums)
			nums = (1, 2, 3)
			calc(*nums)
		```

4. 关键字参数

	* 关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict

		```
			def person(name, age, **kw):
				print('name:', name, 'age:', age, 'other:', kw)

			>>> person('Michael', 30)
			name: Michael age: 30 other: {}
		```

	* 也可以传入任意个数的关键字参数

		```
			>>> person('Bob', 35, city='Beijing')
			name: Bob age: 35 other: {'city': 'Beijing'}
			>>> person('Adam', 45, gender='M', job='Engineer')
			name: Adam age: 45 other: {'gender': 'M', 'job': 'Engineer'}
		```

	* 简化书写：

		```
			>>> extra = {'city': 'Beijing', 'job': 'Engineer'}
			>>> person('Jack', 24, **extra)
			name: Jack age: 24 other: {'city': 'Beijing', 'job': 'Engineer'}
		```

	* **extra表示把extra这个dict的所有key-value用关键字参数传入到函数的**kw参数，kw将获得一个dict，注意kw获得的dict是extra的一份拷贝，对kw的改动不会影响到函数外的extra

5. 命名关键字参数

	* 对于关键字参数，函数的调用者可以传入任意不受限制的关键字参数，但是，如果要限制关键字参数的名字，就可以用命名关键字参数

	* 命名关键字参数是长这个样子的：

		```
			def person(name, age, *, city, job):
				print(name, age, city, job)
		```

	* 和关键字参数**kw不同，命名关键字参数需要一个特殊分隔符*，*后面的参数被视为命名关键字参数

		```
			>>> person('Jack', 24, city='Beijing', job='Engineer')
			Jack 24 Beijing Engineer
		```

	* 注：命名关键字参数为必须传入的参数，如果不传入则会报错

		```Python
			person('张三', 33) #报错
		```

	* 使用命名关键字参数时，要特别注意，如果没有可变参数，就必须加一个*作为特殊分隔符。如果缺少*，Python解释器将无法识别位置参数和命名关键字参数：

6. 参数组合

	* 在Python中定义函数，可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，这5种参数都可以组合使用。但是请注意，参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。

	* 比如定义一个函数，包含上述若干种参数：

		```
			def f1(a, b, c=0, *args, **kw):
				print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)

			def f2(a, b, c=0, *, d, **kw):
				print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)
		```
	
	* 调用代码如下：

		```
			>>> f1(1, 2)
			a = 1 b = 2 c = 0 args = () kw = {}
			>>> f1(1, 2, c=3)
			a = 1 b = 2 c = 3 args = () kw = {}
			>>> f1(1, 2, 3, 'a', 'b')
			a = 1 b = 2 c = 3 args = ('a', 'b') kw = {}
			>>> f1(1, 2, 3, 'a', 'b', x=99)
			a = 1 b = 2 c = 3 args = ('a', 'b') kw = {'x': 99}
			>>> f2(1, 2, d=99, ext=None)
			a = 1 b = 2 c = 0 d = 99 kw = {'ext': None}
		```

	* 最神奇的是通过一个tuple和dict，你也可以调用上述函数：

		```
			>>> args = (1, 2, 3, 4)
			>>> kw = {'d': 99, 'x': '#'}
			>>> f1(*args, **kw)
			a = 1 b = 2 c = 3 args = (4,) kw = {'d': 99, 'x': '#'}
			>>> args = (1, 2, 3)
			>>> kw = {'d': 88, 'x': '#'}
			>>> f2(*args, **kw)
			a = 1 b = 2 c = 3 d = 88 kw = {'x': '#'}
		```

	* 所以，对于任意函数，都可以通过类似func(*args, **kw)的形式调用它，无论它的参数是如何定义的

	* **虽然可以组合多达5种参数，但不要同时使用太多的组合，否则函数接口的可理解性很差。**

## 递归函数

