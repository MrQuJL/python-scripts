print(type(123))

print(type('str'))

print(type(None))

print(type(abs))

print('----------我是分割线----------')

print(type(123) == type(456))

print(type(123) == int)

print(type('abc') == type('abc'))

print(type('abc') == str)

print(type('abc') == type(123))

print('--------函数类型-------')

import types

def fn():
	pass

print(type(fn)==types.FunctionType)

print(type(abs)==types.BuiltinFunctionType)

print(type(lambda x:x)==types.LambdaType)

print(type(x for x in range(10))==types.GeneratorType)

print(isinstance([1,2,3],(list,tuple)))

print(isinstance((1,2,3),(list,tuple)))

#  总是优先使用isinstance()判断类型，可以将指定类型及其子类“一网打尽”。

print(dir('abc'))

print(len('ABC'))

print('ABC'.__len__())

class MyDog(object):
	def __len__(self):
		return 100

dog = MyDog()
print(len(dog))

print('ABC'.lower())

class MyObject(object):
	def __init__(self):
		self.x = 9
	def power(self):
		return self.x * self.x

obj = MyObject()

print('-----列出对象的一系列属性-----')

print(hasattr(obj,'x'))

print(obj.x)

print(hasattr(obj,'y'))

setattr(obj,'y',19)

print(hasattr(obj,'y'))

print(getattr(obj,'y'))

print(getattr(obj,'x'))

#getattr(obj,'z')

print(getattr(obj,'z',404))

print('-------获得对象的方法--------')

print(hasattr(obj,'power'))

print(getattr(obj,'power'))

fn = getattr(obj,'power')

print(fn())

sum = obj.x + obj.y

print(sum)

def readImage(fp):
	if hasattr(fp, 'read'):
		return readDate(fp)
	return None

