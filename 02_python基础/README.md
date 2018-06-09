# Python基础

## 转义字符

* 如果字符串内部既包含'又包含"怎么办？可以用转义字符\来标识，比如：
    
    ```'I\'m \"OK\"!'```

* 如果字符串里面有很多字符都需要转义，就需要加很多\，为了简化，Python还允许用r''表示''内部的字符串默认不转义，可以自己试试：

    ```print(r'\\\t\\')```

* 如果字符串内部有很多换行，用\n写在一行里不好阅读，为了简化，Python允许用'''...'''的格式表示多行内容(在三个单引号内换行直接敲回车即可，...表示由很多数据)

    ```
    print('''line1
    line2
    line3''')
    ```

* 如果在'''内还想不转义字符在前面加上r即可

    ```
    print(r'''hello,\n
    world''')
    ```

## 布尔值

* 布尔值和布尔代数的表示完全一致，一个布尔值只有True、False两种值，要么是True，要么是False，在Python中，可以直接用True、False表示布尔值（请注意大小写）

    ```
    print(True)
    print(False)
    print(3 > 2)
    print(2 > 3)
    ```

* and（与） or（或） not（非）

    ```
    if age > 18:
        print('adult')
    else:
        print('teenager')
    ```

## 空值

* 空值是Python里一个特殊的值，用None表示。None不能理解为0，因为0是有意义的，而None是一个特殊的空值

## 变量

* 变量的概念基本上和初中代数的方程变量是一致的，只是在计算机程序中，变量不仅可以是数字，还可以是任意数据类型。

* 变量在程序中就是用一个变量名表示了，变量名必须是大小写英文、数字和_的组合，且不能用数字开头

    ```
    a = 123 # a是整数

    print(a)

    a = 'ABC' # a变为字符串

    print(a)
    ```

* 这种变量本身类型不固定的语言称之为动态语言，与之对应的是静态语言。静态语言在定义变量时必须指定变量类型，如果赋值的时候类型不匹配，就会报错。

## 除法（精确除 VS 地板除）

    ```
    print(10 / 3)
    print(10 // 3)
    ```

## 小结

* 注意：Python的整数没有大小限制，而某些语言的整数根据其存储长度是有大小限制的，例如Java对32位整数的范围限制在-2147483648-2147483647。

* Python的浮点数也没有大小限制，但是超出一定范围就直接表示为inf（无限大）。

## python字符编码

* 在最新的Python 3版本中，字符串是以Unicode编码的，也就是说，Python的字符串支持多语言

* 对于单个字符的编码，Python提供了ord()函数获取字符的整数表示，chr()函数把编码转换为对应的字符

* 由于Python的字符串类型是str，在内存中以Unicode表示，一个字符对应若干个字节。如果要在网络上传输，或者保存到磁盘上，就需要把str变为以字节为单位的bytes

* 以Unicode表示的str通过encode()方法可以编码为指定的bytes

* 'ABC'.encode('ascii')

* 'ABC'.encode('utf-8')

* 'ABC'.encode('UTF8')

* 反过来，如果我们从网络或磁盘上读取了字节流，那么读到的数据就是bytes。要把bytes变为str，就需要用decode()方法

* 如果bytes中只有一小部分无效的字节，可以传入errors='ignore'忽略错误的字节：

    ```
    b'\xe4\xb8\xad\xff'.decode('utf-8', errors='ignore')
    ```

* 要计算str包含多少个字符，可以用len()函数

    ```
    len('ABC')
    len('中文')
    ```

* len()函数计算的是str的字符数，如果换成bytes，len()函数就计算字节数

    ```
    len(b'ABC')
    len(b'\xe4\xb8\xad\xe6\x96\x87')
    len('中文'.encode('utf-8'))
    ```

* 由于Python源代码也是一个文本文件，所以，当你的源代码中包含中文的时候，在保存源代码时，就需要务必指定保存为UTF-8编码。当Python解释器读取源代码时，为了让它按UTF-8编码读取，我们通常在文件开头写上这两行
    
    ```
    #!/usr/bin/env python3
    # -*- coding: utf-8 -*-
    ```

    第一行注释是为了告诉Linux/OS X系统，这是一个Python可执行程序，Windows系统会忽略这个注释；

    第二行注释是为了告诉Python解释器，按照UTF-8编码读取源代码，否则，你在源代码中写的中文输出可能会有乱码。

## 格式化

* 最后一个常见的问题是如何输出格式化的字符串。我们经常会输出类似'亲爱的xxx你好！你xx月的话费是xx，余额是xx'之类的字符串，而xxx的内容都是根据变量变化的，所以，需要一种简便的格式化字符串的方式。

* 在Python中，采用的格式化方式和C语言是一致的，用%实现，举例如下：

    ```
    >>> 'Hello, %s' % 'world'
    'Hello, world'
    >>> 'Hi, %s, you have $%d.' % ('Michael', 1000000)
    'Hi, Michael, you have $1000000.'
    ```

* %运算符就是用来格式化字符串的。在字符串内部，%s表示用字符串替换，%d表示用整数替换，有几个%?占位符，后面就跟几个变量或者值，顺序要对应好。如果只有一个%?，括号可以省略。

* 常见的占位符有 %d(整数) %f(浮点数) %s(字符串) %x(十六进制)

* 其中，格式化整数和浮点数还可以指定是否补0和整数与小数的位数

    ```
    print('%2d-%02d' % (3, 1))
    print('%.2f' % 3.1415926)
    ```

* 如果你不太确定应该用什么，%s永远起作用，它会把任何数据类型转换为字符串

* 有些时候，字符串里面的%是一个普通字符怎么办？这个时候就需要转义，用%%来表示一个%

    ```
    print('growth rate: %d %%' % 7)
    ```

* 另一种格式化字符串的方法是使用字符串的format()方法，它会用传入的参数依次替换字符串内的占位符{0}、{1}……，不过这种方式写起来比%要麻烦得多

    ```
    >>> 'Hello, {0}, 成绩提升了 {1:.1f}%'.format('小明', 17.125)
    ```

## list

* Python内置的一种数据类型是列表：list。list是一种有序的集合，可以随时添加和删除其中的元素

    ```
    >>> classmates = ['Michael', 'Bob', 'Tracy']
    >>> classmates
    ['qujianlei', 'Bob', 'Tracy']
    ```

* 变量classmates就是一个list。用len()函数可以获得list元素的个数

    ```
    >>> len(classmates)
    3
    ```

* 用索引来访问list中每一个位置的元素，记得索引是从0开始的

    ```
    >>> classmates[0]
    'qujianlei'
    >>> classmates[1]
    'Bob'
    >>> classmates[2]
    'Tracy'
    >>> classmates[3]
    Traceback (most recent call last):
     File "<stdin>", line 1, in <module>
    IndexError: list index out of rangev
    ```

* 记得最后一个元素的索引是len(classmates) - 1

* 如果要取最后一个元素，除了计算索引位置外，还可以用-1做索引，直接获取最后一个元素

    ```
    >>> classmates[-1]
    'Tracy'
    ```

* list是一个可变的有序表，所以，可以往list中追加元素到末尾：

    ```
    >>> classmates.append('Adam')
    >>> classmates
    ['Michael', 'Bob', 'Tracy', 'Adam']
    ```

* 也可以把元素插入到指定的位置，比如索引号为1的位置

    ```
    >>> classmates.insert(1, 'Jack')
    >>> classmates
    ['Michael', 'Jack', 'Bob', 'Tracy', 'Adam']
    ```

* 要删除list末尾的元素，用pop()方法

    ```
    >>> classmates.pop()
    'Adam'
    >>> classmates
    ['Michael', 'Jack', 'Bob', 'Tracy']
    ```

* 要删除指定位置的元素，用pop(i)方法，其中i是索引位置

* 要把某个元素替换成别的元素，可以直接赋值给对应的索引位置

* python对list里面的元素可以排序

* list里面的元素的数据类型也可以不同，比如：

* >>> L = ['Apple', 123, True]

* list元素也可以是另一个list，比如：

    ```
    >>> s = ['python', 'java', ['asp', 'php'], 'scheme']
    >>> len(s)
    4

    >>> p = ['asp', 'php']
    >>> s = ['python', 'java', p, 'scheme']
    ```

* 如果一个list中一个元素也没有，就是一个空的list，它的长度为0：

    ```
    >>> L = []
    >>> len(L)
    0
    ```

## tuple

* 另一种有序列表叫元组：tuple。tuple和list非常类似，但是tuple一旦初始化就不能修改，比如同样是列出同学的名字：

    ```
    >>> classmates = ('Michael', 'Bob', 'Tracy')
    ```

* 现在，classmates这个tuple不能变了，它也没有append()，insert()这样的方法。其他获取元素的方法和list是一样的，你可以正常地使用classmates[0]，classmates[-1]，但不能赋值成另外的元素。

* 不可变的tuple有什么意义？因为tuple不可变，所以代码更安全。如果可能，能用tuple代替list就尽量用tuple

* 一个元素的tuple为了避免引起歧义，需这样表示：

    ```
    >>> t = (1,)
    >>> t
    (1,)
    ```

* Python在显示只有1个元素的tuple时，也会加一个逗号,，以免你误解成数学计算意义上的括号。

* 注意tuple的不可变其实是指向的不可变，指向的如果是一个引用的话，那个引用所指向的内容是可变的。

## 条件判断

* 比如，输入用户年龄，根据年龄打印不同的内容，在Python程序中，用if语句实现：

    ```
    age = 3
    if age >= 18:
        print('adult')
    elif age >= 6:
      print('teenager')
    else:
      print('kid')
    ```
注意：是 ```elif```，python通过缩进来确定if下面需要执行多少条语句，所以如果需要写多条语句只需要通过缩进就可以了，例如：

    ```
    age = 3
    if age >= 18:
        print('your age is', age)
        print('adult')
    else:
        print('your age is', age)
        print('teenager')
    ```

* 注意：input返回的数据类型是str，需要使用int函数来转换成整数，例如：

    ```
    s = input('birth: ')
    birth = int(s)
    if birth < 2000:
        print('00前')
    else:
        print('00后')
    ```

## 循环

* 为了让计算机能计算成千上万次的重复运算，我们就需要循环语句

    ```
    names = ['Michael', 'Bob', 'Tracy']
    for name in names:
        print(name)
    ```

* Python提供一个range()函数，可以生成一个整数序列，再通过list()函数可以转换为list。比如range(5)生成的序列是从0开始小于5的整数

    ```
    >>> list(range(5))
    [0, 1, 2, 3, 4]
    ```

* range(101)就可以生成0-100的整数序列，计算如下：

    ```
    sum = 0
    for x in range(101):
        sum = sum + x
    print(sum)
    ```

* while循环如下：

    ```
    sum = 0
    n = 99
    while n > 0:
        sum = sum + n
        n = n - 2
    print(sum)
    ```
* continue + break

## dict

* Python内置了字典：dict的支持，dict全称dictionary，在其他语言中也称为map，使用键-值（key-value）存储，具有极快的查找速度。

    ```
    >>> d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
    >>> d['Michael']
    95
    ```

* 把数据放入dict的方法，除了初始化时指定外，还可以通过key放入：

    ```
    >>> d['Adam'] = 67
    >>> d['Adam']
    67
    ```

* 要避免key不存在的错误，有两种办法，一是通过in判断key是否存在
    
    ```
    >>> 'Thomas' in d
    False
    ```

* 二是通过dict提供的get()方法，如果key不存在，可以返回None，或者自己指定的value：

    ```
    >>> d.get('Thomas')
    >>> d.get('Thomas', -1)
    -1
    ```

* 注意：返回None的时候Python的交互环境不显示结果。

* 要删除一个key，用pop(key)方法，对应的value也会从dict中删除：

    ```
    >>> d.pop('Bob')
    75
    >>> d
    {'Michael': 95, 'Tracy': 85}
    ```

* dict有以下几个特点：
    
    1. 查找和插入的速度极快，不会随着key的增加而变慢
    2. 需要占用大量的内存，内存浪费多。

* list的特点：

    1. 查找和插入的时间随着元素的增加而增加
    2. 占用空间小，浪费内存很少

* 所以，dict是用空间来换取时间的一种方法。

* 正确使用dict非常重要，需要牢记的第一条就是dict的key必须是不可变对象。

## set

* set和dict类似，也是一组key的集合，但不存储value。由于key不能重复，所以，在set中，没有重复的key。

* 要创建一个set，需要提供一个list作为输入集合：

    ```
    >>> s = set([1, 2, 3])
    >>> s
    {1, 2, 3}
    ```

* 重复元素在set中自动被过滤：

    ```
    >>> s = set([1, 1, 2, 2, 3, 3])
    >>> s
    {1, 2, 3}
    ```

* 通过add(key)方法可以添加元素到set中，可以重复添加，但不会有效果：

    ```
    >>> s.add(4)
    >>> s
    {1, 2, 3, 4}
    >>> s.add(4)
    >>> s
    {1, 2, 3, 4}
    ```

* 通过remove(key)方法可以删除元素：

    ```
    >>> s.remove(4)
    >>> s
    {1, 2, 3}
    ```

* set可以看成数学意义上的无序和无重复元素的集合，因此，两个set可以做数学意义上的交集、并集等操作：

    ```
    >>> s1 = set([1, 2, 3])
    >>> s2 = set([2, 3, 4])
    >>> s1 & s2
    {2, 3}
    >>> s1 | s2
    {1, 2, 3, 4}
    ```

* a.sort() -- list的一个函数

* a.replace('a', 'A') -- str的一个函数















