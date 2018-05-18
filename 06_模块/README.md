# 模块

* 为了编写可维护的代码，我们把很多函数分组，分别放到不同的文件里，这样，每个文件包含的代码就相对较少，很多编程语言都采用这种组织代码的方式。在Python中，一个.py文件就称之为一个模块（Module）。

* 举个例子，一个```abc.py```的文件就是一个名字叫```abc```的模块，一个```xyz.py```的文件就是一个名字叫```xyz```的模块。

* 现在，假设我们的abc和xyz这两个模块名字与其他模块冲突了，于是我们可以通过包来组织模块，避免冲突。方法是选择一个顶层包名，比如mycompany，按照如下目录存放：

mycompany
├─ __init__.py
├─ abc.py
└─ xyz.py

* 引入了包以后，只要顶层的包名不与别人冲突，那所有模块都不会与别人冲突。现在，abc.py模块的名字就变成了mycompany.abc，类似的，xyz.py的模块名变成了mycompany.xyz。

* 请注意，每一个包目录下面都会有一个__init__.py的文件，这个文件是必须存在的，否则，Python就把这个目录当成普通目录，而不是一个包。__init__.py可以是空文件，也可以有Python代码，因为__init__.py本身就是一个模块，而它的模块名就是mycompany。

* 类似的，可以有多级目录，组成多级层次的包结构。比如如下的目录结构：

mycompany
 ├─ web
 │  ├─ __init__.py
 │  ├─ utils.py
 │  └─ www.py
 ├─ __init__.py
 ├─ abc.py
 └─ utils.py

* 文件www.py的模块名就是mycompany.web.www，两个文件utils.py的模块名分别是mycompany.utils和mycompany.web.utils。

* 自己创建模块时要注意命名，不能和Python自带的模块名称冲突。例如，系统自带了sys模块，自己的模块就不可命名为sys.py，否则将无法导入系统自带的sys模块。

* 模块名不要和系统模块名冲突，最好先查看系统是否已存在该模块，检查方法是在Python交互环境执行```import abc```，若成功则说明系统存在此模块。

## 使用模块

* 一个标准的模块头如下：

	```
		#!/usr/bin/env python3
		# -*- coding: utf-8 -*-

		' a test module '

		__author__ = 'Michael Liao'

		def test():
			pass
		...
		if __name__=='__main__':
			test()
	```

* 第1行和第2行是标准注释，第1行注释可以让这个hello.py文件直接在Unix/Linux/Mac上运行，第2行注释表示.py文件本身使用标准UTF-8编码；

* 第4行是一个字符串，表示模块的文档注释，任何模块代码的第一个字符串都被视为模块的文档注释；

* 第6行使用__author__变量把作者写进去，这样当你公开源代码后别人就可以瞻仰你的大名；

* 以上就是Python模块的标准文件模板，当然也可以全部删掉不写，但是，按标准办事肯定没错。

* sys模块有一个argv变量，用list存储了命令行的所有参数。argv至少有一个元素，因为第一个参数永远是该.py文件的名称，例如：

* 运行python3 hello.py获得的sys.argv就是['hello.py']；

* 运行python3 hello.py MrQuJL获得的sys.argv就是['hello.py', 'MrQuJL']。

* 最后，注意到这两行代码：

	```
		if __name__=='__main__':
			test()
	```

* 当我们在命令行运行hello模块文件时，Python解释器把一个特殊变量__name__置为__main__，而如果在其他地方导入该hello模块时，if判断将失败，因此，这种if测试可以让一个模块通过命令行运行时执行一些额外的代码，最常见的就是运行测试。

* 我们可以用命令行运行hello.py看看效果：

	```
		$ python3 hello.py
		Hello, world!
		$ python hello.py MrQuJL
		Hello, MrQuJL!
	```

* 如果启动Python交互环境，再导入hello模块：

	```
		$ python3
		Python 3.4.3 (v3.4.3:9b73f1c3e601, Feb 23 2015, 02:52:03) 
		[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
		Type "help", "copyright", "credits" or "license" for more information.
		>>> import hello
		>>>
	```

* 导入时，没有打印Hello, word!，因为没有执行test()函数。

* 调用hello.test()时，才能打印出Hello, word!：

	```
		>>> hello.test()
		Hello, world!
	```

## 作用域

* 在一个模块中，我们可能会定义很多函数和变量，但有的函数和变量我们希望给别人使用，有的函数和变量我们希望仅仅在模块内部使用。在Python中，是通过_前缀来实现的。

* 类似_xxx和__xxx这样的函数或变量就是非公开的（private），不应该被直接引用，比如_abc，__abc等；

* 之所以我们说，private函数和变量“不应该”被直接引用，而不是“不能”被直接引用，是因为Python并没有一种方法可以完全限制访问private函数或变量，但是，从编程习惯上不应该引用private函数或变量。

* private函数或变量不应该被别人引用，那它们有什么用呢？请看例子：

	```
		def _private_1(name):
			return 'Hello, %s' % name

		def _private_2(name):
			return 'Hi, %s' % name

		def greeting(name):
			if len(name) > 3:
				return _private_1(name)
			else:
				return _private_2(name)
	```

* 我们在模块里公开greeting()函数，而把内部逻辑用private函数隐藏起来了，这样，调用greeting()函数不用关心内部的private函数细节，这也是一种非常有用的代码封装和抽象的方法，即：

* 外部不需要引用的函数全部定义成private，只有外部需要引用的函数才定义为public。



