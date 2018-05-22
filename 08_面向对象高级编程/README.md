# 面向对象高级编程

## 使用__slots__

* 正常情况下，当我们定义了一个class，创建了一个class的实例后，我们可以给该实例绑定任何属性和方法，这就是动态语言的灵活性。先定义class：

	```
		class Student(object):
			pass
	```

* 然后，尝试给实例绑定一个属性：

	```
		>>> s = Student()
		>>> s.name = 'Michael' # 动态给实例绑定一个属性
		>>> print(s.name)
		Michael
	```

* 还可以使用types模块中的MethodType方法来绑定方法:

	```
		>>> def set_age(self, age): # 定义一个函数作为实例方法
		...     self.age = age
		...
		>>> from types import MethodType
		>>> s.set_age = MethodType(set_age, s) # 给实例绑定一个方法
		>>> s.set_age(25) # 调用实例方法
		>>> s.age # 测试结果
		25
	```

* 但是，给一个实例绑定的方法，对另一个实例是不起作用的：

	```
		>>> s2 = Student() # 创建新的实例
		>>> s2.set_age(25) # 尝试调用方法
		Traceback (most recent call last):
		  File "<stdin>", line 1, in <module>
		AttributeError: 'Student' object has no attribute 'set_age'
	```

* 为了给所有实例都绑定方法，可以给class绑定方法：

	```
		>>> def set_score(self, score):
		...     self.score = score
		...
		>>> Student.set_score = set_score
	```

* 给class绑定方法后，所有实例均可调用.

* 但是，如果我们想要限制实例的属性怎么办？比如，只允许对Student实例添加name和age属性或者方法

* 为了达到限制的目的，Python允许在定义class的时候，定义一个特殊的__slots__变量，来限制该class实例能添加的属性或方法：

	```
		class Student(object):
			__slots__ = ('name', 'age') # 用tuple定义允许绑定的属性名称
	```

* 使用__slots__要注意，__slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的：

	```
		>>> class GraduateStudent(Student):
		...     pass
		...
		>>> g = GraduateStudent()
		>>> g.score = 9999
	```

* 除非在子类中也定义__slots__，这样，子类实例允许定义的属性就是自身的__slots__加上父类的__slots__。

## 使用@property

* 为了限制类中属性的赋值，需要定义setter，getter方法，然后调用setter和getter方法来实现，那么有没有不调用方法有能实现对参数的限制呢？

* Python内置的@property装饰器就是负责把一个方法变成属性调用的：

	```
		class Student(object):

			@property
			def score(self):
				return self._score

			@score.setter
			def score(self, value):
				if not isinstance(value, int):
					raise ValueError('score must be an integer!')
				if value < 0 or value > 100:
					raise ValueError('score must between 0 ~ 100!')
				self._score = value
	```

* @property的实现比较复杂，我们先考察如何使用。把一个getter方法变成属性，只需要加上@property就可以了，此时，@property本身又创建了另一个装饰器@score.setter，负责把一个setter方法变成属性赋值，于是，我们就拥有一个可控的属性操作：

	```
		>>> s = Student()
		>>> s.score = 60 # OK，实际转化为s.set_score(60)
		>>> s.score # OK，实际转化为s.get_score()
		60
		>>> s.score = 9999
		Traceback (most recent call last):
		  ...
		ValueError: score must between 0 ~ 100!
	```

* 注意到这个神奇的@property，我们在对实例属性操作的时候，就知道该属性很可能不是直接暴露的，而是通过getter和setter方法来实现的。

* 还可以定义只读属性，只定义getter方法，不定义setter方法就是一个只读属性：

	```
		class Student(object):

			@property
			def birth(self):
				return self._birth

			@birth.setter
			def birth(self, value):
				self._birth = value

			@property
			def age(self):
				return 2015 - self._birth
	```

* 上面的birth是可读写属性，而age就是一个只读属性，因为age可以根据birth和当前时间计算出来。

* @property广泛应用在类的定义中，可以让调用者写出简短的代码，同时保证对参数进行必要的检查，这样，程序运行时就减少了出错的可能性。

## 多重继承

* python支持多继承，写法：

	```
		class Bat(Mammal, Flyable):
			pass
	```

* 在设计类的继承关系时，通常，主线都是单一继承下来的，例如，Ostrich继承自Bird。但是，如果需要“混入”额外的功能，通过多重继承就可以实现，比如，让Ostrich除了继承自Bird外，再同时继承Runnable。这种设计通常称之为**MixIn**。

* 为了更好地看出继承关系，我们把Runnable和Flyable改为RunnableMixIn和FlyableMixIn。类似的，你还可以定义出肉食动物CarnivorousMixIn和植食动物HerbivoresMixIn，让某个动物同时拥有好几个MixIn：

	```
		class Dog(Mammal, RunnableMixIn, CarnivorousMixIn):
			pass
	```

* MixIn的目的就是给一个类增加多个功能，这样，在设计类的时候，我们优先考虑通过多重继承来组合多个MixIn的功能，而不是设计多层次的复杂的继承关系。

* Python自带的很多库也使用了MixIn。举个例子，Python自带了TCPServer和UDPServer这两类网络服务，而要同时服务多个用户就必须使用多进程或多线程模型，这两种模型由ForkingMixIn和ThreadingMixIn提供。通过组合，我们就可以创造出合适的服务来。

* 比如，编写一个多进程模式的TCP服务，定义如下：

	```
		class MyTCPServer(TCPServer, ForkingMixIn):
			pass
	```

* 编写一个多线程模式的UDP服务，定义如下：

	```
		class MyUDPServer(UDPServer, ThreadingMixIn):
			pass
	```

* 如果你打算搞一个更先进的协程模型，可以编写一个CoroutineMixIn：

	```
		class MyTCPServer(TCPServer, CoroutineMixIn):
			pass
	```

* 这样一来，我们不需要复杂而庞大的继承链，只要选择组合不同的类的功能，就可以快速构造出所需的子类。

* 由于Python允许使用多重继承，因此，MixIn就是一种常见的设计。

* 只允许单一继承的语言（如Java）不能使用MixIn的设计。

## 定制类

### __str__

* 功能类似 Java 中的 toString

	```
		>>> class Student(object):
		...     def __init__(self, name):
		...         self.name = name
		...     def __str__(self):
		...         return 'Student object (name: %s)' % self.name
		...
		>>> print(Student('Michael'))
		Student object (name: Michael)
	```

* 但是细心的朋友会发现直接敲变量不用print，打印出来的实例还是不好看：

	```
		>>> s = Student('Michael')
		>>> s
		<__main__.Student object at 0x109afb310>
	```

* 这是因为直接显示变量调用的不是__str__()，而是__repr__()，两者的区别是__str__()返回用户看到的字符串，而__repr__()返回程序开发者看到的字符串，也就是说，__repr__()是为调试服务的。

* 解决办法是再定义一个__repr__()。但是通常__str__()和__repr__()代码都是一样的，所以，有个偷懒的写法：

	```
		class Student(object):
			def __init__(self, name):
				self.name = name
			def __str__(self):
				return 'Student object (name=%s)' % self.name
			__repr__ = __str__
	```

### __iter__

* 如果一个类想被用于for ... in循环，类似list或tuple那样，就必须实现一个__iter__()方法，该方法返回一个迭代对象，然后，Python的for循环就会不断调用该迭代对象的__next__()方法拿到循环的下一个值，直到遇到StopIteration错误时退出循环。

* 我们以斐波那契数列为例，写一个Fib类，可以作用于for循环：

	```
		class Fib(object):
			def __init__(self):
				self.a, self.b = 0, 1 # 初始化两个计数器a，b

			def __iter__(self):
				return self # 实例本身就是迭代对象，故返回自己

			def __next__(self):
				self.a, self.b = self.b, self.a + self.b # 计算下一个值
				if self.a > 100000: # 退出循环的条件
					raise StopIteration()
				return self.a # 返回下一个值
	```

* 现在，试试把Fib实例作用于for循环：

	```
		>>> for n in Fib():
		...     print(n)
		...
		1
		1
		2
		3
		5
		...
		46368
		75025
	```

### __getitem__

* Fib实例虽然能作用于for循环，看起来和list有点像，但是，把它当成list来使用还是不行，比如，取第5个元素：

	```
		>>> Fib()[5]
		Traceback (most recent call last):
		  File "<stdin>", line 1, in <module>
		TypeError: 'Fib' object does not support indexing
	```

* 要表现得像list那样按照下标取出元素，需要实现__getitem__()方法：

	```
		class Fib(object):
			def __getitem__(self, n):
				a, b = 1, 1
				for x in range(n):
					a, b = b, a + b
				return a
	```

* 现在，就可以按下标访问数列的任意一项了：

	```
		>>> f = Fib()
		>>> f[0]
		1
		>>> f[1]
		1
		>>> f[2]
		2
		>>> f[3]
		3
		>>> f[10]
		89
		>>> f[100]
		573147844013817084101
	```

* 但是list有个神奇的切片方法：

	```
		>>> list(range(100))[5:10]
		[5, 6, 7, 8, 9]
	```

* 对于Fib却报错。原因是__getitem__()传入的参数可能是一个int，也可能是一个切片对象slice，所以要做判断：

	```
		class Fib(object):
			def __getitem__(self, n):
				if isinstance(n, int): # n是索引
					a, b = 1, 1
					for x in range(n):
						a, b = b, a + b
					return a
				if isinstance(n, slice): # n是切片
					start = n.start
					stop = n.stop
					if start is None:
						start = 0
					a, b = 1, 1
					L = []
					for x in range(stop):
						if x >= start:
							L.append(a)
						a, b = b, a + b
					return L
	```

* 现在试试Fib的切片：

	```
		>>> f = Fib()
		>>> f[0:5]
		[1, 1, 2, 3, 5]
		>>> f[:10]
		[1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
	```

* 但是没有对step参数作处理：

	```
		>>> f[:10:2]
		[1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
	```

* 也没有对负数作处理，所以，要正确实现一个__getitem__()还是有很多工作要做的。

* 总之，通过上面的方法，我们自己定义的类表现得和Python自带的list、tuple、dict没什么区别，这完全归功于动态语言的“鸭子类型”，不需要强制继承某个接口。

### __getattr__

* 正常情况下，当我们调用类的方法或属性时，如果不存在，就会报错。比如定义Student类：

	```
		class Student(object):

			def __init__(self):
				self.name = 'Michael'
	```

* 调用name属性，没问题，但是，调用不存在的score属性，就有问题了：

	```
		>>> s = Student()
		>>> print(s.name)
		Michael
		>>> print(s.score)
		Traceback (most recent call last):
		  ...
		AttributeError: 'Student' object has no attribute 'score'
	```

* 错误信息很清楚地告诉我们，没有找到score这个attribute。

* 要避免这个错误，除了可以加上一个score属性外，Python还有另一个机制，那就是写一个__getattr__()方法，动态返回一个属性。修改如下：

	```
		class Student(object):

			def __init__(self):
				self.name = 'Michael'

			def __getattr__(self, attr):
				if attr=='score':
					return 99
	```

* 当调用不存在的属性时，比如score，Python解释器会试图调用__getattr__(self, 'score')来尝试获得属性，这样，我们就有机会返回score的值：

	```
		>>> s = Student()
		>>> s.name
		'Michael'
		>>> s.score
		99
	```

* 返回函数也是完全可以的：

	```
		class Student(object):

			def __getattr__(self, attr):
				if attr=='age':
					return lambda: 25
	```

* 只是调用方式要变为：

	```
		>>> s.age()
		25
	```

* 注意，只有在没有找到属性的情况下，才调用__getattr__，已有的属性，比如name，不会在__getattr__中查找。

* 此外，注意到任意调用如s.abc都会返回None，这是因为我们定义的__getattr__默认返回就是None。要让class只响应特定的几个属性，我们就要按照约定，抛出AttributeError的错误：

	```
		class Student(object):

			def __getattr__(self, attr):
				if attr=='age':
					return lambda: 25
				raise AttributeError('\'Student\' object has no attribute \'%s\'' % attr)
	```

* 这实际上可以把一个类的所有属性和方法调用全部动态化处理了，不需要任何特殊手段。

### __call__

* 任何类，只需要定义一个__call__()方法，就可以直接对实例进行调用。请看示例：

	```
		class Student(object):
			def __init__(self, name):
				self.name = name

			def __call__(self):
				print('My name is %s.' % self.name)
	```

* 调用方式如下：

	```
		>>> s = Student('Michael')
		>>> s() # self参数不要传入
		My name is Michael.
	```

* __call__()还可以定义参数。对实例进行直接调用就好比对一个函数进行调用一样，所以你完全可以把对象看成函数，把函数看成对象，因为这两者之间本来就没啥根本的区别。

* 那么，怎么判断一个变量是对象还是函数呢？其实，更多的时候，我们需要判断一个对象是否能被调用，能被调用的对象就是一个Callable对象，比如函数和我们上面定义的带有__call__()的类实例：

	```
		>>> callable(Student())
		True
		>>> callable(max)
		True
		>>> callable([1, 2, 3])
		False
		>>> callable(None)
		False
		>>> callable('str')
		False
	```

* 通过callable()函数，我们就可以判断一个对象是否是“可调用”对象。

* Python的class允许定义许多定制方法，可以让我们非常方便地生成特定的类。

## 使用枚举类

* 当我们需要定义常量时，一个办法是用大写变量通过整数来定义，例如月份：

	```
		JAN = 1
		FEB = 2
		MAR = 3
		...
		NOV = 11
		DEC = 12
	```

* 好处是简单，缺点是类型是int，并且仍然是变量。

* 更好的方法是为这样的枚举类型定义一个class类型，然后，每个常量都是class的一个唯一实例。Python提供了Enum类来实现这个功能：

	```
		from enum import Enum

		Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
	```

* 这样我们就获得了Month类型的枚举类，可以直接使用Month.Jan来引用一个常量，或者枚举它的所有成员：

	```
		for name, member in Month.__members__.items():
			print(name, '=>', member, ',', member.value)
	```

* value属性则是自动赋给成员的int常量，默认从1开始计数。

* 如果需要更精确地控制枚举类型，可以从Enum派生出自定义类：

	```
		from enum import Enum, unique

		@unique
		class Weekday(Enum):
			Sun = 0 # Sun的value被设定为0
			Mon = 1
			Tue = 2
			Wed = 3
			Thu = 4
			Fri = 5
			Sat = 6
	```

## 使用元类

* python允许在程序运行的时候动态的创建类

* 我们说class的定义是运行时动态创建的，而创建class的方法就是使用type()函数。

* type()函数既可以返回一个对象的类型，又可以创建出新的类型，比如，我们可以通过type()函数创建出Hello类，而无需通过class Hello(object)...的定义：

	```
		>>> def fn(self, name='world'): # 先定义函数
		...     print('Hello, %s.' % name)
		...
		>>> Hello = type('Hello', (object,), dict(hello=fn)) # 创建Hello class
		>>> h = Hello()
		>>> h.hello()
		Hello, world.
		>>> print(type(Hello))
		<class 'type'>
		>>> print(type(h))
		<class '__main__.Hello'>
	```

* 要创建一个class对象，type()函数依次传入3个参数：

1. class的名称；
2. 继承的父类集合，注意Python支持多重继承，如果只有一个父类，别忘了tuple的单元素写法；
3. class的方法名称与函数绑定，这里我们把函数fn绑定到方法名hello上。

* 通过type()函数创建的类和直接写class是完全一样的，因为Python解释器遇到class定义时，仅仅是扫描一下class定义的语法，然后调用type()函数创建出class。

* 正常情况下，我们都用class Xxx...来定义类，但是，type()函数也允许我们动态创建出类来，也就是说，动态语言本身支持运行期动态创建类，这和静态语言有非常大的不同，要在静态语言运行期创建类，必须构造源代码字符串再调用编译器，或者借助一些工具生成字节码实现，本质上都是动态编译，会非常复杂。

* 除了使用type()动态创建类以外，要控制类的创建行为，还可以使用metaclass。这里就不多解释了，基本用不到。


