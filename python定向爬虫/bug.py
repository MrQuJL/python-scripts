import re

#a = 'xy123'
#b = re.findall('x..', a)
# findall 返回一个list
#print(b)

#a = 'xyxy123'
#b = re.findall('x*', a)
#print(b)

#a = 'xy123'
#b = re.findall('x?', a)
#print(b)

#secret_code = 'xxIxxyuikb,gtxxlovexxmnhuiyuxxyouxx'
#b = re.findall('xx(.*?)xx', secret_code)
#print(b)

#for i in b:
#	print(i)

s = '''poipixxhello
xxurietxxworldxx'''

#b = re.findall('xx(.*?)xx', s, re.S)
# re.S的作用是使.包括\n
#print(b)


s2 = 'xxIxx123xxlovexxtytcvuxxyouxx'
f = re.search('xx(.*?)xx123xx(.*?)xx', s2).group(2)
#search 返回一个Match对象
#在确定只有一个内容时，使用search方法可以提高效率
#print(f)
m = re.findall('xx(.*?)xx123xx(.*?)xx', s2)
#返回一个list,里面有一个tuple，tuple里面有两个元素
#print(m[0][1])

s = '123abcssfasdfas123'
output = re.sub('123(.*?)123', '123%d123' % 789, s)
#sub 返回一个字符串
#print(output)

#不推荐使用compile

#匹配纯数字
a = 'asdfasf12345676iouioui'
b = re.findall('(\d+)', a)
print(b)


#常用技巧
#import re
#from re import *
#from re import findall,search,sub,S
#不需要compile
#使用\d+匹配纯数字


