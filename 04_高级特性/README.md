# 高级特性

在Python中，代码不是越多越好，而是越少越好。代码不是越复杂越好，而是越简单越好。

基于这一思想，我们来介绍Python中非常有用的高级特性，1行代码能实现的功能，决不写5行代码。请始终牢记，代码越少，开发效率越高。

## 切片

* 取前3个元素，用一行代码就可以完成切片：
	
	```
		>>> L[0:3]
		['Michael', 'Sarah', 'Tracy']
	```

* L[0:3]表示，从索引0开始取，直到索引3为止，但不包括索引3。即索引0，1，2，正好是3个元素，如果第一个索引是0，还可以省略：

	```
		>>> L[:3]
		['Michael', 'Sarah', 'Tracy']
	```

* 后10个数：

	```
		>>> L[-10:]
		[90, 91, 92, 93, 94, 95, 96, 97, 98, 99]
	```

* 前10个数，每两个取一个：

	```
		>>> L[:10:2]
		[0, 2, 4, 6, 8]
	```

* 所有数，每5个取一个：

	```
		>>> L[::5]
		[0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95]
	```

* 甚至什么都不写，只写[:]就可以原样复制一个list：

	```
		>>> L[:]
		[0, 1, 2, 3, ..., 99]
	```

* tuple也是一种list，唯一区别是tuple不可变。因此，tuple也可以用切片操作，只是操作的结果仍是tuple：

	```
		>>> (0, 1, 2, 3, 4, 5)[:3]
		(0, 1, 2)
	```

* 字符串'xxx'也可以看成是一种list，每个元素就是一个字符。因此，字符串也可以用切片操作，只是操作结果仍是字符串：

	```
		>>> 'ABCDEFG'[:3]
		'ABC'
		>>> 'ABCDEFG'[::2]
		'ACEG'
	```

## 迭代

* 在Python中，迭代是通过for ... in来完成的Python的for循环抽象程度要高于C的for循环，因为Python的for循环不仅可以用在list或tuple上，还可以作用在其他可迭代对象上。
	
	```
		>>> d = {'a': 1, 'b': 2, 'c': 3}
		>>> for key in d:
		...     print(key)
		...
		a
		c
		b
	```

* 默认情况下，dict迭代的是key。如果要迭代value，可以用for value in d.values()，如果要同时迭代key和value，可以用for k, v in d.items()。

* 所以，当我们使用for循环时，只要作用于一个可迭代对象，for循环就可以正常运行，而我们不太关心该对象究竟是list还是其他数据类型。

* 那么，如何判断一个对象是可迭代对象呢？方法是通过collections模块的Iterable类型判断：

	```
		>>> from collections import Iterable
		>>> isinstance('abc', Iterable) # str是否可迭代
		True
		>>> isinstance([1,2,3], Iterable) # list是否可迭代
		True
		>>> isinstance(123, Iterable) # 整数是否可迭代
		False
	```

* 最后一个小问题，如果要对list实现类似Java那样的下标循环怎么办？Python内置的enumerate函数可以把一个list变成索引-元素对，这样就可以在for循环中同时迭代索引和元素本身：

	```
		>>> for i, value in enumerate(['A', 'B', 'C']):
		...     print(i, value)
		...
		0 A
		1 B
		2 C
	```

* 上面的for循环里，同时引用了两个变量，在Python里是很常见的，比如下面的代码：

	```
		>>> for x, y in [(1, 1), (2, 4), (3, 9)]:
		...     print(x, y)
		...
		1 1
		2 4
		3 9
	```

* 练习：请使用迭代查找一个list中最小和最大值，并返回一个tuple：

	```
		def findMinAndMax(L):
			if L == None or len(L) == 0:
				return (None, None)
			if len(L) == 1:
				return (L[0], L[0])
			min = L[0]
			max = L[0]
			for i in L:
				if i < min:
					min = i
				if i > max:
					max = i
			return (min, max)
	```

## 列表生成式

* 举个例子，要生成list [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]可以用list(range(1, 11))：

	```
		>>> list(range(1, 11))
		[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
	```

* 但如果要生成[1x1, 2x2, 3x3, ..., 10x10]怎么做？方法一是循环：

	```
		>>> L = []
		>>> for x in range(1, 11):
		...    L.append(x * x)
		...
		>>> L
		[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
	```

* 但是循环太繁琐，而列表生成式则可以用一行语句代替循环生成上面的list：

	```
		>>> [x * x for x in range(1, 11)]
		[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
	```

* for循环后面还可以加上if判断，这样我们就可以筛选出仅偶数的平方：

	```
		>>> [x * x for x in range(1, 11) if x % 2 == 0]
		[4, 16, 36, 64, 100]
	```

* 还可以使用两层循环，可以生成全排列：

	```
		>>> [m + n for m in 'ABC' for n in 'XYZ']
		['AX', 'AY', 'AZ', 'BX', 'BY', 'BZ', 'CX', 'CY', 'CZ']
	```

* 运用列表生成式，可以写出非常简洁的代码。例如，列出当前目录下的所有文件和目录名，可以通过一行代码实现：

	```
		>>> import os # 导入os模块，模块的概念后面讲到
		>>> [d for d in os.listdir('.')] # os.listdir可以列出文件和目录
		['.emacs.d', '.ssh', '.Trash', 'Adlm', 'Applications', 'Desktop', 'Documents', 'Downloads', 'Library', 'Movies', 'Music', 'Pictures', 'Public', 'VirtualBox VMs', 'Workspace', 'XCode']
	```

* for循环其实可以同时使用两个甚至多个变量，比如dict的items()可以同时迭代key和value：

	```
		>>> d = {'x': 'A', 'y': 'B', 'z': 'C' }
		>>> for k, v in d.items():
		...     print(k, '=', v)
		...
		y = B
		x = A
		z = C
	```

* 因此，列表生成式也可以使用两个变量来生成list：

	```
		>>> d = {'x': 'A', 'y': 'B', 'z': 'C' }
		>>> [k + '=' + v for k, v in d.items()]
		['y=B', 'x=A', 'z=C']
	```

* 最后把一个list中所有的字符串变成小写：

	```
		>>> L = ['Hello', 'World', 'IBM', 'Apple']
		>>> [s.lower() for s in L]
		['hello', 'world', 'ibm', 'apple']
	```

## 生成器

* 通过列表生成式，我们可以直接创建一个列表。但是，受到内存限制，列表容量肯定是有限的。而且，创建一个包含100万个元素的列表，不仅占用很大的存储空间，如果我们仅仅需要访问前面几个元素，那后面绝大多数元素占用的空间都白白浪费了。

* 所以，如果列表元素可以按照某种算法推算出来，那我们是否可以在循环的过程中不断推算出后续的元素呢？这样就不必创建完整的list，从而节省大量的空间。在Python中，这种一边循环一边计算的机制，称为生成器：generator。

	```
		>>> L = [x * x for x in range(10)]
		>>> L
		[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
		>>> g = (x * x for x in range(10))
		>>> g
		<generator object <genexpr> at 0x1022ef630>
	```

* 创建L和g的区别仅在于最外层的[]和()，L是一个list，而g是一个generator。

* 对generator的跌打是通过for循环或者next函数来取下一个元素的

* 斐波拉契数列用列表生成式写不出来，但是，用函数把它打印出来却很容易：

	```
		def fib(max):
			n, a, b = 0, 0, 1
			while n < max:
				print(b)
				a, b = b, a + b
				n = n + 1
			return 'done'
	```

* 注意赋值语句：

	```
		a, b = b, a + b
	```

* 相当于:

	```
		t = (b, a + b) # t是一个tuple
		a = t[0]
		b = t[1]
	```

* 要把fib函数变成generator，只需要把print(b)改为yield b就可以了：

	```
		def fib(max):
			n, a, b = 0, 0, 1
			while n < max:
				yield b
				a, b = b, a + b
				n = n + 1
			return 'done'
	```

* 这就是定义generator的另一种方法。如果一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generator：

	```
		>>> f = fib(6)
		>>> f
		<generator object fib at 0x104feaaa0>
	```

* 这里，最难理解的就是generator和函数的执行流程不一样。函数是顺序执行，遇到return语句或者最后一行函数语句就返回。而变成generator的函数，在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行。

## 迭代器

* 可以直接作用于for循环的数据类型有以下几种：

	1. 一类是集合数据类型，如list、tuple、dict、set、str等

	2. 一类是generator，包括生成器和带yield的generator function

* 这些可以直接作用于for循环的对象统称为可迭代对象：Iterable

* 可以使用isinstance()判断一个对象是否是Iterable对象：

	```
		>>> from collections import Iterable
		>>> isinstance([], Iterable)
		True
		>>> isinstance({}, Iterable)
		True
		>>> isinstance('abc', Iterable)
		True
		>>> isinstance((x for x in range(10)), Iterable)
		True
		>>> isinstance(100, Iterable)
		False
	```

* 而生成器不但可以作用于for循环，还可以被next()函数不断调用并返回下一个值，直到最后抛出StopIteration错误表示无法继续返回下一个值了。

* **可以被next()函数调用并不断返回下一个值的对象称为迭代器：Iterator**

* 可以使用isinstance()判断一个对象是否是Iterator对象：

	```
		>>> from collections import Iterator
		>>> isinstance((x for x in range(10)), Iterator)
		True
		>>> isinstance([], Iterator)
		False
		>>> isinstance({}, Iterator)
		False
		>>> isinstance('abc', Iterator)
		False
	```

* 生成器都是Iterator对象，但list、dict、str虽然是Iterable，却不是Iterator

* 把list、dict、str等Iterable变成Iterator可以使用iter()函数：

	```
		>>> isinstance(iter([]), Iterator)
		True
		>>> isinstance(iter('abc'), Iterator)
		True
	```

* 你可能会问，为什么list、dict、str等数据类型不是Iterator？

* 这是因为Python的Iterator对象表示的是一个数据流，Iterator对象可以被next()函数调用并不断返回下一个数据，直到没有数据时抛出StopIteration错误。可以把这个数据流看做是一个有序序列，但我们却不能提前知道序列的长度，只能不断通过next()函数实现按需计算下一个数据，所以Iterator的计算是惰性的，只有在需要返回下一个数据时它才会计算。

* Iterator甚至可以表示一个无限大的数据流，例如全体自然数。而使用list是永远不可能存储全体自然数的。

* 凡是可作用于for循环的对象都是Iterable类型；

* 是可作用于next()函数的对象都是Iterator类型，它们表示一个惰性计算的序列；

* 集合数据类型如list、dict、str等是Iterable但不是Iterator，不过可以通过iter()函数获得一个Iterator对象。

* Python的for循环本质上就是通过不断调用next()函数实现的，例如：

	```
		for x in [1, 2, 3, 4, 5]:
			pass
	```

* 实际上完全等价于：

	```
		# 首先获得Iterator对象:
		it = iter([1, 2, 3, 4, 5])
		# 循环:
		while True:
			try:
				# 获得下一个值:
				x = next(it)
			except StopIteration:
				# 遇到StopIteration就退出循环
				break
	```





