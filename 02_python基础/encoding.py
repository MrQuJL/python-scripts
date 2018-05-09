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




