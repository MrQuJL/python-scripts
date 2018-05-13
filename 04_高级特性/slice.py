L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']

print(L[-2:])

L = list(range(100))

print('倒数第一个元素：' , L[-2:])

print(L[0:10])

print(L[-10:])

print(L[10:20])

print(L[:10:2])

print(L[::5])

M = L[:]

#print("M:", M)
#print("L:", L)

t = (0, 1, 2, 3, 4, 5)[:3]

print(t)

print('ABCDEFG'[:3])

def trim(s):
	start = 0
	end = len(s) - 1
	if s == '':
		return ''
	while start < len(s) and s[start] == ' ':
		start = start + 1
	while  end >= 0 and s[end] == ' ':
		end = end - 1
	if start >= len(s) or end < 0:
		return ''
	return s[start:end + 1]

print('   ABCD  def')
print(trim('   ABCD  def'))

if trim('hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')





