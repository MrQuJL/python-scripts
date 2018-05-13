from collections import Iterable

d = {'a':1,'b':2,'c':3}

#for key in d:
#	print(key)

for value in d.values():
	print(value)

print('-------------')

print(isinstance('abc', Iterable))

print(isinstance([1,2,3], Iterable))

print(isinstance(123, Iterable))

print('-----------------')

for i, value in enumerate(['A','B','C']):
	print(i, value)

for x, y in [(1,1),(2,4),(3,9)]:
	print(x, y)

print('开始定义函数----')

def findMinAndMax(L):
	if L == None or len(L) == 0:
		return (None, None)
	if len(L) == 1:
		return (L[0], L[0])
	min = L[0]
	max = L[0]
	for i in L:
		if i < min:
			min = i
		if i > max:
			max = i
	return (min, max)

if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')






