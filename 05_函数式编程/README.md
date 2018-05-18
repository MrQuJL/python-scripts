# 函数式编程

函数式编程就是一种抽象程度很高的编程范式，纯粹的函数式编程语言编写的函数没有变量，因此，任意一个函数，只要输入是确定的，输出就是确定的，这种纯函数我们称之为没有副作用。而允许使用变量的程序设计语言，由于函数内部的变量状态不确定，同样的输入，可能得到不同的输出，因此，这种函数是有副作用的。

函数式编程的一个特点就是，允许把函数本身作为参数传入另一个函数，还允许返回一个函数！

Python对函数式编程提供部分支持。由于Python允许使用变量，因此，Python不是纯函数式编程语言。

## 高阶函数

因为python中的变量可以指向函数，函数的参数能接受变量，那么一个函数就可以接受另一个函数作为参数，这种函数就称之为高阶函数。

	```
		def add(x, y, f):
			return f(x) + f(y)

		print(add(-5, 6, abs))
	```

### map

* 我们先看map。map()函数接收两个参数，一个是函数，一个是Iterable，map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回。

	```
		>>> def f(x):
		...     return x * x
		...
		>>> r = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])
		>>> list(r)
		[1, 4, 9, 16, 25, 36, 49, 64, 81]
	```

* map()传入的第一个参数是f，即函数对象本身。由于结果r是一个Iterator，Iterator是惰性序列，因此通过list()函数让它把整个序列都计算出来并返回一个list。

* map()作为高阶函数，事实上它把运算规则抽象了，因此，我们不但可以计算简单的f(x)=x2，还可以计算任意复杂的函数，比如，把这个list所有数字转为字符串：

	```
		>>> list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9]))
		['1', '2', '3', '4', '5', '6', '7', '8', '9']
	```

### reduce

* 再看reduce的用法。reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算，其效果就是：

	```
		>>> from functools import reduce
		>>> def add(x, y):
		...     return x + y
		...
		>>> reduce(add, [1, 3, 5, 7, 9])
		25
	```

* 比方说对一个序列求和，就可以用reduce实现：

	```
		>>> from functools import reduce
		>>> def add(x, y):
		...     return x + y
		...
		>>> reduce(add, [1, 3, 5, 7, 9])
		25
	```

### filter

* 和map()类似，filter()也接收一个函数和一个序列。和map()不同的是，filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素。

* 例如，在一个list中，删掉偶数，只保留奇数，可以这么写：

	```
		def is_odd(n):
			return n % 2 == 1

		list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15]))
		# 结果: [1, 5, 9, 15]
	```

* 把一个序列中的空字符串删掉，可以这么写：

	```
		def not_empty(s):
			return s and s.strip()

		list(filter(not_empty, ['A', '', 'B', None, 'C', '  ']))
		# 结果: ['A', 'B', 'C']
	```

* 注意到filter()函数返回的是一个Iterator，也就是一个惰性序列，所以要强迫filter()完成计算结果，需要用list()函数获得所有结果并返回list。

### sorted

* Python内置的sorted()函数就可以对list进行排序：

	```
		>>> sorted([36, 5, -12, 9, -21])
		[-21, -12, 5, 9, 36]
	```

* 此外，sorted()函数也是一个高阶函数，它还可以接收一个key函数来实现自定义的排序，例如按绝对值大小排序：

	```
		>>> sorted([36, 5, -12, 9, -21], key=abs)
		[5, 9, -12, -21, 36]
	```

* sorted也可以对字符串进行排序

	```
		>>> sorted(['bob', 'about', 'Zoo', 'Credit'])
		['Credit', 'Zoo', 'about', 'bob']
	```

* 我们给sorted传入key函数，即可实现忽略大小写的排序：

	```
		>>> sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower)
		['about', 'bob', 'Credit', 'Zoo']
	```

* 要进行反向排序，不必改动key函数，可以传入第三个参数reverse=True：

	```
		>>> sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True)
		['Zoo', 'Credit', 'bob', 'about']
	```

* 从上述例子可以看出，高阶函数的抽象能力是非常强大的，而且，核心代码可以保持得非常简洁。

## 返回函数

* 实现一个可变参数的求和，不需要立刻求和，而是在后面的代码中，根据需要再计算怎么办？ -- 返回函数

	```
		def lazy_sum(*args):
			def sum():
				ax = 0
				for n in args:
					ax = ax + n
				return ax
			return sum
	```

* 这时，调用lazy_sum返回的就不是某个具体的值，而是一个函数

* 并且每次调用都返回的是一个新的函数，即使传入相同的参数：

	```
		>>> f1 = lazy_sum(1, 3, 5, 7, 9)
		>>> f2 = lazy_sum(1, 3, 5, 7, 9)
		>>> f1==f2
		False
	```

* 在这个例子中，我们在函数lazy_sum中又定义了函数sum，并且，内部函数sum可以引用外部函数lazy_sum的参数和局部变量，当lazy_sum返回函数sum时，相关参数和变量都保存在返回的函数中，这种称为“闭包（Closure）”的程序结构拥有极大的威力。

	```
		def count():
		    fs = []
			for i in range(1, 4):
				def f():
					 return i*i
				fs.append(f)
			return fs

		f1, f2, f3 = count()
	```

* 你可能认为调用f1()，f2()和f3()结果应该是1，4，9，但实际结果是：

	```
		>>> f1()
		9
		>>> f2()
		9
		>>> f3()
		9
	```

* 全部都是9！原因就在于返回的函数引用了变量i，但它并非立刻执行。等到3个函数都返回时，它们所引用的变量i已经变成了3，因此最终结果为9。

* **返回闭包时牢记一点：返回函数不要引用任何循环变量，或者后续会发生变化的变量。**

* 如果一定要引用循环变量怎么办？方法是再创建一个函数，用该函数的参数绑定循环变量当前的值，无论该循环变量后续如何更改，已绑定到函数参数的值不变：

	```
		def count():
			def f(j):
				def g():
					return j*j
				return g
			fs = []
			for i in range(1, 4):
				fs.append(f(i)) # f(i)立刻被执行，因此i的当前值被传入f()
			return fs
	```

## 匿名函数

* 在Python中，对匿名函数提供了有限支持。还是以map()函数为例，计算f(x)=x2时，除了定义一个f(x)的函数外，还可以直接传入匿名函数：

	```
		>>> list(map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9]))
		[1, 4, 9, 16, 25, 36, 49, 64, 81]
	```

* 通过对比可以看出，匿名函数lambda x: x * x实际上就是：

	```
		def f(x):
			return x * x
	```

* 关键字lambda表示匿名函数，冒号前面的x表示函数参数。

* 匿名函数有个限制，就是只能有一个表达式，不用写return，返回值就是该表达式的结果。

* 用匿名函数有个好处，因为函数没有名字，不必担心函数名冲突。此外，匿名函数也是一个函数对象，也可以把匿名函数赋值给一个变量，再利用变量来调用该函数：

	```
		>>> f = lambda x: x * x
		>>> f
		<function <lambda> at 0x101c6ef28>
		>>> f(5)
		25
	```

* 同样，也可以把匿名函数作为返回值返回，比如：

	```
		def build(x, y):
			return lambda: x * x + y * y
	```

## 装饰器

* 由于函数也是一个对象，而且函数对象可以被赋值给变量，所以，通过变量也能调用该函数。

	```
		>>> def now():
		...     print('2015-3-25')
		...
		>>> f = now
		>>> f()
		2015-3-25
	```

* 函数对象有一个__name__属性，可以拿到函数的名字：

	```
		>>> now.__name__ # 注意：是两条横线
		'now'
		>>> f.__name__
		'now'
	```

* 现在，假设我们要增强now()函数的功能，比如，在函数调用前后自动打印日志，但又不希望修改now()函数的定义，这种在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）。

* 本质上，decorator就是一个返回函数的高阶函数。所以，我们要定义一个能打印日志的decorator，可以定义如下：

	```
		def log(func):
			def wrapper(*args, **kw):
				print('call %s():' % func.__name__)
				return func(*args, **kw)
			return wrapper
	```

* 观察上面的log，因为它是一个decorator，所以接受一个函数作为参数，并返回一个函数。我们要借助Python的@语法，把decorator置于函数的定义处：

	```
		@log
		def now():
			print('2015-3-25')
	```

* 调用now()函数，不仅会运行now()函数本身，还会在运行now()函数前打印一行日志：

	```
		>>> now()
		call now():
		2015-3-25
	```

* 把@log放到now()函数的定义处，相当于执行了语句：

	```
		now = log(now)
	```

* 由于log()是一个decorator，返回一个函数，所以，原来的now()函数仍然存在，只是现在同名的now变量指向了新的函数，于是调用now()将执行新函数，即在log()函数中返回的wrapper()函数。

* wrapper()函数的参数定义是(*args, **kw)，因此，wrapper()函数可以接受任意参数的调用。在wrapper()函数内，首先打印日志，再紧接着调用原始函数。

* 如果decorator本身需要传入参数，那就需要编写一个返回decorator的高阶函数，写出来会更复杂。比如，要自定义log的文本：

	```
		def log(text):
			def decorator(func):
				def wrapper(*args, **kw):
					print('%s %s():' % (text, func.__name__))
					return func(*args, **kw)
				return wrapper
			return decorator
	```

* 这个3层嵌套的decorator用法如下：

	```
		@log('execute')
		def now():
			print('2015-3-25')
	```

* 执行结果如下：

	```
		>>> now()
		execute now():
		2015-3-25
	```

* 和两层嵌套的decorator相比，3层嵌套的效果是这样的：

	```
		>>> now = log('execute')(now)
	```

* 以上两种decorator的定义都没有问题，但还差最后一步。因为我们讲了函数也是对象，它有__name__等属性，但你去看经过decorator装饰之后的函数，它们的__name__已经从原来的'now'变成了'wrapper'：

	```
		>>> now.__name__
		'wrapper'
	```

* 因为返回的那个wrapper()函数名字就是'wrapper'，所以，需要把原始函数的__name__等属性复制到wrapper()函数中，否则，有些依赖函数签名的代码执行就会出错。

* 不需要编写wrapper.__name__ = func.__name__这样的代码，Python内置的functools.wraps就是干这个事的，所以，一个完整的decorator的写法如下：

	```
		import functools

		def log(func):
			@functools.wraps(func)
			def wrapper(*args, **kw):
				print('call %s():' % func.__name__)
				return func(*args, **kw)
			return wrapper
	```

* 或者针对带参数的decorator：

	```
		import functools

		def log(text):
			def decorator(func):
				@functools.wraps(func)
				def wrapper(*args, **kw):
					print('%s %s():' % (text, func.__name__))
					return func(*args, **kw)
				return wrapper
			return decorator
	```

## 偏函数

* 偏函数的作用就是固定住函数的某些参数

* functools.partial就是帮助我们创建一个偏函数的，不需要我们自己定义int2()，可以直接使用下面的代码创建一个新的函数int2：

	```
		>>> import functools
		>>> int2 = functools.partial(int, base=2)
		>>> int2('1000000')
		64
		>>> int2('1010101')
		85
	```

* 所以，简单总结functools.partial的作用就是，把一个函数的某些参数给固定住（也就是设置默认值），返回一个新的函数，调用这个新函数会更简单。

* 当传入：

	```
		max2 = functools.partial(max, 10)
	```

* 实际上会把10作为*args的一部分自动加到左边，也就是：

	```
		max2(5, 6, 7)
	```

* 相当于：

	```
		args = (10, 5, 6, 7)
		max(*args)
	```

* 结果为10

* 当函数的参数个数太多，需要简化时，使用functools.partial可以创建一个新的函数，这个新函数可以固定住原函数的部分参数，从而在调用时更简单。


