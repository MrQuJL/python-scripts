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



## 使用枚举类



## 使用元类


