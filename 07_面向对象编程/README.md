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




## 获取对象信息





## 实例属性和类属性










