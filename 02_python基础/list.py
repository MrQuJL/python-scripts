classmates = ['Michael', 'Bob', 'Tracy']

print(classmates)

print(len(classmates))

print(classmates[0])

print(classmates[1])

print(classmates[2])

#print(classmates[3])

print('''
''')

print(classmates[-1]) # 获取倒数第一个元素

print(classmates[len(classmates)-1])

classmates.append('Admin')

print(classmates)

# classmates.pop() # 类似一个栈

# print(classmates)

classmates.pop(2)

print(classmates)

classmates[1] = 'Sarah'

print(classmates)

L = ['Apple', 123, True]

print(L)

s = ['python', 'java', ['asp', 'jsp'], 'scheme']

print(s)

print(len(s))

p = ['asp', 'php']

s = ['python', 'java', p, 'scheme']

print(s[2][1])

L = []

print(len(L))

M = ['1', '2']

M.insert(1, True)

print(M)
