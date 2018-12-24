import requests
from lxml import etree

response = requests.get("https://www.jikexueyuan.com/course/")
html = response.content.decode('utf8')

selector = etree.HTML(html)

# 提取文本
content = selector.xpath('//ul[@class="cf"]/li/div[@class="lesson-infor"]/h2/a/text()')
for each in content:
    print(each)

# //定位根节点
# /往下层寻找
# 提取文本内容: /text()
# 提取属性内容: /@xxxx


#'//a/@href'

# //*[@id="useful"]/li[1]


## 特殊情况


# 1.以相同的字符开头的情况

# starts-with(@属性名称,属性字符相同的部分)
#
# <div id="test-1">需要的内容1</div>
# <div id="test-2">需要的内容2</div>
# <div id="testfault">需要的内容3</div>
#
#
# selector = etree.HTML('')
# selector.xpath('//div[starts-with(@id, "test")]/text()')


# 2.标签套标签的情况

# string(.)

html = '''
<div id="class3">美女，
    <font color=red>你的微信是多少？</font>
</div>
'''

selector = etree.HTML(html)

# 调用xpath获取的是一个element对象
data = selector.xpath('//div[@id="class3"]')[0]
info = data.xpath('string(.)')
info = info.replace('\n', '').replace(' ', '')
print(info)


## python并行化

# map的使用

from multiprocessing.dummy import Pool as ThreadPool
import time


# 两核
pool = ThreadPool(2)


def func():
    pass

time1 = time.time()
results = pool.map(func, "web1","web2")
time2 = time.time()
pool.close()
# 防止子进程还没运行完，主进程就退出了
pool.join()

print(str(time2 - time1))



