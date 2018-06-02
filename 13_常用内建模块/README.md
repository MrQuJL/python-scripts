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

## hmac

## itertools

## contextlib

## urllib

## XML

## HTMLParser












