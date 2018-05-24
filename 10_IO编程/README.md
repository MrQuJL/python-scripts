# IO编程

## 文件读写

### 读文件

* 要以读文件的模式打开一个文件对象，使用Python内置的open()函数，传入文件名和标示符：

	```
		>>> f = open('/Users/michael/test.txt', 'r')
	```

* 标示符'r'表示读，这样，我们就成功地打开了一个文件。

* 注：文件分隔符为 '\\' 或 '/'

* 如果文件打开成功，接下来，调用read()方法可以一次读取文件的全部内容，Python把内容读到内存，用一个str对象表示：

	```
		>>> f.read()
		'Hello, world!'
	```

* 最后一步是调用close()方法关闭文件。文件使用完毕后必须关闭，因为文件对象会占用操作系统的资源，并且操作系统同一时间能打开的文件数量也是有限的：

	```
		>>> f.close()
	```

* 由于文件读写时都有可能产生IOError，一旦出错，后面的f.close()就不会调用。所以，为了保证无论是否出错都能正确地关闭文件，我们可以使用try ... finally来实现：

	```
		try:
			f = open('/path/to/file', 'r')
			print(f.read())
		finally:
			if f:
				f.close()
	```

* 但是每次都这么写实在太繁琐，所以，Python引入了with语句来自动帮我们调用close()方法：

	```
		with open('/path/to/file', 'r') as f:
			print(f.read())
	```

* 这和前面的try ... finally是一样的，但是代码更佳简洁，并且不必调用f.close()方法。

* 调用read()会一次性读取文件的全部内容，如果文件有10G，内存就爆了，所以，要保险起见，可以反复调用read(size)方法，每次最多读取size个字节的内容。另外，调用readline()可以每次读取一行内容，调用readlines()一次读取所有内容并按行返回list。因此，要根据需要决定怎么调用。

* 如果文件很小，read()一次性读取最方便；如果不能确定文件大小，反复调用read(size)比较保险；如果是配置文件，调用readlines()最方便：

	```
		for line in f.readlines():
			print(line.strip()) # 把末尾的'\n'删掉
	```

### file-like Object

* 像open()函数返回的这种有个read()方法的对象，在Python中统称为file-like Object。除了file外，还可以是内存的字节流，网络流，自定义流等等。file-like Object不要求从特定类继承，只要写个read()方法就行。

* StringIO就是在内存中创建的file-like Object，常用作临时缓冲。

### 二进制文件

* 前面讲的默认都是读取文本文件，并且是UTF-8编码的文本文件。要读取二进制文件，比如图片、视频等等，用'rb'模式打开文件即可：

	```
		>>> f = open('/Users/michael/test.jpg', 'rb')
		>>> f.read()
		b'\xff\xd8\xff\xe1\x00\x18Exif\x00\x00...' # 十六进制表示的字节
	```

### 字符编码

* 要读取非UTF-8编码的文本文件，需要给open()函数传入encoding参数，例如，读取GBK编码的文件：

	```
		>>> f = open('/Users/michael/gbk.txt', 'r', encoding='gbk')
		>>> f.read()
		'测试'
	```

* 遇到有些编码不规范的文件，你可能会遇到UnicodeDecodeError，因为在文本文件中可能夹杂了一些非法编码的字符。遇到这种情况，open()函数还接收一个errors参数，表示如果遇到编码错误后如何处理。最简单的方式是直接忽略：

	```
		>>> f = open('/Users/michael/gbk.txt', 'r', encoding='gbk', errors='ignore')
	```

### 写文件

* 写文件和读文件是一样的，唯一区别是调用open()函数时，传入标识符'w'或者'wb'表示写文本文件或写二进制文件：

	```
		>>> f = open('/Users/michael/test.txt', 'w')
		>>> f.write('Hello, world!')
		>>> f.close()
	```

* 你可以反复调用write()来写入文件，但是务必要调用f.close()来关闭文件。当我们写文件时，操作系统往往不会立刻把数据写入磁盘，而是放到内存缓存起来，空闲的时候再慢慢写入。只有调用close()方法时，操作系统才保证把没有写入的数据全部写入磁盘。忘记调用close()的后果是数据可能只写了一部分到磁盘，剩下的丢失了。所以，还是用with语句来得保险：

	```
		with open('/Users/michael/test.txt', 'w') as f:
			f.write('Hello, world!')
	```

* 要写入特定编码的文本文件，请给open()函数传入encoding参数，将字符串自动转换成指定编码。

* 细心的童鞋会发现，以'w'模式写入文件时，如果文件已存在，会直接覆盖（相当于删掉后新写入一个文件）。如果我们希望追加到文件末尾怎么办？可以传入'a'以追加（append）模式写入。

* 模式的定义如下：

Character	Meaning
'r'	open for reading (default)
'w'	open for writing, truncating the file first
'x'	open for exclusive creation, failing if the file already exists
'a'	open for writing, appending to the end of the file if it exists
'b'	binary mode
't'	text mode (default)
'+'	open a disk file for updating (reading and writing)
'U'	universal newlines mode (deprecated)

## StringIO和BytesIO

### StringIO

* 很多时候，数据读写不一定是文件，也可以在内存中读写。

* StringIO顾名思义就是在内存中读写str。

* 要把str写入StringIO，我们需要先创建一个StringIO，然后，像文件一样写入即可：

	```
		>>> from io import StringIO
		>>> f = StringIO()
		>>> f.write('hello')
		5
		>>> f.write(' ')
		1
		>>> f.write('world!')
		6
		>>> print(f.getvalue())
		hello world!
	```

* getvalue()方法用于获得写入后的str。

* 要读取StringIO，可以用一个str初始化StringIO，然后，像读文件一样读取：

	```
		>>> from io import StringIO
		>>> f = StringIO('Hello!\nHi!\nGoodbye!')
		>>> while True:
		...     s = f.readline()
		...     if s == '':
		...         break
		...     print(s.strip())
		...
		Hello!
		Hi!
		Goodbye!
	```

### BytesIO

* StringIO操作的只能是str，如果要操作二进制数据，就需要使用BytesIO。

* BytesIO实现了在内存中读写bytes，我们创建一个BytesIO，然后写入一些bytes：

	```
		>>> from io import BytesIO
		>>> f = BytesIO()
		>>> f.write('中文'.encode('utf-8'))
		6
		>>> print(f.getvalue())
		b'\xe4\xb8\xad\xe6\x96\x87'
	```

* 请注意，写入的不是str，而是经过UTF-8编码的bytes。

* 和StringIO类似，可以用一个bytes初始化BytesIO，然后，像读文件一样读取：

	```
		>>> from io import BytesIO
		>>> f = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
		>>> f.read()s
		b'\xe4\xb8\xad\xe6\x96\x87'
	```

* StringIO和BytesIO是在内存中操作str和bytes的方法，使得和读写文件具有一致的接口。

## 操作文件和目录

* 如果要在Python程序中执行这些目录和文件的操作怎么办？其实操作系统提供的命令只是简单地调用了操作系统提供的接口函数，Python内置的os模块也可以直接调用操作系统提供的接口函数。

	```
		>>> import os
		>>> os.name # 操作系统类型
		'nt'
	```

* 如果是posix，说明系统是Linux、Unix或Mac OS X，如果是nt，就是Windows系统。

* 要获取详细的系统信息，可以调用uname()函数：

	```
		>>> os.uname()
		posix.uname_result(sysname='Darwin', nodename='MichaelMacPro.local', release='14.3.0', version='Darwin Kernel Version 14.3.0: Mon Mar 23 11:59:05 PDT 2015; root:xnu-2782.20.48~5/RELEASE_X86_64', machine='x86_64')
	```

* 注意uname()函数在Windows上不提供，也就是说，os模块的某些函数是跟操作系统相关的。

### 环境变量

* 在操作系统中定义的环境变量，全部保存在os.environ这个变量中，可以直接查看：

	```
		>>> os.environ
		environ({'VERSIONER_PYTHON_PREFER_32_BIT': 'no', 'TERM_PROGRAM_VERSION': '326', 'LOGNAME': 'michael', 'USER': 'michael', 'PATH': '/usr/bin:/bin:/usr/sbin:/sbin:/usr/local/bin:/opt/X11/bin:/usr/local/mysql/bin', ...})
	```

* 要获取某个环境变量的值，可以调用os.environ.get('key')：

	```
		>>> os.environ.get('PATH')
		'/usr/bin:/bin:/usr/sbin:/sbin:/usr/local/bin:/opt/X11/bin:/usr/local/mysql/bin'
		>>> os.environ.get('x', 'default')
		'default'
	```

### 操作文件和目录

* 操作文件和目录的函数一部分放在os模块中，一部分放在os.path模块中，这一点要注意一下。查看、创建和删除目录可以这么调用：

	```
		# 查看当前目录的绝对路径:
		>>> os.path.abspath('.')
		'/Users/michael'
		# 在某个目录下创建一个新目录，首先把新目录的完整路径表示出来:
		>>> os.path.join('/Users/michael', 'testdir')
		'/Users/michael/testdir'
		# 然后创建一个目录:
		>>> os.mkdir('/Users/michael/testdir')
		# 删掉一个目录:
		>>> os.rmdir('/Users/michael/testdir')
	```

* 把两个路径合成一个时，不要直接拼字符串，而要通过os.path.join()函数，这样可以正确处理不同操作系统的路径分隔符。在Linux/Unix/Mac下，os.path.join()返回这样的字符串：

	```
		part-1/part-2
	```

* 而Windows下会返回这样的字符串：

	```
		part-1\part-2
	```

* 同样的道理，要拆分路径时，也不要直接去拆字符串，而要通过os.path.split()函数，这样可以把一个路径拆分为两部分，后一部分总是最后级别的目录或文件名：

	```
		>>> os.path.split('/Users/michael/testdir/file.txt')
		('/Users/michael/testdir', 'file.txt')
	```

* os.path.splitext()可以直接让你得到文件扩展名，很多时候非常方便：

	```
		>>> os.path.splitext('/path/to/file.txt')
		('/path/to/file', '.txt')
	```

* 这些合并、拆分路径的函数并不要求目录和文件要真实存在，它们只对字符串进行操作。

* 文件操作使用下面的函数。假定当前目录下有一个test.txt文件：

	```
		# 对文件重命名:
		>>> os.rename('test.txt', 'test.py')
		# 删掉文件:
		>>> os.remove('test.py')
	```

* 但是复制文件的函数居然在os模块中不存在！原因是复制文件并非由操作系统提供的系统调用。理论上讲，我们通过上一节的读写文件可以完成文件复制，只不过要多写很多代码。

* 幸运的是shutil模块提供了copyfile()的函数，你还可以在shutil模块中找到很多实用函数，它们可以看做是os模块的补充。

* 最后看看如何利用Python的特性来过滤文件。比如我们要列出当前目录下的所有目录，只需要一行代码：

	```
		>>> [x for x in os.listdir('.') if os.path.isdir(x)]
		['.lein', '.local', '.m2', '.npm', '.ssh', '.Trash', '.vim', 'Applications', 'Desktop', ...]
	```

* 要列出所有的.py文件，也只需一行代码：

	```
		>>> [x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py']
		['apis.py', 'config.py', 'models.py', 'pymonitor.py', 'test_db.py', 'urls.py', 'wsgiapp.py']
	```

* Python的os模块封装了操作系统的目录和文件操作，要注意这些函数有的在os模块中，有的在os.path模块中。


## 序列化
