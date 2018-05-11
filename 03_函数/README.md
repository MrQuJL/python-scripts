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


## 递归函数


