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

## struct

## hashlib

## hmac

## itertools

## contextlib

## urllib

## XML

## HTMLParser












