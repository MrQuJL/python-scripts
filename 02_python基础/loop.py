names = ['Michael', 'Bob', 'Tracy']

for name in names:
	print(name)

sum = 0
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in a:
	sum += i
print(sum)

print(list(range(6)))

for x in range(101):
	sum += x;
print(sum)

print('''------我是分割线------''')

sum = 0
n = 99
while n > 0:
	sum += n
	n -= 2
print(sum)

sum = 0
n = 1
while n < 100:
	if n & 0x1 == 1:
		sum += n
	n = n + 1
print(sum)

print('''------我是分割线------''')

L = ['Bart', 'Lisa', 'Adam']

for x in L:
	print('Hello,', x, '!')

n = 1
while n <= 100:
	if n > 10:
		break
	print(n)
	n = n + 1
print('END!')

n = 0
while n < 10:
	n = n + 1
	if n & 0x1 == 0:
		continue
	print(n)
print('End odd!')



