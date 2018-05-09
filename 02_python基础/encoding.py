print('包含中文的str')

print('''------''')

print(ord('A'))

print(ord('中'))

print(chr(25991))

print('\u4e2d\u6587')

print(b'ABC')

print('ABC'.encode('ascii'))

print(b'ABC'.decode('ascii'))

print(b'\xe4\xb8\xad\xff'.decode('utf-8',errors='ignore'))

print('中文两字儿的长度：', len('中文'))

print(len('中文'.encode('utf8')))

print(len(b'ABC'))

print('''换行符
''')

print('Hello, %s' % 'world')

print('Hi, %s, you have $%d' % ('Michael', 1000000))

print('%2d-%02d' % (3, 1))

print('%.2f' % 3.1415926)

print('Age: %s. Gender: %s' % (25, True))

print("growth rate: %d%%" % 7)

print('Hello, {0}, 成绩提升了 {1:.1f}%'.format('小明', 17.125))

s1 = 72

s2 = 85

r = (s2 - s1) / s1

r = r * 100

print('%.2f%%' % r)




