# 面向对象编程

## 类和实例

* 在Python中，定义类是通过class关键字：

	```
		class Student(object):
			pass
	```

* class后面紧接着是类名，即Student，类名通常是大写开头的单词，紧接着是(object)，表示该类是从哪个类继承下来的，通常，如果没有合适的继承类，就使用object类，这是所有类最终都会继承的类。

* 定义好了Student类，就可以根据Student类创建出Student的实例，创建实例是通过类名+()实现的：

	```
		>>> bart = Student()
		>>> bart
		<__main__.Student object at 0x10a67a590>
		>>> Student
		<class '__main__.Student'>
	```

* 可以自由地给一个实例变量绑定属性，比如，给实例bart绑定一个name属性：

	```
		>>> bart.name = 'Bart Simpson'
		>>> bart.name
		'Bart Simpson'
	```

* 由于类可以起到模板的作用，因此，可以在创建实例的时候，把一些我们认为必须绑定的属性强制填写进去。通过定义一个特殊的__init__方法，在创建实例的时候，就把name，score等属性绑上去：

	```
		class Student(object):

			def __init__(self, name, score):
				self.name = name
				self.score = score
	```

* **注意：特殊方法“__init__”前后分别有两个下划线！！！**

* 注意到__init__方法的第一个参数永远是self，表示创建的实例本身，因此，在__init__方法内部，就可以把各种属性绑定到self，因为self就指向创建的实例本身。(self -> this)

* 有了__init__方法，在创建实例的时候，就不能传入空的参数了，必须传入与__init__方法匹配的参数，但self不需要传，Python解释器自己会把实例变量传进去：

	```
		>>> bart = Student('Bart Simpson', 59)
		>>> bart.name
		'Bart Simpson'
		>>> bart.score
		59
	```

* 和普通的函数相比，在类中定义的函数只有一点不同，就是第一个参数永远是实例变量self，并且，调用时，不用传递该参数。除此之外，类的方法和普通函数没有什么区别，所以，你仍然可以用默认参数、可变参数、关键字参数和命名关键字参数。

* 可以在Student类的内部定义访问数据的函数，这样，就把“数据”给封装起来了。这些封装数据的函数是和Student类本身是关联起来的，我们称之为类的方法：

	```
		class Student(object):

			def __init__(self, name, score):
				self.name = name
				self.score = score

			def print_score(self):
				print('%s: %s' % (self.name, self.score))
	```

* 要定义一个方法，除了第一个参数是self外，其他和普通函数一样。要调用一个方法，只需要在实例变量上直接调用，除了self不用传递，其他参数正常传入：

	```
		>>> bart.print_score()
		Bart Simpson: 59
	```

* 这样一来，我们从外部看Student类，就只需要知道，创建实例需要给出name和score，而如何打印，都是在Student类的内部定义的，这些数据和逻辑被“封装”起来了，调用很容易，但却不用知道内部实现的细节。

* 封装的另一个好处是可以给Student类增加新的方法，比如get_grade：

	```
		class Student(object):
			...

			def get_grade(self):
				if self.score >= 90:
					return 'A'
				elif self.score >= 60:
					return 'B'
				else:
					return 'C'
	```

* 类是创建实例的模板，而实例则是一个一个具体的对象，各个实例拥有的数据都互相独立，互不影响。

* 和静态语言不同，Python允许对实例变量绑定任何数据，也就是说，对于两个实例变量，虽然它们都是同一个类的不同实例，但拥有的变量名称都可能不同：

	```
		>>> bart = Student('Bart Simpson', 59)
		>>> lisa = Student('Lisa Simpson', 87)
		>>> bart.age = 8
		>>> bart.age
		8
		>>> lisa.age
		Traceback (most recent call last):
		  File "<stdin>", line 1, in <module>
		AttributeError: 'Student' object has no attribute 'age'
	```

## 访问限制

* 如果要让内部属性不被外部访问，可以把属性的名称前加上两个下划线__，在Python中，实例的变量名如果以__开头，就变成了一个私有变量（private），只有内部可以访问，外部不能访问，所以，我们把Student类改一改：

	```
		class Student(object):

			def __init__(self, name, score):
				self.__name = name
				self.__score = score

			def print_score(self):
				print('%s: %s' % (self.__name, self.__score))
	```

* 但是如果外部代码要获取name和score怎么办？可以给Student类增加get_name和get_score这样的方法：

	```
		class Student(object):
			...

			def get_name(self):
				return self.__name

			def get_score(self):
				return self.__score
	```

* 如果又要允许外部代码修改score怎么办？可以再给Student类增加set_score方法：

	```
		class Student(object):
			...

			def set_score(self, score):
				self.__score = score
	```

* 需要注意的是，在Python中，变量名类似__xxx__的，也就是以双下划线开头，并且以双下划线结尾的，是特殊变量，特殊变量是可以直接访问的，不是private变量，所以，不能用__name__、__score__这样的变量名。

* 有些时候，你会看到以一个下划线开头的实例变量名，比如_name，这样的实例变量外部是可以访问的，但是，按照约定俗成的规定，当你看到这样的变量时，意思就是，“虽然我可以被访问，但是，请把我视为私有变量，不要随意访问”。

* 双下划线开头的实例变量是不是一定不能从外部访问呢？其实也不是。不能直接访问__name是因为Python解释器对外把__name变量改成了_Student__name，所以，仍然可以通过_Student__name来访问__name变量：


	```
		>>> bart._Student__name
		'Bart Simpson'
	```

* 但是强烈建议你不要这么干，因为不同版本的Python解释器可能会把__name改成不同的变量名。

* 总的来说就是，Python本身没有任何机制阻止你干坏事，一切全靠自觉。

* 最后注意下面的这种错误写法：

	```
		>>> bart = Student('Bart Simpson', 59)
		>>> bart.get_name()
		'Bart Simpson'
		>>> bart.__name = 'New Name' # 设置__name变量！
		>>> bart.__name
		'New Name'
	```

* 表面上看，外部代码“成功”地设置了__name变量，但实际上这个__name变量和class内部的__name变量不是一个变量！内部的__name变量已经被Python解释器自动改成了_Student__name，而外部代码给bart新增了一个__name变量。不信试试：

	```
		>>> bart.get_name() # get_name()内部返回self.__name
		'Bart Simpson'
	```

## 继承和多态

* 我们已经编写了一个名为Animal的class，有一个run()方法可以直接打印：

	```
		class Animal(object):
			def run(self):
				print('Animal is running...')
	```

* 当我们需要编写Dog和Cat类时，就可以直接从Animal类继承：

	```
		class Dog(Animal):
			pass

		class Cat(Animal):
			pass
	```

* 继承有什么好处？最大的好处是子类获得了父类的全部功能。由于Animial实现了run()方法，因此，Dog和Cat作为它的子类，什么事也没干，就自动拥有了run()方法：

	```
		dog = Dog()
		dog.run()

		cat = Cat()
		cat.run()
	```

* 运行结果如下：

	```
		Animal is running...
		Animal is running...
	```

* 也可以对run方法进行重写:

	```
		class Dog(Animal):

			def run(self):
				print('Dog is running...')

		class Cat(Animal):

			def run(self):
				print('Cat is running...')
	```

* 当子类和父类都存在相同的run()方法时，我们说，子类的run()覆盖了父类的run()，在代码运行的时候，总是会调用子类的run()。这样，我们就获得了继承的另一个好处：多态。

* 判断一个变量是否是某个类型可以用isinstance()判断：

	```
		>>> isinstance(a, list)
		True
		>>> isinstance(b, Animal)
		True
		>>> isinstance(c, Dog)
		True
	```

* 但是等等，试试：

	```
		>>> isinstance(c, Animal)
		True
	```

* 看来c不仅仅是Dog，c还是Animal！

* 对于Python这样的动态语言来说，则不一定需要传入Animal类型。我们只需要保证传入的对象有一个run()方法就可以了：

	```
		class Timer(object):
			def run(self):
				print('Start...')
	```

* 这就是动态语言的“鸭子类型”，它并不要求严格的继承体系，一个对象只要“看起来像鸭子，走起路来像鸭子”，那它就可以被看做是鸭子。

* 动态语言的鸭子类型特点决定了继承不像静态语言那样是必须的。

## 获取对象信息

* 当我们拿到一个对象的引用时，如何知道这个对象是什么类型、有哪些方法呢？

* 基本类型都可以用type()判断：

	```
		>>> type(123)
		<class 'int'>
		>>> type('str')
		<class 'str'>
		>>> type(None)
		<type(None) 'NoneType'>
	```

* 如果一个变量指向函数或者类，也可以用type()判断：

	```
		>>> type(abs)
		<class 'builtin_function_or_method'>
		>>> type(a)
		<class '__main__.Animal'>
	```

* 但是type()函数返回的是什么类型呢？它返回对应的Class类型。如果我们要在if语句中判断，就需要比较两个变量的type类型是否相同：

	```
		>>> type(123)==type(456)
		True
		>>> type(123)==int
		True
		>>> type('abc')==type('123')
		True
		>>> type('abc')==str
		True
		>>> type('abc')==type(123)
		False
	```

* 判断基本数据类型可以直接写int，str等，但如果要判断一个对象是否是函数怎么办？可以使用types模块中定义的常量：

	```
		>>> import types
		>>> def fn():
		...     pass
		...
		>>> type(fn)==types.FunctionType
		True
		>>> type(abs)==types.BuiltinFunctionType
		True
		>>> type(lambda x: x)==types.LambdaType
		True
		>>> type((x for x in range(10)))==types.GeneratorType
		True
	```

* 对于class的继承关系来说，使用type()就很不方便。我们要判断class的类型，可以使用isinstance()函数。

* 能用type()判断的基本类型也可以用isinstance()判断：

	```
		>>> isinstance('a', str)
		True
		>>> isinstance(123, int)
		True
		>>> isinstance(b'a', bytes)
		True
	```

* 并且还可以判断一个变量是否是某些类型中的一种，比如下面的代码就可以判断是否是list或者tuple：

	```
		>>> isinstance([1, 2, 3], (list, tuple))
		True
		>>> isinstance((1, 2, 3), (list, tuple))
		True
	```

* **总是优先使用isinstance()判断类型，可以将指定类型及其子类“一网打尽”。**

* 如果要获得一个对象的所有属性和方法，可以使用dir()函数，它返回一个包含字符串的list，比如，获得一个str对象的所有属性和方法：

	```
		>>> dir('ABC')
		['__add__', '__class__',..., '__subclasshook__', 'capitalize', 'casefold',..., 'zfill']
	```

* 类似__xxx__的属性和方法在Python中都是有特殊用途的，比如__len__方法返回长度。在Python中，如果你调用len()函数试图获取一个对象的长度，实际上，在len()函数内部，它自动去调用该对象的__len__()方法，所以，下面的代码是等价的：

	```
		>>> len('ABC')
		3
		>>> 'ABC'.__len__()
		3
	```

* 我们自己写的类，如果也想用len(myObj)的话，就自己写一个__len__()方法：

	```
		>>> class MyDog(object):
		...     def __len__(self):
		...         return 100
		...
		>>> dog = MyDog()
		>>> len(dog)
		100
	```

* 剩下的都是普通属性或方法，比如lower()返回小写的字符串：

	```
		>>> 'ABC'.lower()
		'abc'
	```

* getattr(obj, 'attr', 404) -- 获得obj的attr属性，属性不存在则返回404

* setattr(obj, 'attr', 'value') -- 向obj中添加属性attr，值为value

* hasattr(obj, 'attr') -- 判断obj中是否有attr属性


## 实例属性和类属性

* 由于Python是动态语言，根据类创建的实例可以任意绑定属性。

	```
		class Student(object):
			def __init__(self, name):
				self.name = name

		s = Student('Bob')
		s.score = 90
	```

* 但是，如果Student类本身需要绑定一个属性呢？可以直接在class中定义属性，这种属性是类属性，归Student类所有：

	```
		class Student(object):
			name = 'Student'
	```

* 当我们定义了一个类属性后，这个属性虽然归类所有，但类的所有实例都可以访问到。来测试一下：

	```
		>>> class Student(object):
		...     name = 'Student'
		...
		>>> s = Student() # 创建实例s
		>>> print(s.name) # 打印name属性，因为实例并没有name属性，所以会继续查找class的name属性
		Student
		>>> print(Student.name) # 打印类的name属性
		Student
		>>> s.name = 'Michael' # 给实例绑定name属性
		>>> print(s.name) # 由于实例属性优先级比类属性高，因此，它会屏蔽掉类的name属性
		Michael
		>>> print(Student.name) # 但是类属性并未消失，用Student.name仍然可以访问
		Student
		>>> del s.name # 如果删除实例的name属性
		>>> print(s.name) # 再次调用s.name，由于实例的name属性没有找到，类的name属性就显示出来了
		Student
	```

* 可以通过 del 来删除实例的某个属性

* 从上面的例子可以看出，在编写程序的时候，千万不要对实例属性和类属性使用相同的名字，因为相同名称的实例属性将屏蔽掉类属性，但是当你删除实例属性后，再使用相同的名称，访问到的将是类属性。

* 如果是调用类属性需要在属性名前加类名. 例：Student.count

* 实例属性属于各个实例所有，互不干扰；

* 类属性属于类所有，所有实例共享一个属性；

* 不要对实例属性和类属性使用相同的名字，否则将产生难以发现的错误。

