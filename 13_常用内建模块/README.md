# 常用内建模块

## datetime

* 如何获取当前日期和时间：

	```
		>>> from datetime import datetime
		>>> now = datetime.now() # 获取当前datetime
		>>> print(now)
		2015-05-18 16:28:07.198690
		>>> print(type(now))
		<class 'datetime.datetime'>
	```

* 获取指定日期和时间:

	```
		>>> from datetime import datetime
		>>> dt = datetime(2015, 4, 19, 12, 20) # 用指定日期时间创建datetime
		>>> print(dt)
		2015-04-19 12:20:00
	```

* 把一个datetime类型转换为timestamp只需要简单调用timestamp()方法：

	```
		>>> from datetime import datetime
		>>> dt = datetime(2015, 4, 19, 12, 20) # 用指定日期时间创建datetime
		>>> dt.timestamp() # 把datetime转换为timestamp
		1429417200.0
	```

* 注意Python的timestamp是一个浮点数。如果有小数位，小数位表示毫秒数。

* 要把timestamp转换为datetime，使用datetime提供的fromtimestamp()方法：

	```
		>>> from datetime import datetime
		>>> t = 1429417200.0
		>>> print(datetime.fromtimestamp(t))
		2015-04-19 12:20:00
	```

* str转换为datetime:

* 很多时候，用户输入的日期和时间是字符串，要处理日期和时间，首先必须把str转换为datetime。转换方法是通过datetime.strptime()实现，需要一个日期和时间的格式化字符串：

	```
		>>> from datetime import datetime
		>>> cday = datetime.strptime('2015-6-1 18:19:59', '%Y-%m-%d %H:%M:%S')
		>>> print(cday)
		2015-06-01 18:19:59
	```

* datetime转换为str:

* 如果已经有了datetime对象，要把它格式化为字符串显示给用户，就需要转换为str，转换方法是通过strftime()实现的，同样需要一个日期和时间的格式化字符串：

	```
		>>> from datetime import datetime
		>>> now = datetime.now()
		>>> print(now.strftime('%a, %b %d %H:%M'))
		Mon, May 05 16:28
	```

* datetime加减:

* 对日期和时间进行加减实际上就是把datetime往后或往前计算，得到新的datetime。加减可以直接用+和-运算符，不过需要导入timedelta这个类：

	```
		>>> from datetime import datetime, timedelta
		>>> now = datetime.now()
		>>> now
		datetime.datetime(2015, 5, 18, 16, 57, 3, 540997)
		>>> now + timedelta(hours=10)
		datetime.datetime(2015, 5, 19, 2, 57, 3, 540997)
		>>> now - timedelta(days=1)
		datetime.datetime(2015, 5, 17, 16, 57, 3, 540997)
		>>> now + timedelta(days=2, hours=12)
		datetime.datetime(2015, 5, 21, 4, 57, 3, 540997)
	```

* 可见，使用timedelta你可以很容易地算出前几天和后几天的时刻。

## collections

### namedtuple

* namedtuple是一个函数，它用来创建一个自定义的tuple对象，并且规定了tuple元素的个数，并可以用属性而不是索引来引用tuple的某个元素。

	```
		>>> from collections import namedtuple
		>>> Point = namedtuple('Point', ['x', 'y'])
		>>> p = Point(1, 2)
		>>> p.x
		1
		>>> p.y
		2
	```

### deque

* deque是为了高效实现插入和删除操作的双向列表，适合用于队列和栈：

	```
		>>> from collections import deque
		>>> q = deque(['a', 'b', 'c'])
		>>> q.append('x')
		>>> q.appendleft('y')
		>>> q
		deque(['y', 'a', 'b', 'c', 'x'])
	```

### defaultdict

* 使用dict时，如果引用的Key不存在，就会抛出KeyError。如果希望key不存在时，返回一个默认值，就可以用defaultdict：

	```
		>>> from collections import defaultdict
		>>> dd = defaultdict(lambda: 'N/A')
		>>> dd['key1'] = 'abc'
		>>> dd['key1'] # key1存在
		'abc'
		>>> dd['key2'] # key2不存在，返回默认值
		'N/A'
	```

### OrderedDict

* 使用dict时，Key是无序的。在对dict做迭代时，我们无法确定Key的顺序。

* 如果要保持Key的顺序，可以用OrderedDict：

	```
		>>> from collections import OrderedDict
		>>> d = dict([('a', 1), ('b', 2), ('c', 3)])
		>>> d # dict的Key是无序的
		{'a': 1, 'c': 3, 'b': 2}
		>>> od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
		>>> od # OrderedDict的Key是有序的
		OrderedDict([('a', 1), ('b', 2), ('c', 3)])
	```

### Counter

* Counter是一个简单的计数器，例如，统计字符出现的个数：

	```
		>>> from collections import Counter
		>>> c = Counter()
		>>> for ch in 'programming':
		...     c[ch] = c[ch] + 1
		...
		>>> c
		Counter({'g': 2, 'm': 2, 'r': 2, 'a': 1, 'i': 1, 'o': 1, 'n': 1, 'p': 1})
	```

## base64

* Base64是一种用64个字符来表示任意二进制数据的方法。

* 用记事本打开exe、jpg、pdf这些文件时，我们都会看到一大堆乱码，因为二进制文件包含很多无法显示和打印的字符，所以，如果要让记事本这样的文本处理软件能处理二进制数据，就需要一个二进制到字符串的转换方法。Base64是一种最常见的二进制编码方法。

* Base64的原理很简单，首先，准备一个包含64个字符的数组：

	```['A', 'B', 'C', ... 'a', 'b', 'c', ... '0', '1', ... '+', '/']```

* 然后，对二进制数据进行处理，每3个字节一组，一共是3x8=24bit，划为4组，每组正好6个bit

* 这样我们得到4个数字作为索引，然后查表，获得相应的4个字符，就是编码后的字符串。

* 所以，Base64编码会把3字节的二进制数据编码为4字节的文本数据，长度增加33%，好处是编码后的文本数据可以在邮件正文、网页等直接显示。

* 如果要编码的二进制数据不是3的倍数，最后会剩下1个或2个字节怎么办？Base64用\x00字节在末尾补足后，再在编码的末尾加上1个或2个=号，表示补了多少字节，解码的时候，会自动去掉。

* Python内置的base64可以直接进行base64的编解码：

	```
		>>> import base64
		>>> base64.b64encode(b'binary\x00string')
		b'YmluYXJ5AHN0cmluZw=='
		>>> base64.b64decode(b'YmluYXJ5AHN0cmluZw==')
		b'binary\x00string'
	```

* 由于标准的Base64编码后可能出现字符+和/，在URL中就不能直接作为参数，所以又有一种"url safe"的base64编码，其实就是把字符+和/分别变成-和_：

	```
		>>> base64.b64encode(b'i\xb7\x1d\xfb\xef\xff')
		b'abcd++//'
		>>> base64.urlsafe_b64encode(b'i\xb7\x1d\xfb\xef\xff')
		b'abcd--__'
		>>> base64.urlsafe_b64decode('abcd--__')
		b'i\xb7\x1d\xfb\xef\xff'
	```

* 由于标准的Base64编码后可能出现字符+和/，在URL中就不能直接作为参数，所以又有一种"url safe"的base64编码，其实就是把字符+和/分别变成-和_：

	```
		>>> base64.b64encode(b'i\xb7\x1d\xfb\xef\xff')
		b'abcd++//'
		>>> base64.urlsafe_b64encode(b'i\xb7\x1d\xfb\xef\xff')
		b'abcd--__'
		>>> base64.urlsafe_b64decode('abcd--__')
		b'i\xb7\x1d\xfb\xef\xff'
	```

* 还可以自己定义64个字符的排列顺序，这样就可以自定义Base64编码，不过，通常情况下完全没有必要。

* Base64是一种通过查表的编码方法，不能用于加密，即使使用自定义的编码表也不行。

* Base64适用于小段内容的编码，比如数字证书签名、Cookie的内容等。

* 由于=字符也可能出现在Base64编码中，但=用在URL、Cookie里面会造成歧义，所以，很多Base64编码后会把=去掉：

	```
		# 标准Base64:
		'abcd' -> 'YWJjZA=='
		# 自动去掉=:
		'abcd' -> 'YWJjZA'
	```

* 去掉=后怎么解码呢？因为Base64是把3个字节变为4个字节，所以，Base64编码的长度永远是4的倍数，因此，需要加上=把Base64字符串的长度变为4的倍数，就可以正常解码了。

* Base64是一种任意二进制到文本字符串的编码方法，常用于在URL、Cookie、网页中传输少量二进制数据。

## struct

* Python提供了一个struct模块来解决bytes和其他二进制数据类型的转换。

* struct的pack函数把任意数据类型变成bytes：

	```
		>>> import struct
		>>> struct.pack('>I', 10240099)
		b'\x00\x9c@c'
	```

* pack的第一个参数是处理指令，'>I'的意思是：

* >表示字节顺序是big-endian，也就是网络序，I表示4字节无符号整数。

* 后面的参数个数要和处理指令一致。

* unpack把bytes变成相应的数据类型：

	```
		>>> struct.unpack('>IH', b'\xf0\xf0\xf0\xf0\x80\x80')
		(4042322160, 32896)
	```

* 根据>IH的说明，后面的bytes依次变为I：4字节无符号整数和H：2字节无符号整数。

* 所以，尽管Python不适合编写底层操作字节流的代码，但在对性能要求不高的地方，利用struct就方便多了。

## hashlib

* Python的hashlib提供了常见的摘要算法，如MD5，SHA1等等。

* 什么是摘要算法呢？摘要算法又称哈希算法、散列算法。它通过一个函数，把任意长度的数据转换为一个长度固定的数据串（通常用16进制的字符串表示）。

* 我们以常见的摘要算法MD5为例，计算出一个字符串的MD5值：

	```
		import hashlib

		md5 = hashlib.md5()
		md5.update('how to use md5 in python hashlib?'.encode('utf-8'))
		print(md5.hexdigest())
	```

* 计算结果如下：

	```
		d26a53750bc40b38b65a520292f69306
	```

* 如果数据量很大，可以分块多次调用update()，最后计算的结果是一样的：

	```
		import hashlib

		md5 = hashlib.md5()
		md5.update('how to use md5 in '.encode('utf-8'))
		md5.update('python hashlib?'.encode('utf-8'))
		print(md5.hexdigest())
	```

* MD5是最常见的摘要算法，速度很快，生成结果是固定的128 bit字节，通常用一个32位的16进制字符串表示。

* 另一种常见的摘要算法是SHA1，调用SHA1和调用MD5完全类似：

	```
		import hashlib

		sha1 = hashlib.sha1()
		sha1.update('how to use sha1 in '.encode('utf-8'))
		sha1.update('python hashlib?'.encode('utf-8'))
		print(sha1.hexdigest())
	```

* SHA1的结果是160 bit字节，通常用一个40位的16进制字符串表示。

* 比SHA1更安全的算法是SHA256和SHA512，不过越安全的算法不仅越慢，而且摘要长度更长。

## hmac

* 通过哈希算法，我们可以验证一段数据是否有效，方法就是对比该数据的哈希值，例如，判断用户口令是否正确，我们用保存在数据库中的password_md5对比计算md5(password)的结果，如果一致，用户输入的口令就是正确的。

* 为了防止黑客通过彩虹表根据哈希值反推原始口令，在计算哈希的时候，不能仅针对原始输入计算，需要增加一个salt来使得相同的输入也能得到不同的哈希，这样，大大增加了黑客破解的难度。

* 如果salt是我们自己随机生成的，通常我们计算MD5时采用md5(message + salt)。但实际上，把salt看做一个“口令”，加salt的哈希就是：计算一段message的哈希时，根据不通口令计算出不同的哈希。要验证哈希值，必须同时提供正确的口令。

* 这实际上就是Hmac算法：Keyed-Hashing for Message Authentication。它通过一个标准算法，在计算哈希的过程中，把key混入计算过程中。

* 和我们自定义的加salt算法不同，Hmac算法针对所有哈希算法都通用，无论是MD5还是SHA-1。采用Hmac替代我们自己的salt算法，可以使程序算法更标准化，也更安全。

* Python自带的hmac模块实现了标准的Hmac算法。我们来看看如何使用hmac实现带key的哈希。

* 我们首先需要准备待计算的原始消息message，随机key，哈希算法，这里采用MD5，使用hmac的代码如下：

	```
		>>> import hmac
		>>> message = b'Hello, world!'
		>>> key = b'secret'
		>>> h = hmac.new(key, message, digestmod='MD5')
		>>> # 如果消息很长，可以多次调用h.update(msg)
		>>> h.hexdigest()
		'fa4ee7d173f2d97ee79022d1a7355bcf'
	```

* 可见使用hmac和普通hash算法非常类似。hmac输出的长度和原始哈希算法的长度一致。需要注意传入的key和message都是bytes类型，str类型需要首先编码为bytes。

* Python内置的hmac模块实现了标准的Hmac算法，它利用一个key对message计算“杂凑”后的hash，使用hmac算法比标准hash算法更安全，因为针对相同的message，不同的key会产生不同的hash。

## itertools

* Python的内建模块itertools提供了非常有用的用于操作迭代对象的函数。

* 首先，我们看看itertools提供的几个“无限”迭代器：

	```
		>>> import itertools
		>>> natuals = itertools.count(1)
		>>> for n in natuals:
		...     print(n)
		...
		1
		2
		3
		...
	```

* 因为count()会创建一个无限的迭代器，所以上述代码会打印出自然数序列，根本停不下来，只能按Ctrl+C退出。

* cycle()会把传入的一个序列无限重复下去：

	```
		>>> import itertools
		>>> cs = itertools.cycle('ABC') # 注意字符串也是序列的一种
		>>> for c in cs:
		...     print(c)
		...
		'A'
		'B'
		'C'
		'A'
		'B'
		'C'
		...
	```

* 同样停不下来。

* repeat()负责把一个元素无限重复下去，不过如果提供第二个参数就可以限定重复次数：

	```
		>>> ns = itertools.repeat('A', 3)
		>>> for n in ns:
		...     print(n)
		...
		A
		A
		A
	```

* 无限序列只有在for迭代时才会无限地迭代下去，如果只是创建了一个迭代对象，它不会事先把无限个元素生成出来，事实上也不可能在内存中创建无限多个元素。

* 无限序列虽然可以无限迭代下去，但是通常我们会通过takewhile()等函数根据条件判断来截取出一个有限的序列：

	```
		>>> natuals = itertools.count(1)
		>>> ns = itertools.takewhile(lambda x: x <= 10, natuals)
		>>> list(ns)
		[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
	```

* itertools提供的几个迭代器操作函数更加有用：

### chain()

* chain()可以把一组迭代对象串联起来，形成一个更大的迭代器：

	```
		>>> for c in itertools.chain('ABC', 'XYZ'):
		...     print(c)
		# 迭代效果：'A' 'B' 'C' 'X' 'Y' 'Z'
	```

### groupby()

* groupby()把迭代器中相邻的重复元素挑出来放在一起：

	```
		>>> for key, group in itertools.groupby('AAABBBCCAAA'):
		...     print(key, list(group))
		...
		A ['A', 'A', 'A']
		B ['B', 'B', 'B']
		C ['C', 'C']
		A ['A', 'A', 'A']
	```

* 实际上挑选规则是通过函数完成的，只要作用于函数的两个元素返回的值相等，这两个元素就被认为是在一组的，而函数返回值作为组的key。如果我们要忽略大小写分组，就可以让元素'A'和'a'都返回相同的key：

	```
		>>> for key, group in itertools.groupby('AaaBBbcCAAa', lambda c: c.upper()):
		...     print(key, list(group))
		...
		A ['A', 'a', 'a']
		B ['B', 'B', 'b']
		C ['c', 'C']
		A ['A', 'A', 'a']
	```

## contextlib

* 在Python中，读写文件这样的资源要特别注意，必须在使用完毕后正确关闭它们。正确关闭文件资源的一个方法是使用try...finally：

	```
		try:
			f = open('/path/to/file', 'r')
			f.read()
		finally:
			if f:
				f.close()
	```

* 写try...finally非常繁琐。Python的with语句允许我们非常方便地使用资源，而不必担心资源没有关闭，所以上面的代码可以简化为：

	```
		with open('/path/to/file', 'r') as f:
			f.read()
	```

* 并不是只有open()函数返回的fp对象才能使用with语句。实际上，任何对象，只要正确实现了上下文管理，就可以用于with语句。

* 实现上下文管理是通过__enter__和__exit__这两个方法实现的。例如，下面的class实现了这两个方法：

	```
		class Query(object):

			def __init__(self, name):
				self.name = name

			def __enter__(self):
				print('Begin')
				return self

			def __exit__(self, exc_type, exc_value, traceback):
				if exc_type:
					print('Error')
				else:
					print('End')

			def query(self):
				print('Query info about %s...' % self.name)
	```

* 这样我们就可以把自己写的资源对象用于with语句：

	```
		with Query('Bob') as q:
			q.query()
	```

### @contextmanager

* 编写__enter__和__exit__仍然很繁琐，因此Python的标准库contextlib提供了更简单的写法，上面的代码可以改写如下：

	```
		from contextlib import contextmanager

		class Query(object):

			def __init__(self, name):
				self.name = name

			def query(self):
				print('Query info about %s...' % self.name)

		@contextmanager
		def create_query(name):
			print('Begin')
			q = Query(name)
			yield q
			print('End')
	```

* @contextmanager这个decorator接受一个generator，用yield语句把with ... as var把变量输出出去，然后，with语句就可以正常地工作了：

	```
		with create_query('Bob') as q:
			q.query()
	```

* 很多时候，我们希望在某段代码执行前后自动执行特定代码，也可以用@contextmanager实现。例如：

	```
		@contextmanager
		def tag(name):
			print("<%s>" % name)
			yield
			print("</%s>" % name)

		with tag("h1"):
			print("hello")
			print("world")
	```

* 上述代码执行结果为：

	```
		<h1>
		hello
		world
		</h1>
	```

* 代码的执行顺序是：

	1. with语句首先执行yield之前的语句，因此打印出<h1>；
	2. yield调用会执行with语句内部的所有语句，因此打印出hello和world；
	3. 最后执行yield之后的语句，打印出</h1>。

* 因此，@contextmanager让我们通过编写generator来简化上下文管理。

### @closing

* 如果一个对象没有实现上下文，我们就不能把它用于with语句。这个时候，可以用closing()来把该对象变为上下文对象。例如，用with语句使用urlopen()：

	```
		from contextlib import closing
		from urllib.request import urlopen

		with closing(urlopen('https://www.python.org')) as page:
			for line in page:
				print(line)
	```

* closing也是一个经过@contextmanager装饰的generator，这个generator编写起来其实非常简单：

	```
		@contextmanager
		def closing(thing):
			try:
				yield thing
			finally:
				thing.close()
	```

* 它的作用就是把任意对象变为上下文对象，并支持with语句。

* @contextlib还有一些其他decorator，便于我们编写更简洁的代码。

## urllib

* urllib提供了一系列用于操作URL的功能。

### Get

* urllib的request模块可以非常方便地抓取URL内容，也就是发送一个GET请求到指定的页面，然后返回HTTP的响应：

* 例如，对豆瓣的一个URLhttps://api.douban.com/v2/book/2129650进行抓取，并返回响应：

	```
		from urllib import request

		with request.urlopen('https://api.douban.com/v2/book/2129650') as f:
			data = f.read()
			print('Status:', f.status, f.reason)
			for k, v in f.getheaders():
				print('%s: %s' % (k, v))
			print('Data:', data.decode('utf-8'))
	```

* 可以看到HTTP响应的头和JSON数据：

	```
		Status: 200 OK
		Server: nginx
		Date: Tue, 26 May 2015 10:02:27 GMT
		Content-Type: application/json; charset=utf-8
		Content-Length: 2049
		Connection: close
		Expires: Sun, 1 Jan 2006 01:00:00 GMT
		Pragma: no-cache
		Cache-Control: must-revalidate, no-cache, private
		X-DAE-Node: pidl1
		Data: {"rating":{"max":10,"numRaters":16,"average":"7.4","min":0},"subtitle":"","author":["廖雪峰编著"],"pubdate":"2007-6",...}
	```

* 如果我们要想模拟浏览器发送GET请求，就需要使用Request对象，通过往Request对象添加HTTP头，我们就可以把请求伪装成浏览器。例如，模拟iPhone 6去请求豆瓣首页：

	```
		from urllib import request

		req = request.Request('http://www.douban.com/')
		req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
		with request.urlopen(req) as f:
			print('Status:', f.status, f.reason)
			for k, v in f.getheaders():
				print('%s: %s' % (k, v))
			print('Data:', f.read().decode('utf-8'))
	```

* 这样豆瓣会返回适合iPhone的移动版网页：

	```
		...
			<meta name="viewport" content="width=device-width, user-scalable=no, initial-scale=1.0, minimum-scale=1.0, maximum-scale=1.0">
			<meta name="format-detection" content="telephone=no">
			<link rel="apple-touch-icon" sizes="57x57" href="http://img4.douban.com/pics/cardkit/launcher/57.png" />
		...
	```

### Post

* 如果要以POST发送一个请求，只需要把参数data以bytes形式传入。

* 我们模拟一个微博登录，先读取登录的邮箱和口令，然后按照weibo.cn的登录页的格式以username=xxx&password=xxx的编码传入：

	```
		from urllib import request, parse

		print('Login to weibo.cn...')
		email = input('Email: ')
		passwd = input('Password: ')
		login_data = parse.urlencode([
			('username', email),
			('password', passwd),
			('entry', 'mweibo'),
			('client_id', ''),
			('savestate', '1'),
			('ec', ''),
			('pagerefer', 'https://passport.weibo.cn/signin/welcome?entry=mweibo&r=http%3A%2F%2Fm.weibo.cn%2F')
		])

		req = request.Request('https://passport.weibo.cn/sso/login')
		req.add_header('Origin', 'https://passport.weibo.cn')
		req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
		req.add_header('Referer', 'https://passport.weibo.cn/signin/login?entry=mweibo&res=wel&wm=3349&r=http%3A%2F%2Fm.weibo.cn%2F')

		with request.urlopen(req, data=login_data.encode('utf-8')) as f:
			print('Status:', f.status, f.reason)
			for k, v in f.getheaders():
				print('%s: %s' % (k, v))
			print('Data:', f.read().decode('utf-8'))
	```

* 如果登录成功，我们获得的响应如下：

	```
		Status: 200 OK
		Server: nginx/1.2.0
		...
		Set-Cookie: SSOLoginState=1432620126; path=/; domain=weibo.cn
		...
		Data: {"retcode":20000000,"msg":"","data":{...,"uid":"1658384301"}}
	```

* 如果登录失败，我们获得的响应如下：

	```
		...
		Data: {"retcode":50011015,"msg":"\u7528\u6237\u540d\u6216\u5bc6\u7801\u9519\u8bef","data":{"username":"example@python.org","errline":536}}
	```

### Handler

* 如果还需要更复杂的控制，比如通过一个Proxy去访问网站，我们需要利用ProxyHandler来处理，示例代码如下：

	```
		proxy_handler = urllib.request.ProxyHandler({'http': 'http://www.example.com:3128/'})
		proxy_auth_handler = urllib.request.ProxyBasicAuthHandler()
		proxy_auth_handler.add_password('realm', 'host', 'username', 'password')
		opener = urllib.request.build_opener(proxy_handler, proxy_auth_handler)
		with opener.open('http://www.example.com/login.html') as f:
			pass
	```

* urllib提供的功能就是利用程序去执行各种HTTP请求。如果要模拟浏览器完成特定功能，需要把请求伪装成浏览器。伪装的方法是先监控浏览器发出的请求，再根据浏览器的请求头来伪装，User-Agent头就是用来标识浏览器的。

## XML

* XML虽然比JSON复杂，在Web中应用也不如以前多了，不过仍有很多地方在用，所以，有必要了解如何操作XML。

### DOM vs SAX

* 操作XML有两种方法：DOM和SAX。DOM会把整个XML读入内存，解析为树，因此占用内存大，解析慢，优点是可以任意遍历树的节点。SAX是流模式，边读边解析，占用内存小，解析快，缺点是我们需要自己处理事件。

* 正常情况下，优先考虑SAX，因为DOM实在太占内存。

* 在Python中使用SAX解析XML非常简洁，通常我们关心的事件是start_element，end_element和char_data，准备好这3个函数，然后就可以解析xml了。

* 举个例子，当SAX解析器读到一个节点时：

	```html
		<a href="/">python</a>
	```

会产生3个事件：

1. start_element事件，在读取<a href="/">时；

2. char_data事件，在读取python时；

3. end_element事件，在读取</a>时。

* 用代码实验一下：

	```python
		from xml.parsers.expat import ParserCreate

		class DefaultSaxHandler(object):
			def start_element(self, name, attrs):
				print('sax:start_element: %s, attrs: %s' % (name, str(attrs)))

			def end_element(self, name):
				print('sax:end_element: %s' % name)

			def char_data(self, text):
				print('sax:char_data: %s' % text)

		xml = r'''<?xml version="1.0"?>
		<ol>
			<li><a href="/python">Python</a></li>
			<li><a href="/ruby">Ruby</a></li>
		</ol>
		'''

		handler = DefaultSaxHandler()
		parser = ParserCreate()
		parser.StartElementHandler = handler.start_element
		parser.EndElementHandler = handler.end_element
		parser.CharacterDataHandler = handler.char_data
		parser.Parse(xml)
	```

* 需要注意的是读取一大段字符串时，CharacterDataHandler可能被多次调用，所以需要自己保存起来，在EndElementHandler里面再合并。

* 除了解析XML外，如何生成XML呢？99%的情况下需要生成的XML结构都是非常简单的，因此，最简单也是最有效的生成XML的方法是拼接字符串：

	```
		L = []
		L.append(r'<?xml version="1.0"?>')
		L.append(r'<root>')
		L.append(encode('some & data'))
		L.append(r'</root>')
		return ''.join(L)
	```

* 如果要生成复杂的XML呢？建议你不要用XML，改成JSON。

* 解析XML时，注意找出自己感兴趣的节点，响应事件时，把节点数据保存起来。解析完毕后，就可以处理数据。

## HTMLParser

* 如果我们要编写一个搜索引擎，第一步是用爬虫把目标网站的页面抓下来，第二步就是解析该HTML页面，看看里面的内容到底是新闻、图片还是视频。

* 假设第一步已经完成了，第二步应该如何解析HTML呢？

* HTML本质上是XML的子集，但是HTML的语法没有XML那么严格，所以不能用标准的DOM或SAX来解析HTML。

* 好在Python提供了HTMLParser来非常方便地解析HTML，只需简单几行代码：

	```python
		from html.parser import HTMLParser
		from html.entities import name2codepoint

		class MyHTMLParser(HTMLParser):

			def handle_starttag(self, tag, attrs):
				print('<%s>' % tag)

			def handle_endtag(self, tag):
				print('</%s>' % tag)

			def handle_startendtag(self, tag, attrs):
				print('<%s/>' % tag)

			def handle_data(self, data):
				print(data)

			def handle_comment(self, data):
				print('<!--', data, '-->')

			def handle_entityref(self, name):
				print('&%s;' % name)

			def handle_charref(self, name):
				print('&#%s;' % name)

		parser = MyHTMLParser()
		parser.feed('''<html>
		<head></head>
		<body>
		<!-- test html parser -->
			<p>Some <a href=\"#\">html</a> HTML&nbsp;tutorial...<br>END</p>
		</body></html>''')
	```

* feed()方法可以多次调用，也就是不一定一次把整个HTML字符串都塞进去，可以一部分一部分塞进去。

* 特殊字符有两种，一种是英文表示的&nbsp;，一种是数字表示的&#1234;，这两种字符都可以通过Parser解析出来。

* 利用HTMLParser，可以把网页中的文本、图像等解析出来。
