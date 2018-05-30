from collections import namedtuple
from collections import deque
from collections import defaultdict
from collections import OrderedDict
from collections import Counter

p = (1, 2)

Point = namedtuple('Point', ['x', 'y'])
#用来定义一种数据类型
p = Point(1, 2)

#print(p.x)

#print(isinstance(p, Point))

Circle = namedtuple('Circle', ['x','y','z'])

c = Circle(1,2,3)

#print(c.y)

q = deque(['a','b','c'])
q.append('x')
q.appendleft('y')
#print(q)

dd = defaultdict(lambda : 'N/A')
dd['key1'] = 'abc'
#print(dd['key1'])
#print(dd['key2'])

d = dict([('b',2),('a',1),('c',3)])
print(d)

od = OrderedDict([('b',2),('a',1),('c',3)])
print(od)

od = OrderedDict()
od['z'] = 1
od['y'] = 2
od['x'] = 3
l = list(od.keys())
print(l)

c = Counter()
for ch in 'programming':
	c[ch] = c[ch] + 1

print(c)
