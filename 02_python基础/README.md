# Python基础

## 转义字符

* 如果字符串内部既包含'又包含"怎么办？可以用转义字符\来标识，比如：
	
	```'I\'m \"OK\"!'```

* 如果字符串里面有很多字符都需要转义，就需要加很多\，为了简化，Python还允许用r''表示''内部的字符串默认不转义，可以自己试试：

	```print(r'\\\t\\')```

* 如果字符串内部有很多换行，用\n写在一行里不好阅读，为了简化，Python允许用'''...'''的格式表示多行内容(在三个单引号内换行直接敲回车即可，...表示由很多数据)

	```
		print('''line1
		line2
		line3''')
	```

* 如果在'''内还想不转义字符在前面加上r即可

	```
		print(r'''hello,\n
		world''')
	```

## 布尔值

* 布尔值和布尔代数的表示完全一致，一个布尔值只有True、False两种值，要么是True，要么是False，在Python中，可以直接用True、False表示布尔值（请注意大小写）

	```
		print(True)
		print(False)
		print(3 > 2)
		print(2 > 3)
	```

* and（与） or（或） not（非）

	```
		if age > 18:
			print('adult')
		else:
			print('teenager')
	```

## 空值

* 空值是Python里一个特殊的值，用None表示。None不能理解为0，因为0是有意义的，而None是一个特殊的空值

## 变量

* 变量的概念基本上和初中代数的方程变量是一致的，只是在计算机程序中，变量不仅可以是数字，还可以是任意数据类型。

* 变量在程序中就是用一个变量名表示了，变量名必须是大小写英文、数字和_的组合，且不能用数字开头

	```
		a = 123 # a是整数

		print(a)

		a = 'ABC' # a变为字符串

		print(a)
	```

* 这种变量本身类型不固定的语言称之为动态语言，与之对应的是静态语言。静态语言在定义变量时必须指定变量类型，如果赋值的时候类型不匹配，就会报错。

## 除法（精确除 VS 地板除）

	```
		print(10 / 3)
		print(10 // 3)
	```

## 小结

* 注意：Python的整数没有大小限制，而某些语言的整数根据其存储长度是有大小限制的，例如Java对32位整数的范围限制在-2147483648-2147483647。

* Python的浮点数也没有大小限制，但是超出一定范围就直接表示为inf（无限大）。

## python字符编码

* 在最新的Python 3版本中，字符串是以Unicode编码的，也就是说，Python的字符串支持多语言

* 对于单个字符的编码，Python提供了ord()函数获取字符的整数表示，chr()函数把编码转换为对应的字符

* 由于Python的字符串类型是str，在内存中以Unicode表示，一个字符对应若干个字节。如果要在网络上传输，或者保存到磁盘上，就需要把str变为以字节为单位的bytes

* 以Unicode表示的str通过encode()方法可以编码为指定的bytes

* 'ABC'.encode('ascii')

* 'ABC'.encode('utf-8')

* 'ABC'.encode('UTF8')

* 反过来，如果我们从网络或磁盘上读取了字节流，那么读到的数据就是bytes。要把bytes变为str，就需要用decode()方法

* 如果bytes中只有一小部分无效的字节，可以传入errors='ignore'忽略错误的字节：

	```
		 b'\xe4\xb8\xad\xff'.decode('utf-8', errors='ignore')
	```

* 要计算str包含多少个字符，可以用len()函数

	```
		len('ABC')
		len('中文')
	```

* len()函数计算的是str的字符数，如果换成bytes，len()函数就计算字节数

	```
		len(b'ABC')
		len(b'\xe4\xb8\xad\xe6\x96\x87')
		len('中文'.encode('utf-8'))
	```

* 由于Python源代码也是一个文本文件，所以，当你的源代码中包含中文的时候，在保存源代码时，就需要务必指定保存为UTF-8编码。当Python解释器读取源代码时，为了让它按UTF-8编码读取，我们通常在文件开头写上这两行
	
	```
		#!/usr/bin/env python3
		# -*- coding: utf-8 -*-
	```

	第一行注释是为了告诉Linux/OS X系统，这是一个Python可执行程序，Windows系统会忽略这个注释；

	第二行注释是为了告诉Python解释器，按照UTF-8编码读取源代码，否则，你在源代码中写的中文输出可能会有乱码。

## 格式化

* 最后一个常见的问题是如何输出格式化的字符串。我们经常会输出类似'亲爱的xxx你好！你xx月的话费是xx，余额是xx'之类的字符串，而xxx的内容都是根据变量变化的，所以，需要一种简便的格式化字符串的方式。

* 在Python中，采用的格式化方式和C语言是一致的，用%实现，举例如下：

	```
		>>> 'Hello, %s' % 'world'
		'Hello, world'
		>>> 'Hi, %s, you have $%d.' % ('Michael', 1000000)
		'Hi, Michael, you have $1000000.'
	```

* %运算符就是用来格式化字符串的。在字符串内部，%s表示用字符串替换，%d表示用整数替换，有几个%?占位符，后面就跟几个变量或者值，顺序要对应好。如果只有一个%?，括号可以省略。

* 常见的占位符有 %d(整数) %f(浮点数) %s(字符串) %x(十六进制)

* 其中，格式化整数和浮点数还可以指定是否补0和整数与小数的位数

	```
		print('%2d-%02d' % (3, 1))
		print('%.2f' % 3.1415926)
	```

* 如果你不太确定应该用什么，%s永远起作用，它会把任何数据类型转换为字符串

* 有些时候，字符串里面的%是一个普通字符怎么办？这个时候就需要转义，用%%来表示一个%

	```
		print('growth rate: %d %%' % 7)
	```

* 另一种格式化字符串的方法是使用字符串的format()方法，它会用传入的参数依次替换字符串内的占位符{0}、{1}……，不过这种方式写起来比%要麻烦得多

	```
		>>> 'Hello, {0}, 成绩提升了 {1:.1f}%'.format('小明', 17.125)
	```

## list

* Python内置的一种数据类型是列表：list。list是一种有序的集合，可以随时添加和删除其中的元素

	```
		>>> classmates = ['Michael', 'Bob', 'Tracy']
		>>> classmates
		['Michael', 'Bob', 'Tracy']
	```

* 变量classmates就是一个list。用len()函数可以获得list元素的个数

	```
		>>> len(classmates)
		3
	```

* 用索引来访问list中每一个位置的元素，记得索引是从0开始的

	```
		>>> classmates[0]
		'Michael'
		>>> classmates[1]
		'Bob'
		>>> classmates[2]
		'Tracy'
		>>> classmates[3]
		Traceback (most recent call last):
		 File "<stdin>", line 1, in <module>
		IndexError: list index out of rangev
	```

* 记得最后一个元素的索引是len(classmates) - 1

* 如果要取最后一个元素，除了计算索引位置外，还可以用-1做索引，直接获取最后一个元素

	```
		>>> classmates[-1]
		'Tracy'
	```

* list是一个可变的有序表，所以，可以往list中追加元素到末尾：

	```
		>>> classmates.append('Adam')
		>>> classmates
		['Michael', 'Bob', 'Tracy', 'Adam']
	```

* 也可以把元素插入到指定的位置，比如索引号为1的位置

	```
		>>> classmates.insert(1, 'Jack')
		>>> classmates
		['Michael', 'Jack', 'Bob', 'Tracy', 'Adam']
	```

* 要删除list末尾的元素，用pop()方法

	```
		>>> classmates.pop()
		'Adam'
		>>> classmates
		['Michael', 'Jack', 'Bob', 'Tracy']
	```

* 要删除指定位置的元素，用pop(i)方法，其中i是索引位置

* 要把某个元素替换成别的元素，可以直接赋值给对应的索引位置

* list里面的元素的数据类型也可以不同，比如：

* >>> L = ['Apple', 123, True]

* list元素也可以是另一个list，比如：

	```
		>>> s = ['python', 'java', ['asp', 'php'], 'scheme']
		>>> len(s)
		4

		>>> p = ['asp', 'php']
		>>> s = ['python', 'java', p, 'scheme']
	```

* 如果一个list中一个元素也没有，就是一个空的list，它的长度为0：

	```
		>>> L = []
		>>> len(L)
		0
	```

